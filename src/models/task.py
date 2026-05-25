import anthropic
from typing import Literal
from pydantic import BaseModel
from models.token_cost import TokenModel

TaskCategory = Literal[
    "limits", "calculus", "series",
    "la_vectors", "la_matrices",
    "multivar", "multivar_integrals", "vector_analysis", "ode",
    "proof",
]

class SubTask(BaseModel):
     id: int
     parameters: dict
     description: str

class Task(BaseModel):
      id: int
      description: str
      parameters: dict
      subtasks: list[SubTask]
      categories: list[TaskCategory]
      sols: list[str]

class TaskList(BaseModel):
      tasks: list[Task]

class Solution(BaseModel):
      subtask_id: int
      result: str
      explanation: str
      tokens: TokenModel

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
Task.categories   — One or more math domains required by this task. Choose from:
                    "limits"             — limits, sequences, continuity
                    "calculus"           — derivatives, integrals (single-variable)
                    "series"             — Taylor/Maclaurin series, convergence radius
                    "la_vectors"         — vectors, vector spaces, orthogonality, Gram-Schmidt
                    "la_matrices"        — matrices, linear systems, eigenvalues, decompositions
                    "multivar"           — partial derivatives, gradient, Hessian, Lagrange, Jacobian
                    "multivar_integrals" — double/triple integrals, line integrals
                    "vector_analysis"    — divergence, curl, Laplacian, conservative fields, potential
                    "ode"                — ordinary differential equations
                    "proof"              — proofs by induction or other formal arguments
                    A task may require multiple categories, e.g. ["multivar", "multivar_integrals"].
Task.sols         — Always [].

SubTask.description — Full verbatim text of this sub-task only.
SubTask.parameters  — Values stated explicitly in THIS sub-task that are not already in Task.parameters.
                      Empty dict if all needed values come from the parent.

RULES:
- Copy all mathematical expressions verbatim (do not simplify or reformat).
- If a value appears in the parent context, put it in Task.parameters — not repeated in each SubTask.
- Sub-task parameters only contain values unique to that sub-task."""

def extract_tasks_from_pdf(client: anthropic.Anthropic, pdf_text: str = "", image_blocks: list[dict] | None = None) -> tuple[list[Task], TokenModel]:
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

    tokens = TokenModel(t_in=response.usage.input_tokens, t_out=response.usage.output_tokens, t_c_read=0, t_c_write=0)

    return (response.parsed_output.tasks, tokens)
