export type TaskCategory =
  | 'limits'
  | 'calculus'
  | 'series'
  | 'la_vectors'
  | 'la_matrices'
  | 'multivar'
  | 'multivar_integrals'
  | 'vector_analysis'
  | 'ode'
  | 'proof'

export interface SubTask {
  id: number
  description: string
  parameters: Record<string, string>
}

export interface Task {
  id: number
  description: string
  parameters: Record<string, string>
  categories: TaskCategory[]
  subtasks: SubTask[]
}

export interface Solution {
  subtaskId: number
  result: string
  explanation: string
}

export interface TokenSummary {
  t_in: number
  t_out: number
  t_c_read: number
  t_c_write: number
  cost_usd: number
}

export type SolveStreamEvent =
  | { type: 'task_extracted'; data: Task[] }
  | { type: 'tool_call'; data: { name: string; args: string } }
  | { type: 'token'; data: string }
  | { type: 'solution'; data: Solution }
  | { type: 'done'; data: TokenSummary }
