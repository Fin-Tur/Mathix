<script setup lang="ts">
defineProps<{
  primaryLabel: string
  secondaryLabel: string
  isPrimary: boolean
}>()

defineEmits<{ toggle: [] }>()
</script>

<template>
  <div class="inline-flex rounded-lg border border-navy-600 bg-navy-900 p-1">
    <button
      class="flex items-center gap-2 rounded-md px-4 py-1.5 text-sm font-medium transition-all duration-200"
      :class="
        isPrimary
          ? 'bg-glow-500/20 text-glow-400 shadow-none'
          : 'text-slate-400 hover:text-glow-300'
      "
      @click="isPrimary ? null : $emit('toggle')"
    >
      <slot name="primary-icon" />
      {{ primaryLabel }}
    </button>
    <button
      class="flex items-center gap-2 rounded-md px-4 py-1.5 text-sm font-medium transition-all duration-200"
      :class="
        !isPrimary
          ? 'bg-glow-500/20 text-glow-400 shadow-none'
          : 'text-slate-400 hover:text-glow-300'
      "
      @click="!isPrimary ? null : $emit('toggle')"
    >
      <slot name="secondary-icon" />
      {{ secondaryLabel }}
    </button>
  </div>
</template>
