<script setup lang="ts">
defineProps<{ file: File }>()
defineEmits<{ clear: [] }>()

function formatSize(bytes: number): string {
  if (bytes < 1024) return `${bytes} B`
  if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`
  return `${(bytes / (1024 * 1024)).toFixed(1)} MB`
}
</script>

<template>
  <div class="flex items-center gap-3 rounded-lg border border-glow-500/30 bg-navy-800 px-4 py-3 animate-fade-in">
    <div class="flex h-9 w-9 flex-shrink-0 items-center justify-center rounded-lg bg-glow-500/20">
      <svg class="h-5 w-5 text-glow-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
          d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
      </svg>
    </div>
    <div class="min-w-0 flex-1">
      <p class="truncate text-sm font-medium text-glow-300">{{ file.name }}</p>
      <p class="text-xs text-slate-500">{{ formatSize(file.size) }}</p>
    </div>
    <button
      class="flex-shrink-0 rounded-md p-1.5 text-slate-500 transition-colors hover:bg-navy-700 hover:text-slate-300"
      @click="$emit('clear')"
    >
      <svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
      </svg>
    </button>
  </div>
</template>
