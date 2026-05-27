<template>
  <span class="inline-flex items-center gap-1">
    <span
      v-for="i in 3"
      :key="i"
      class="h-1.5 w-1.5 rounded-full bg-glow-400"
      :style="{ animationDelay: `${(i - 1) * 0.2}s` }"
      :class="'animate-bounce'"
    />
  </span>
</template>
