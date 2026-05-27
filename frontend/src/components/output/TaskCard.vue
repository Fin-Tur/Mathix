<script setup lang="ts">
import { ref } from 'vue'
import type { Task, Solution } from '../../types/solve'
import SubtaskCard from './SubtaskCard.vue'

const props = defineProps<{
  task: Task
  solutions: Record<number, Solution>
}>()

const expanded = ref(true)

const categoryColors: Record<string, string> = {
  limits:             'bg-purple-500/15 text-purple-300',
  calculus:           'bg-blue-500/15 text-blue-300',
  series:             'bg-indigo-500/15 text-indigo-300',
  la_vectors:         'bg-cyan-500/15 text-cyan-300',
  la_matrices:        'bg-teal-500/15 text-teal-300',
  multivar:           'bg-emerald-500/15 text-emerald-300',
  multivar_integrals: 'bg-green-500/15 text-green-300',
  vector_analysis:    'bg-lime-500/15 text-lime-300',
  ode:                'bg-orange-500/15 text-orange-300',
  proof:              'bg-red-500/15 text-red-300',
}

function solvedCount() {
  return props.task.subtasks.filter((s) => props.solutions[s.id]).length
}
</script>

<template>
  <div class="border-b border-navy-700 last:border-b-0">
    <!-- Task header — always visible, click to toggle -->
    <button
      class="flex w-full items-start gap-3 px-4 py-3 text-left transition-colors hover:bg-navy-800/50"
      @click="expanded = !expanded"
    >
      <div
        class="mt-0.5 flex h-5 w-5 flex-shrink-0 items-center justify-center rounded bg-navy-700 font-mono text-[10px] font-bold text-slate-400"
      >
        {{ task.id }}
      </div>
      <div class="min-w-0 flex-1">
        <p class="line-clamp-2 text-xs leading-relaxed text-slate-200">
          {{ task.description }}
        </p>
        <p class="mt-1 text-[10px] text-slate-600">
          {{ solvedCount() }} / {{ task.subtasks.length }} gelöst
        </p>
      </div>
      <svg
        class="mt-0.5 h-3.5 w-3.5 flex-shrink-0 text-slate-600 transition-transform duration-200"
        :class="expanded ? 'rotate-180' : ''"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
      >
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
      </svg>
    </button>

    <!-- Task body — collapsible -->
    <Transition
      enter-active-class="transition-all duration-300 ease-out"
      enter-from-class="opacity-0 -translate-y-1"
      enter-to-class="opacity-100 translate-y-0"
      leave-active-class="transition-all duration-200 ease-in"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div v-if="expanded" class="px-3 pb-3">
        <!-- Category badges -->
        <div class="mb-3 flex flex-wrap gap-1 px-1">
          <span
            v-for="cat in task.categories"
            :key="cat"
            class="inline-flex rounded px-1.5 py-0.5 text-[10px] font-medium"
            :class="categoryColors[cat] ?? 'bg-slate-500/15 text-slate-300'"
          >
            {{ cat.replace(/_/g, ' ') }}
          </span>
        </div>

        <!-- Subtask list -->
        <div class="space-y-2">
          <SubtaskCard
            v-for="subtask in task.subtasks"
            :key="subtask.id"
            :subtask="subtask"
            :solution="solutions[subtask.id]"
          />
        </div>
      </div>
    </Transition>
  </div>
</template>
