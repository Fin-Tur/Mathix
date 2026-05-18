import anthropic
from pydantic import BaseModel

class Task(BaseModel):
      id: int
      description: str
      parameters: dict

class TaskList(BaseModel):
      tasks: list[Task]

class Solution(BaseModel):
      task_id: int
      result: str
      explanation: str

_EXTRACT_INSTRUCTION = """Extract every individual mathematical (sub-)task from this content.

Rules:
- Each numbered or lettered sub-task (a), b), 1., 2., ...) must become its own Task entry.
- description: the full task text INCLUDING the concrete mathematical expression or set, verbatim.
  Do NOT summarise or paraphrase — copy the exact formula, sequence, or set notation.
- parameters: a dict of named values mentioned in the task, e.g.
  {"expr": "n/(n+1)", "variable": "n"} or {"set": "{1/n | n in N}"}.
  Leave empty dict if no explicit parameters are stated.
- If a task has no sub-parts, create one entry for the whole task."""

def extract_tasks_from_pdf(client: anthropic.Anthropic, pdf_text: str = "", image_blocks: list[dict] | None = None) -> list[Task]:
    if image_blocks:
        content = image_blocks + [{"type": "text", "text": _EXTRACT_INSTRUCTION}]
    else:
        content = f"{_EXTRACT_INSTRUCTION}\n\n{pdf_text}"

    response = client.messages.parse(
        model="claude-haiku-4-5",
        max_tokens=4096,
        messages=[{"role": "user", "content": content}],
        output_format=TaskList,
    )

    return response.parsed_output.tasks

