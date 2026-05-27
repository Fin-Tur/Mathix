import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { VerifyResult, TokenSummary, VerifyStreamEvent } from '../types/verify'
import { useStream } from '../composables/useStream'
import { submitVerifyText, submitVerifyImage } from '../services/verifyService'

export const useVerifyStore = defineStore('verify', () => {
  const inputMode = ref<'image' | 'text'>('image')
  const image = ref<File | null>(null)
  const textInput = ref('')
  const result = ref<VerifyResult | null>(null)
  const tokenSummary = ref<TokenSummary | null>(null)
  const error = ref<string | null>(null)

  const stream = useStream<VerifyStreamEvent>()
  const { lines, isActive, start, appendLine, stop, reset: resetStream } = stream

  function setImage(f: File | null) {
    image.value = f
  }

  function setTextInput(text: string) {
    textInput.value = text
  }

  function toggleMode() {
    inputMode.value = inputMode.value === 'image' ? 'text' : 'image'
    image.value = null
    textInput.value = ''
  }

  function handleEvent(event: VerifyStreamEvent) {
    if (event.type === 'token') {
      const last = lines.value[lines.value.length - 1]
      if (last !== undefined && last.length > 0 && !last.endsWith('\n')) {
        lines.value[lines.value.length - 1] = last + event.data
      } else {
        appendLine(event.data)
      }
    } else if (event.type === 'result') {
      result.value = event.data
    } else if (event.type === 'done') {
      tokenSummary.value = event.data
      stop()
    }
  }

  function startStream() {
    error.value = null
    result.value = null
    tokenSummary.value = null

    const serviceCall = (onEvent: (e: VerifyStreamEvent) => void) => {
      if (inputMode.value === 'image' && image.value) {
        return submitVerifyImage(image.value, onEvent)
      }
      return submitVerifyText(textInput.value, onEvent)
    }

    start(serviceCall, handleEvent)
  }

  function cancelStream() {
    stop()
  }

  function resetAll() {
    resetStream()
    image.value = null
    textInput.value = ''
    result.value = null
    tokenSummary.value = null
    error.value = null
  }

  return {
    inputMode,
    image,
    textInput,
    result,
    tokenSummary,
    error,
    lines,
    isActive,
    setImage,
    setTextInput,
    toggleMode,
    startStream,
    cancelStream,
    resetAll,
  }
})
