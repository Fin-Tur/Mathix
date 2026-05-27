<script setup lang="ts">
import TabNav from './TabNav.vue'
</script>

<template>
  <header
    class="fixed inset-x-0 top-0 z-50 border-b border-navy-700/80 bg-navy-950/80 backdrop-blur-md"
  >
    <div class="mx-auto flex max-w-7xl items-center justify-between gap-6 px-6 py-3">
      <RouterLink to="/solve" class="flex items-center gap-3">
        <div
          class="flex h-9 w-9 items-center justify-center rounded-xl border border-glow-500/20 bg-glow-500/10 transition-colors duration-200 hover:bg-glow-500/15"
        >
          <svg
            class="h-5 w-5 text-glow-400"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="1.8"
              d="M4.5 6.375a4.125 4.125 0 118.25 0 4.125 4.125 0 01-8.25 0zM14.25 8.625a3.375 3.375 0 116.75 0 3.375 3.375 0 01-6.75 0zM1.5 19.125a7.125 7.125 0 0114.25 0v.003l-.001.119a.75.75 0 01-.363.63 13.067 13.067 0 01-6.761 1.873c-2.472 0-4.786-.684-6.76-1.873a.75.75 0 01-.364-.63l-.001-.122zM17.25 19.128l-.001.144a2.25 2.25 0 01-.233.96 10.088 10.088 0 005.06-1.01.75.75 0 00.42-.643 4.875 4.875 0 00-6.957-4.611 8.586 8.586 0 011.71 5.157v.003z"
            />
          </svg>
        </div>
        <span class="text-xl font-bold tracking-tight text-glow-300 text-glow">Mathix</span>
      </RouterLink>

      <TabNav />

      <div class="w-24 text-right">
        <span class="rounded-md border border-navy-700 bg-navy-800 px-2 py-0.5 text-xs text-slate-600 font-mono">
          v0.1.0
        </span>
      </div>
    </div>
  </header>
</template>
