<script setup lang="ts">
defineProps<{
  modelValue: string
  placeholder?: string
  rows?: number
}>()

defineEmits<{ 'update:modelValue': [string] }>()
</script>

<template>
  <div class="relative">
    <textarea
      class="w-full resize-none rounded-xl border border-navy-600 bg-navy-900 px-4 py-3 font-mono text-sm text-glow-300 placeholder-slate-600 outline-none transition-all duration-200 focus:border-glow-500/60 focus:shadow-glow-sm focus:ring-0"
      :placeholder="placeholder ?? 'Aufgabe eingeben…'"
      :rows="rows ?? 6"
      :value="modelValue"
      @input="$emit('update:modelValue', ($event.target as HTMLTextAreaElement).value)"
    />
    <div
      v-if="!modelValue"
      class="pointer-events-none absolute right-3 top-3 text-xs text-slate-700"
    >
      LaTeX / Klartext
    </div>
  </div>
</template>
