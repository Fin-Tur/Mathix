import os
import sys
import anthropic
import reader.pdfreader_img as PDFReaderIMG
from reader.pdfreader import PDFReader
from models.task import Task, TaskList, Solution, extract_tasks_from_pdf
from models.tools import TOOLS, TOOL_MAP

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def run_task(task: Task) -> Solution:

    messages = [{"role": "user", "content": f"{task.description}\nParameters: {task.parameters}"}]


    while True:

        response = client.messages.parse(
            model="claude-haiku-4-5",
            max_tokens=1024,
            system="You are a brilliant mathematican and problem solver. You will be given mathematical problems per text or via pdf and you will solve them using the tools at your disposal.",
            tools=TOOLS,
            output_format=Solution,
            messages=messages,
        )

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
     
    pdf_path = sys.argv[2] if len(sys.argv) > 2 else None

    if not pdf_path:
        sys.exit("PDF path not provided.")

    if pdf_path:
        pdf_text = PDFReader(pdf_path).read_all()
        tasks = extract_tasks_from_pdf(client, pdf_text)

    sols = []

    for task in tasks:
        print(f"Running task {task.id}: {task.description}")
        solution = run_task(task)
        sols.append(solution)
        print(f"Solution for task {task.id}: {solution.result}\nExplanation: {solution.explanation}\n")


