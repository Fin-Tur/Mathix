<script setup lang="ts">
defineProps<{
  label: string
  loading?: boolean
  disabled?: boolean
  variant?: 'primary' | 'secondary'
}>()

defineEmits<{ click: [] }>()
</script>

<template>
  <button
    :disabled="loading || disabled"
    class="relative inline-flex items-center justify-center gap-2 rounded-xl px-8 py-3 font-semibold transition-all duration-200 disabled:cursor-not-allowed disabled:opacity-50"
    :class="
      variant === 'secondary'
        ? 'border border-glow-500/40 bg-navy-800 text-glow-400 hover:bg-navy-700'
        : 'bg-glow-500 text-white shadow-glow-btn hover:bg-glow-400 hover:shadow-glow-btn-hover active:scale-95'
    "
    @click="$emit('click')"
  >
    <svg
      v-if="loading"
      class="h-4 w-4 animate-spin"
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      viewBox="0 0 24 24"
    >
      <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />
      <path
        class="opacity-75"
        fill="currentColor"
        d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"
      />
    </svg>
    {{ loading ? 'Verarbeite…' : label }}
  </button>
</template>
