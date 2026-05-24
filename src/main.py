import os
import sys
import anthropic
import reader.pdfreader_img as PDFReaderIMG
from reader.pdfreader import PDFReader
from models.task import Task, TaskList, Solution, extract_tasks_from_pdf
from models.tools import TOOLS, TOOL_MAP

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def run_task(task: Task) -> Solution:

    content = f"{task.description}\nParameters: {task.parameters}"
    if task.parameters_global:
        content += f"\nGlobal context: {task.parameters_global}"
    messages = [{"role": "user", "content": content}]

    #TODO: Append sols to Task

    while True:

        response = client.messages.parse(
            model="claude-haiku-4-5",
            max_tokens=1024,
            system =[{
                "type": "text", 
                "text": "You are a brilliant mathematican and problem solver. You will be given mathematical problems in the Task format and you will solve them using the tools at your disposal.",
                "cache_control": {"type": "ephemeral"},
                }],
            tools=TOOLS,
            output_format=Solution,
            messages=messages,
        )

        u = response.usage
        print(f"[cache] write={u.cache_creation_input_tokens}  "
        f"read={u.cache_read_input_tokens}  "
        f"uncached={u.input_tokens}"
        f"total(round)={u}")

        if response.stop_reason == "end_turn":
            response.parsed_output.task_id = task.id
            return response.parsed_output

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


if __name__ == "__main__":

    pdf_path = sys.argv[1] if len(sys.argv) > 1 else None

    if not pdf_path:
        sys.exit("Usage: python main.py <path_to_pdf>")

    pdf_text = PDFReader(pdf_path).read_all()

    if pdf_text.strip():
        tasks = extract_tasks_from_pdf(client, pdf_text)
    else:
        print("No text found in PDF — falling back to image-based extraction.")
        image_blocks = PDFReaderIMG.PDFReaderImg(pdf_path).all_as_blocks()
        tasks = extract_tasks_from_pdf(client, image_blocks=image_blocks)

    sols = []

    for task in tasks:
        print(f"Running task {task.id}: {task.description}")
        solution = run_task(task)
        sols.append(solution)
        print(f"Solution for task {task.id}: {solution.result}\nExplanation: {solution.explanation}\n")


