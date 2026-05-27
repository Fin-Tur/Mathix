<script setup lang="ts">
import { ref } from 'vue'
import type { TokenSummary } from '../../types/solve'

defineProps<{ summary: TokenSummary }>()

const expanded = ref(false)

function fmt(n: number): string {
  return n.toLocaleString('de-DE')
}
</script>

<template>
  <div class="animate-fade-in rounded-xl border border-glow-500/20 bg-navy-900 px-4 py-3">
    <button
      class="flex w-full items-center justify-between gap-4"
      @click="expanded = !expanded"
    >
      <div class="flex items-center gap-2">
        <div class="h-2 w-2 rounded-full bg-glow-400" />
        <span class="text-sm font-medium text-slate-400">Kosten</span>
      </div>
      <div class="flex items-center gap-3">
        <span class="font-mono text-sm font-semibold text-glow-400">
          ${{ summary.cost_usd.toFixed(6) }}
        </span>
        <svg
          class="h-4 w-4 text-slate-600 transition-transform duration-200"
          :class="expanded ? 'rotate-180' : ''"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
        </svg>
      </div>
    </button>

    <div v-if="expanded" class="mt-3 grid grid-cols-2 gap-2 border-t border-navy-700 pt-3 sm:grid-cols-4">
      <div v-for="[label, val] in [['Input', summary.t_in], ['Output', summary.t_out], ['Cache Read', summary.t_c_read], ['Cache Write', summary.t_c_write]]" :key="label" class="rounded-lg bg-navy-800 px-3 py-2 text-center">
        <p class="text-xs text-slate-500">{{ label }}</p>
        <p class="font-mono text-sm font-medium text-glow-300">{{ fmt(val as number) }}</p>
      </div>
    </div>
  </div>
</template>
