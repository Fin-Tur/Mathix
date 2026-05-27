<script setup lang="ts">
import { ref, watch, nextTick } from 'vue'

const props = defineProps<{
  lines: string[]
  isActive: boolean
  fill?: boolean
}>()

const containerRef = ref<HTMLElement | null>(null)

watch(
  () => props.lines.length,
  async () => {
    await nextTick()
    if (containerRef.value) {
      containerRef.value.scrollTop = containerRef.value.scrollHeight
    }
  },
)

function lineClass(line: string): string {
  if (line.startsWith('->')) return 'text-amber-400'
  if (line.startsWith('\nSolution') || line.startsWith('Solution')) return 'text-glow-300 font-semibold'
  if (line.startsWith('Running task')) return 'text-slate-200 font-medium mt-2'
  if (line.startsWith('\nExplanation') || line.startsWith('Explanation')) return 'text-slate-400 italic'
  return 'text-glow-400'
}
</script>

<template>
  <div
    v-if="lines.length > 0 || isActive"
    class="overflow-hidden rounded-xl border border-navy-600 bg-navy-950"
    :class="fill ? 'flex flex-1 min-h-0 flex-col' : 'animate-fade-in'"
  >
    <!-- Terminal titlebar -->
    <div class="flex flex-shrink-0 items-center gap-2 border-b border-navy-600 bg-navy-900 px-4 py-2.5">
      <div class="flex gap-1.5">
        <span class="h-3 w-3 rounded-full bg-red-500/70" />
        <span class="h-3 w-3 rounded-full bg-yellow-500/70" />
        <span class="h-3 w-3 rounded-full bg-green-500/70" />
      </div>
      <span class="ml-2 font-mono text-xs text-slate-500">mathix · output</span>
      <div v-if="isActive" class="ml-auto flex items-center gap-1.5">
        <span class="h-1.5 w-1.5 animate-pulse rounded-full bg-glow-400" />
        <span class="text-xs text-glow-400">live</span>
      </div>
    </div>

    <!-- Output content -->
    <div
      ref="containerRef"
      class="p-5 font-mono text-sm leading-relaxed"
      :class="fill ? 'flex-1 min-h-0 overflow-y-auto' : 'min-h-32 max-h-[1200px] overflow-y-auto'"
    >
      <div v-for="(line, i) in lines" :key="i">
        <span :class="lineClass(line)">{{ line }}</span>
      </div>
      <span v-if="isActive" class="inline-block h-3.5 w-0.5 animate-cursor-blink bg-glow-400 align-middle" />
    </div>
  </div>
</template>
