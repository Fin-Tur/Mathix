import anthropic
from pydantic import BaseModel

class SubTask(BaseModel):
     id: int
     parameters: dict
     description: str

class Task(BaseModel):
      id: int
      description: str
      parameters: dict
      subtasks: list[SubTask]
      sols: list[str]

class TaskList(BaseModel):
      tasks: list[Task]

class Solution(BaseModel):
      task_id: int
      result: str
      explanation: str

_EXTRACT_INSTRUCTION = """Extract all mathematical tasks from the content into the TaskList structure.

STRUCTURE:
- Task = a top-level problem (may contain sub-tasks)
- SubTask = a lettered/numbered part (a), b), 1., 2., ...)

FIELD RULES:

Task.description  — Full text of the top-level problem statement. Verbatim, no paraphrasing.
Task.parameters   — Shared values defined at the top level and reused across sub-tasks.
                    e.g. {"A": "[[2,1,-1],[4,3,1],[0,2,3]]", "b": "[1,7,4]", "f": "(x**3-8)/(x-2)"}
                    Empty dict if nothing is shared.
Task.subtasks     — One SubTask per lettered/numbered part. If no sub-parts exist, one SubTask
                    containing the whole problem.
Task.sols         — Always [].

SubTask.description — Full verbatim text of this sub-task only.
SubTask.parameters  — Values stated explicitly in THIS sub-task that are not already in Task.parameters.
                      Empty dict if all needed values come from the parent.

RULES:
- Copy all mathematical expressions verbatim (do not simplify or reformat).
- If a value appears in the parent context, put it in Task.parameters — not repeated in each SubTask.
- Sub-task parameters only contain values unique to that sub-task."""

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

