import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { Task, Solution, TokenSummary, SolveStreamEvent } from '../types/solve'
import { useStream } from '../composables/useStream'
import { submitSolveText, submitSolvePdf } from '../services/solveService'

export const useSolveStore = defineStore('solve', () => {
  const inputMode = ref<'pdf' | 'text'>('pdf')
  const file = ref<File | null>(null)
  const textInput = ref('')
  const tasks = ref<Task[]>([])
  const solutions = ref<Record<number, Solution>>({})
  const tokenSummary = ref<TokenSummary | null>(null)
  const error = ref<string | null>(null)

  const stream = useStream<SolveStreamEvent>()
  const { lines, isActive, start, appendLine, stop, reset: resetStream } = stream

  function setFile(f: File | null) {
    file.value = f
  }

  function setTextInput(text: string) {
    textInput.value = text
  }

  function toggleMode() {
    inputMode.value = inputMode.value === 'pdf' ? 'text' : 'pdf'
    file.value = null
    textInput.value = ''
  }

  function handleEvent(event: SolveStreamEvent) {
    if (event.type === 'task_extracted') {
      tasks.value = event.data
    } else if (event.type === 'tool_call') {
      appendLine(`->${event.data.name}(${event.data.args})`)
    } else if (event.type === 'token') {
      const last = lines.value[lines.value.length - 1]
      if (last !== undefined && !last.startsWith('->') && !last.startsWith('Solution') && !last.startsWith('Running')) {
        lines.value[lines.value.length - 1] = last + event.data
      } else {
        appendLine(event.data)
      }
    } else if (event.type === 'solution') {
      solutions.value = { ...solutions.value, [event.data.subtaskId]: event.data }
      appendLine(`\nSolution for subtask ${event.data.subtaskId}: ${event.data.result}\n`)
    } else if (event.type === 'done') {
      tokenSummary.value = event.data
      stop()
    }
  }

  function startStream() {
    error.value = null
    tasks.value = []
    solutions.value = {}
    tokenSummary.value = null

    const serviceCall = (onEvent: (e: SolveStreamEvent) => void) => {
      if (inputMode.value === 'pdf' && file.value) {
        return submitSolvePdf(file.value, onEvent)
      }
      return submitSolveText(textInput.value, onEvent)
    }

    start(serviceCall, handleEvent)
  }

  function cancelStream() {
    stop()
  }

  function resetAll() {
    resetStream()
    file.value = null
    textInput.value = ''
    tasks.value = []
    solutions.value = {}
    tokenSummary.value = null
    error.value = null
  }

  return {
    inputMode,
    file,
    textInput,
    tasks,
    solutions,
    tokenSummary,
    error,
    lines,
    isActive,
    setFile,
    setTextInput,
    toggleMode,
    startStream,
    cancelStream,
    resetAll,
  }
})
