import { ref } from 'vue'

export function useFileUpload(acceptedTypes: string[]) {
  const file = ref<File | null>(null)
  const isDragOver = ref(false)

  function isAccepted(f: File): boolean {
    return acceptedTypes.some((t) => {
      if (t.endsWith('/*')) return f.type.startsWith(t.slice(0, -1))
      return f.type === t
    })
  }

  function setFile(f: File) {
    if (isAccepted(f)) file.value = f
  }

  function onDrop(e: DragEvent) {
    e.preventDefault()
    isDragOver.value = false
    const dropped = Array.from(e.dataTransfer?.files ?? [])[0]
    if (dropped) setFile(dropped)
  }

  function onDragOver(e: DragEvent) {
    e.preventDefault()
    isDragOver.value = true
  }

  function onDragLeave() {
    isDragOver.value = false
  }

  function onFileInput(e: Event) {
    const input = e.target as HTMLInputElement
    const selected = input.files?.[0]
    if (selected) setFile(selected)
  }

  function clearFile() {
    file.value = null
  }

  return { file, isDragOver, onDrop, onDragOver, onDragLeave, onFileInput, clearFile }
}
