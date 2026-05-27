<script setup lang="ts">
import { ref, computed } from 'vue'
import { useSolveStore } from '../stores/solve'
import InputModeToggle from '../components/input/InputModeToggle.vue'
import DropZone from '../components/input/DropZone.vue'
import TextInputArea from '../components/input/TextInputArea.vue'
import GlowButton from '../components/action/GlowButton.vue'
import ResultOverlay from '../components/output/ResultOverlay.vue'
import StreamPanel from '../components/output/StreamPanel.vue'
import TokenBadge from '../components/output/TokenBadge.vue'
import TaskCard from '../components/output/TaskCard.vue'

const store = useSolveStore()
const overlayVisible = ref(false)

const canSubmit = computed(() => {
  if (store.inputMode === 'pdf') return store.file !== null
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
      <h1 class="text-2xl font-bold text-glow-300 text-glow">Aufgaben lösen</h1>
      <p class="mt-1.5 text-sm text-slate-400">
        Lade ein PDF hoch oder gib eine Aufgabe ein — die KI löst sie Schritt für Schritt.
      </p>
    </div>

    <div class="space-y-4">
      <InputModeToggle
        primary-label="PDF"
        secondary-label="Text"
        :is-primary="store.inputMode === 'pdf'"
        @toggle="store.toggleMode()"
      >
        <template #primary-icon>
          <svg class="h-3.5 w-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
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
        v-if="store.inputMode === 'pdf'"
        :accepted-types="['application/pdf']"
        label="PDF-Datei hochladen"
        sublabel="Aufgabenblätter, Übungszettel, Klausuren"
        icon="pdf"
        @file-selected="store.setFile($event)"
        @file-cleared="store.setFile(null)"
      />

      <TextInputArea
        v-else
        v-model="store.textInput"
        placeholder="Aufgabe eingeben, z. B.: Berechne den Grenzwert von f(x) = (x² - 4) / (x - 2) für x → 2."
        :rows="7"
      />

      <GlowButton
        label="Lösen"
        :loading="false"
        :disabled="!canSubmit"
        @click="handleSubmit"
      />
    </div>
  </div>

  <!-- Result overlay -->
  <ResultOverlay
    :show="overlayVisible"
    title="Aufgaben lösen"
    :is-active="store.isActive"
    @close="handleClose"
    @reset="handleReset"
  >
    <template #sidebar-label>Aufgaben</template>

    <template #sidebar>
      <div v-if="store.tasks.length === 0" class="flex items-center justify-center px-4 py-12">
        <p class="text-xs text-slate-600">Aufgaben werden extrahiert…</p>
      </div>
      <TaskCard
        v-for="task in store.tasks"
        :key="task.id"
        :task="task"
        :solutions="store.solutions"
      />
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
