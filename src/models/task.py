from http import client

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

def extract_tasks_from_pdf(client: anthropic.Anthropic, pdf_text: str) -> list[Task]:
    response = client.messages.parse(
        model="claude-haiku-4-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": f"Extract all tasks:\n{pdf_text}"}],
        output_format=TaskList, 
    )

    return response.parsed_output.tasks 

