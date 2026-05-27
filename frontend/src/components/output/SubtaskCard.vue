<script setup lang="ts">
import { ref } from 'vue'
import type { SubTask, Solution } from '../../types/solve'

defineProps<{
  subtask: SubTask
  solution?: Solution
}>()

const showExplanation = ref(false)
</script>

<template>
  <div
    class="rounded-lg border bg-navy-950 px-4 py-3 transition-all duration-300"
    :class="solution ? 'border-glow-500/20' : 'border-navy-700'"
  >
    <div class="flex items-start gap-3">
      <div
        class="mt-0.5 flex h-5 w-5 flex-shrink-0 items-center justify-center rounded-full text-xs font-bold transition-all duration-300"
        :class="
          solution
            ? 'bg-glow-500/20 text-glow-400'
            : 'bg-navy-700 text-slate-500'
        "
      >
        <svg v-if="solution" class="h-3 w-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" />
        </svg>
        <span v-else class="text-[10px]">{{ subtask.id }}</span>
      </div>

      <div class="min-w-0 flex-1">
        <p class="text-sm text-slate-200">{{ subtask.description }}</p>

        <div v-if="solution" class="mt-3 animate-slide-up space-y-2">
          <div class="rounded-lg border border-glow-500/20 bg-navy-900 px-3 py-2">
            <p class="text-xs text-slate-400">Ergebnis</p>
            <p class="font-mono text-sm font-semibold text-glow-300">{{ solution.result }}</p>
          </div>

          <button
            class="flex items-center gap-1 text-xs text-slate-400 transition-colors hover:text-glow-400"
            @click="showExplanation = !showExplanation"
          >
            <svg
              class="h-3.5 w-3.5 transition-transform duration-200"
              :class="showExplanation ? 'rotate-90' : ''"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
            </svg>
            {{ showExplanation ? 'Erklärung verbergen' : 'Erklärung anzeigen' }}
          </button>

          <div
            v-if="showExplanation"
            class="rounded-lg bg-navy-800 px-3 py-2 text-xs leading-relaxed text-slate-300 animate-fade-in"
          >
            {{ solution.explanation }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
