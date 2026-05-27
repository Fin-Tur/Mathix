<script setup lang="ts">
import { ref, computed } from 'vue'
import { useFileUpload } from '../../composables/useFileUpload'
import FilePreview from './FilePreview.vue'

const props = defineProps<{
  acceptedTypes: string[]
  label: string
  sublabel?: string
  icon?: string
}>()

const emit = defineEmits<{ 'file-selected': [File]; 'file-cleared': [] }>()

const { file, isDragOver, onDrop, onDragOver, onDragLeave, onFileInput, clearFile } =
  useFileUpload(props.acceptedTypes)

function handleClear() {
  clearFile()
  emit('file-cleared')
}

function handleDrop(e: DragEvent) {
  onDrop(e)
  if (file.value) emit('file-selected', file.value)
}

function handleFileInput(e: Event) {
  onFileInput(e)
  if (file.value) emit('file-selected', file.value)
}

const inputEl = ref<HTMLInputElement | null>(null)

function openFilePicker() {
  if (!file.value) inputEl.value?.click()
}

const borderClass = computed(() =>
  isDragOver.value
    ? 'border-glow-400 bg-navy-800 shadow-glow-sm'
    : 'border-navy-600 hover:border-glow-500/60 hover:bg-navy-900/50',
)
</script>

<template>
  <div>
    <div
      v-if="!file"
      class="relative flex cursor-pointer flex-col items-center justify-center gap-3 rounded-xl border-2 border-dashed p-10 transition-all duration-200"
      :class="borderClass"
      @drop="handleDrop"
      @dragover="onDragOver"
      @dragleave="onDragLeave"
      @click="openFilePicker"
    >
      <input
        ref="inputEl"
        type="file"
        class="sr-only"
        :accept="acceptedTypes.join(',')"
        @change="handleFileInput"
      />

      <div
        class="flex h-14 w-14 items-center justify-center rounded-2xl border border-glow-500/25 bg-glow-500/10"
      >
        <svg
          v-if="!icon || icon === 'pdf'"
          class="h-7 w-7 text-glow-400"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="1.5"
            d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m2.25 0H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z"
          />
        </svg>
        <svg
          v-else
          class="h-7 w-7 text-glow-400"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="1.5"
            d="M2.25 15.75l5.159-5.159a2.25 2.25 0 013.182 0l5.159 5.159m-1.5-1.5l1.409-1.409a2.25 2.25 0 013.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 001.5-1.5V6a1.5 1.5 0 00-1.5-1.5H3.75A1.5 1.5 0 002.25 6v12a1.5 1.5 0 001.5 1.5zm10.5-11.25h.008v.008h-.008V8.25zm.375 0a.375.375 0 11-.75 0 .375.375 0 01.75 0z"
          />
        </svg>
      </div>

      <div class="text-center">
        <p class="text-sm font-medium text-glow-400">{{ label }}</p>
        <p v-if="sublabel" class="mt-1 text-xs text-slate-400">{{ sublabel }}</p>
        <p class="mt-2 text-xs text-slate-500">
          {{ acceptedTypes.join(', ').toUpperCase() }} · Klicken oder Drag & Drop
        </p>
      </div>
    </div>

    <FilePreview v-else :file="file" @clear="handleClear" />
  </div>
</template>
