<script setup lang="ts">
import { ref, computed } from 'vue'
import { useVerifyStore } from '../stores/verify'
import InputModeToggle from '../components/input/InputModeToggle.vue'
import DropZone from '../components/input/DropZone.vue'
import TextInputArea from '../components/input/TextInputArea.vue'
import GlowButton from '../components/action/GlowButton.vue'
import ResultOverlay from '../components/output/ResultOverlay.vue'
import StreamPanel from '../components/output/StreamPanel.vue'
import TokenBadge from '../components/output/TokenBadge.vue'
import VerifyResult from '../components/output/VerifyResult.vue'

const store = useVerifyStore()
const overlayVisible = ref(false)

const canSubmit = computed(() => {
  if (store.inputMode === 'image') return store.image !== null
  return store.textInput.trim().length > 0
})

function handleSubmit() {
  overlayVisible.value = true
  store.startStream()
}

function handleClose() {
  overlayVisible.value = false
  store.cancelStream()
}

function handleReset() {
  store.resetAll()
  overlayVisible.value = false
}
</script>

<template>
  <div class="mx-auto max-w-2xl px-6 pb-12 pt-24">
    <div class="mb-8">
      <h1 class="text-2xl font-bold text-glow-300 text-glow">Rechnungen überprüfen</h1>
      <p class="mt-1.5 text-sm text-slate-400">
        Lade ein Bild einer Rechnung hoch oder gib sie als Text ein — die KI prüft die Korrektheit.
      </p>
    </div>

    <div class="space-y-4">
      <InputModeToggle
        primary-label="Bild"
        secondary-label="Text"
        :is-primary="store.inputMode === 'image'"
        @toggle="store.toggleMode()"
      >
        <template #primary-icon>
          <svg class="h-3.5 w-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
          </svg>
        </template>
        <template #secondary-icon>
          <svg class="h-3.5 w-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
          </svg>
        </template>
      </InputModeToggle>

      <DropZone
        v-if="store.inputMode === 'image'"
        :accepted-types="['image/png', 'image/jpeg', 'image/webp', 'image/*']"
        label="Bild hochladen"
        sublabel="Foto der Rechnung, Screenshot, gescannte Seite"
        icon="image"
        @file-selected="store.setImage($event)"
        @file-cleared="store.setImage(null)"
      />

      <TextInputArea
        v-else
        v-model="store.textInput"
        placeholder="Rechnung oder Beweis eingeben, z. B.: Ist ∑_{k=1}^{n} k = n(n+1)/2 korrekt?"
        :rows="7"
      />

      <GlowButton
        label="Überprüfen"
        :loading="false"
        :disabled="!canSubmit"
        @click="handleSubmit"
      />
    </div>
  </div>

  <!-- Result overlay -->
  <ResultOverlay
    :show="overlayVisible"
    title="Überprüfung"
    :is-active="store.isActive"
    @close="handleClose"
    @reset="handleReset"
  >
    <template #sidebar-label>Ergebnis</template>

    <template #sidebar>
      <div class="p-4">
        <VerifyResult :result="store.result" :is-streaming="store.isActive" />
      </div>
    </template>

    <template #output>
      <StreamPanel
        :lines="store.lines"
        :is-active="store.isActive"
        :fill="true"
      />
      <TokenBadge v-if="store.tokenSummary" class="mt-4 flex-shrink-0" :summary="store.tokenSummary" />
    </template>
  </ResultOverlay>
</template>
