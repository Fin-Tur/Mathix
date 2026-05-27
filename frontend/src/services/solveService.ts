import type { StreamHandle } from './api'
import type { SolveStreamEvent, Task, Solution, TokenSummary } from '../types/solve'

type EventCallback = (event: SolveStreamEvent) => void

const delay = (ms: number) => new Promise<void>((r) => setTimeout(r, ms))

async function runMockStream(input: string, onEvent: EventCallback, signal: { cancelled: boolean }) {
  await delay(500)
  if (signal.cancelled) return

  const mockTask: Task = {
    id: 1,
    description: input.slice(0, 120) || 'Gegeben sei f(x) = (x³ - 8) / (x - 2). Untersuche folgendes:',
    parameters: {},
    categories: ['limits', 'calculus'],
    subtasks: [
      { id: 1, description: 'Berechne lim_{x→2} f(x)', parameters: {} },
      { id: 2, description: "Bestimme f'(x) für x ≠ 2", parameters: {} },
      { id: 3, description: 'Finde und klassifiziere die kritischen Punkte von g(x) = x⁴ - 4x²', parameters: {} },
    ],
  }

  onEvent({ type: 'task_extracted', data: [mockTask] })
  await delay(300)
  if (signal.cancelled) return

  const toolCalls = [
    { name: 'solve_limit', args: "{'expr': '(x^3 - 8) / (x - 2)', 'variable': 'x', 'point': '2'}" },
    { name: 'solve_derivative', args: "{'expr': 'x**2 + 2*x + 4', 'variable': 'x'}" },
  ]

  for (const tc of toolCalls) {
    onEvent({ type: 'tool_call', data: tc })
    await delay(350)
    if (signal.cancelled) return
  }

  const solutions: Array<{ sol: Solution; explanation: string }> = [
    {
      sol: { subtaskId: 1, result: '12', explanation: '' },
      explanation:
        'Der Grenzwert von f(x) = (x³ - 8)/(x - 2) für x → 2 ist 12. Durch Faktorisierung ergibt sich x³ - 8 = (x - 2)(x² + 2x + 4), also f(x) = x² + 2x + 4 für x ≠ 2. Somit: lim_{x→2} f(x) = 4 + 4 + 4 = 12.',
    },
    {
      sol: { subtaskId: 2, result: "f'(x) = 2x + 2", explanation: '' },
      explanation:
        "Für x ≠ 2 vereinfacht sich f(x) = (x³ - 8)/(x - 2) zu x² + 2x + 4. Die Ableitung ergibt: f'(x) = 2x + 2.",
    },
    {
      sol: {
        subtaskId: 3,
        result: 'x = -√2 (lok. Min.), x = 0 (lok. Max.), x = √2 (lok. Min.)',
        explanation: '',
      },
      explanation:
        "Kritische Punkte: g'(x) = 4x³ - 8x = 4x(x² - 2) = 0 → x ∈ {0, ±√2}. Zweiter Ableitungstest: g''(0) = -8 < 0 (Max.), g''(±√2) = 16 > 0 (Min.).",
    },
  ]

  for (const { sol, explanation } of solutions) {
    await delay(200)
    if (signal.cancelled) return

    const words = explanation.split(' ')
    for (const word of words) {
      onEvent({ type: 'token', data: word + ' ' })
      await delay(35)
      if (signal.cancelled) return
    }

    onEvent({ type: 'solution', data: sol })
    await delay(400)
    if (signal.cancelled) return
  }

  const summary: TokenSummary = {
    t_in: 4820,
    t_out: 1240,
    t_c_read: 3100,
    t_c_write: 512,
    cost_usd: 0.007225,
  }
  onEvent({ type: 'done', data: summary })
}

export function submitSolveText(text: string, onEvent: EventCallback): StreamHandle {
  const signal = { cancelled: false }
  runMockStream(text, onEvent, signal)
  return { cancel: () => { signal.cancelled = true } }
}

export function submitSolvePdf(file: File, onEvent: EventCallback): StreamHandle {
  const signal = { cancelled: false }
  runMockStream(`[PDF: ${file.name}]`, onEvent, signal)
  return { cancel: () => { signal.cancelled = true } }
}
