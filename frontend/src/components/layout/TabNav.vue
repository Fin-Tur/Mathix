<script setup lang="ts">
import { useRoute } from 'vue-router'

const route = useRoute()
</script>

<template>
  <nav class="flex items-center gap-1 rounded-xl border border-navy-700 bg-navy-900 p-1">
    <RouterLink
      v-for="tab in [{ path: '/solve', label: 'Solve' }, { path: '/verify', label: 'Verify' }]"
      :key="tab.path"
      :to="tab.path"
      class="relative rounded-lg px-5 py-1.5 text-sm font-medium transition-all duration-200"
      :class="
        route.path === tab.path
          ? 'bg-glow-500/20 text-glow-400'
          : 'text-slate-400 hover:text-glow-300'
      "
    >
      {{ tab.label }}
      <span
        v-if="route.path === tab.path"
        class="absolute inset-x-2 -bottom-px h-px bg-gradient-to-r from-transparent via-glow-400 to-transparent"
      />
    </RouterLink>
  </nav>
</template>
