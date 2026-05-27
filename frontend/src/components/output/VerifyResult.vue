<script setup lang="ts">
import type { VerifyResult } from '../../types/verify'
import LoadingDots from '../shared/LoadingDots.vue'

defineProps<{
  result: VerifyResult | null
  isStreaming: boolean
}>()
</script>

<template>
  <div v-if="isStreaming && !result" class="flex items-center gap-3 text-sm text-slate-400">
    <LoadingDots />
    <span>Überprüfe…</span>
  </div>

  <div v-else-if="result" class="animate-slide-up space-y-4">
    <div
      class="flex items-start gap-4 rounded-xl border px-5 py-4"
      :class="
        result.valid
          ? 'border-green-500/30 bg-green-900/10'
          : 'border-red-500/30 bg-red-900/10'
      "
    >
      <div
        class="flex h-10 w-10 flex-shrink-0 items-center justify-center rounded-full"
        :class="result.valid ? 'bg-green-500/20' : 'bg-red-500/20'"
      >
        <svg
          v-if="result.valid"
          class="h-5 w-5 text-green-400"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7" />
        </svg>
        <svg
          v-else
          class="h-5 w-5 text-red-400"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </div>

      <div class="flex-1">
        <p
          class="font-semibold"
          :class="result.valid ? 'text-green-400' : 'text-red-400'"
        >
          {{ result.valid ? 'Korrekt' : 'Fehlerhaft' }}
        </p>
        <p class="mt-1 text-sm text-slate-300">{{ result.explanation }}</p>
      </div>
    </div>

    <div v-if="result.steps?.length" class="space-y-2">
      <p class="text-xs font-medium uppercase tracking-wide text-slate-600">Schritte</p>
      <div
        v-for="(step, i) in result.steps"
        :key="i"
        class="flex items-center gap-3 rounded-lg border px-4 py-2.5"
        :class="
          step.valid
            ? 'border-green-500/20 bg-green-900/5'
            : 'border-red-500/20 bg-red-900/5'
        "
      >
        <svg
          v-if="step.valid"
          class="h-4 w-4 flex-shrink-0 text-green-400"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7" />
        </svg>
        <svg
          v-else
          class="h-4 w-4 flex-shrink-0 text-red-400"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M6 18L18 6M6 6l12 12" />
        </svg>
        <span class="text-sm text-slate-300">{{ step.description }}</span>
      </div>
    </div>
  </div>
</template>
