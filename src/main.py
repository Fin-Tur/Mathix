import os
import sys
import anthropic
import reader.pdfreader_img as PDFReaderIMG
from reader.pdfreader import PDFReader
from models.task import Task, TaskList, Solution, extract_tasks_from_pdf
from models.tools import get_tools, TOOL_MAP
from models.token_cost import TokenModel, calculate_cost, LLM

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def run_task(task: Task) -> list[Solution]:

    solutions = []

    for sub in task.subtasks:

        t_in = 0
        t_out = 0
        t_c_read = 0
        t_c_write = 0

        content = f"{task.description}\nTask Parameters: {task.parameters}"
        content += f"{sub.description}\nSubTask Parameters: {sub.parameters}"
        
        if task.sols:
            content += "The previous solutions are\n:" + "\n".join(task.sols)

        messages = [{"role": "user", "content": content}]

        while True:
            response = client.messages.parse(
                model="claude-haiku-4-5",
                max_tokens=1024,
                system =[{
                    "type": "text",
                    "text": "You are a brilliant mathematician and problem solver. You will be given mathematical problems in the Task and Subtask format and you will solve them using the tools at your disposal. "
                    "You have the solutions to the previous subtasks in your context. Calculate every result only once and reuse previous results whenever possible.\n"
                    "Input formats: vectors as JSON strings e.g. '[1,2,3]', matrices as nested JSON strings e.g. '[[1,2],[3,4]]', infinity as 'oo', negative infinity as '-oo'.",
                    "cache_control": {"type": "ephemeral"},
                    }],
                tools=get_tools(task.categories),
                output_format=Solution,
                messages=messages,
            )

            usage = response.usage
            t_in += usage.input_tokens
            t_out += usage.output_tokens
            t_c_read += usage.cache_read_input_tokens or 0
            t_c_write += usage.cache_creation_input_tokens or 0
             

            if response.stop_reason == "end_turn":
                sol = response.parsed_output
                sol.tokens = TokenModel(t_in=t_in, t_out=t_out, t_c_read=t_c_read, t_c_write=t_c_write)
                sol.subtask_id = sub.id
                task.sols.append(f"Subtask {sub.id} ({sub.description}): {sol.result}")
                solutions.append(sol)
                break

            if response.stop_reason == "tool_use":
                messages.append({"role": "assistant", "content": response.content})
                results = []
                for block in response.content:
                    if block.type == "tool_use":
                        print(f"->{block.name}({block.input})")
                        ergebnis = TOOL_MAP[block.name](**block.input)
                        results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": str(ergebnis),
                        })

                messages.append({"role": "user", "content": results})
            
    return solutions


if __name__ == "__main__":

    pdf_path = sys.argv[1] if len(sys.argv) > 1 else None

    if not pdf_path:
        sys.exit("Usage: python main.py <path_to_pdf>")

    pdf_text = PDFReader(pdf_path).read_all()

    if pdf_text.strip():
        tasks, extract_cost = extract_tasks_from_pdf(client, pdf_text)
    else:
        print("No text found in PDF — falling back to image-based extraction.")
        image_blocks = PDFReaderIMG.PDFReaderImg(pdf_path).all_as_blocks()
        tasks, extract_cost = extract_tasks_from_pdf(client, image_blocks=image_blocks)

    sols = []

    for task in tasks:
        print(f"Running task {task.id}: {task.description}, {task.categories}")
        task_solutions = run_task(task)
        sols.extend(task_solutions)
        for sol in task_solutions:
            print(f"Solution for subtask {sol.subtask_id}: {sol.result}\nExplanation: {sol.explanation}\n")

    cost = calculate_cost([sol.tokens for sol in sols] + [extract_cost], LLM.haiku_45)
    print(f"\nTotal Cost: {cost}")




