import { ref } from 'vue'
import type { StreamHandle } from '../services/api'

export function useStream<T>() {
  const lines = ref<string[]>([])
  const isActive = ref(false)
  let handle: StreamHandle | null = null

  function start(
    serviceCall: (onEvent: (event: T) => void) => StreamHandle,
    onEvent: (event: T) => void,
  ) {
    lines.value = []
    isActive.value = true

    handle = serviceCall((event) => {
      onEvent(event)
    })
  }

  function appendLine(text: string) {
    lines.value.push(text)
  }

  function stop() {
    handle?.cancel()
    isActive.value = false
    handle = null
  }

  function reset() {
    stop()
    lines.value = []
  }

  return { lines, isActive, start, appendLine, stop, reset }
}
