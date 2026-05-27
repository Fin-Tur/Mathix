import { ref, computed } from 'vue'

export function useInputMode<T extends string>(primary: T, secondary: T) {
  const mode = ref<T>(primary)

  const isPrimary = computed(() => mode.value === primary)

  function toggle() {
    mode.value = mode.value === primary ? secondary : primary
  }

  function setMode(m: T) {
    mode.value = m
  }

  return { mode, isPrimary, toggle, setMode }
}
