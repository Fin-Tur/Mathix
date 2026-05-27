<script setup lang="ts">
defineProps<{ show: boolean; title: string; isActive: boolean }>()
defineEmits<{ close: []; reset: [] }>()
</script>

<template>
  <Transition
    enter-active-class="transition-all duration-450 ease-out"
    enter-from-class="opacity-0 translate-y-4"
    enter-to-class="opacity-100 translate-y-0"
    leave-active-class="transition-all duration-300 ease-in"
    leave-from-class="opacity-100 translate-y-0"
    leave-to-class="opacity-0 translate-y-4"
  >
    <div
      v-if="show"
      class="fixed inset-x-0 bottom-0 z-40 flex flex-col bg-navy-950"
      style="top: 60px"
    >
      <!-- Overlay top bar -->
      <div class="flex flex-shrink-0 items-center gap-4 border-b border-navy-700 bg-navy-900 px-6 py-3">
        <button
          class="flex items-center gap-1.5 text-sm text-slate-400 transition-colors hover:text-slate-100"
          @click="$emit('close')"
        >
          <svg class="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
          </svg>
          Zurück
        </button>

        <div class="h-4 w-px bg-navy-600" />

        <span class="text-sm font-medium text-slate-200">{{ title }}</span>

        <div v-if="isActive" class="flex items-center gap-2">
          <span class="h-1.5 w-1.5 animate-pulse rounded-full bg-glow-400" />
          <span class="text-xs text-glow-400">läuft</span>
        </div>

        <div class="ml-auto">
          <button
            class="text-xs text-slate-600 transition-colors hover:text-slate-400"
            @click="$emit('reset')"
          >
            Neu starten
          </button>
        </div>
      </div>

      <!-- Content: sidebar + output -->
      <div class="flex min-h-0 flex-1 overflow-hidden">

        <!-- Left sidebar: tasks / verify result -->
        <div class="flex w-80 flex-shrink-0 flex-col overflow-y-auto border-r border-navy-700 bg-navy-900">
          <div class="border-b border-navy-700 px-4 py-2.5">
            <p class="text-xs font-medium uppercase tracking-wider text-slate-500">
              <slot name="sidebar-label">Aufgaben</slot>
            </p>
          </div>
          <div class="flex-1 overflow-y-auto">
            <slot name="sidebar" />
          </div>
        </div>

        <!-- Right: stream output (main focus) -->
        <div class="flex min-h-0 flex-1 flex-col overflow-hidden p-6">
          <slot name="output" />
        </div>

      </div>
    </div>
  </Transition>
</template>
