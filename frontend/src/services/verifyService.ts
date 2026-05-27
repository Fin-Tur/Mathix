import type { StreamHandle } from './api'
import type { VerifyStreamEvent, VerifyResult, TokenSummary } from '../types/verify'

type EventCallback = (event: VerifyStreamEvent) => void

const delay = (ms: number) => new Promise<void>((r) => setTimeout(r, ms))

async function runMockVerify(input: string, onEvent: EventCallback, signal: { cancelled: boolean }) {
  await delay(400)
  if (signal.cancelled) return

  const isValid = !input.toLowerCase().includes('falsch') && !input.toLowerCase().includes('wrong')

  const reasoning = isValid
    ? 'Analysiere die Berechnung Schritt für Schritt... Überprüfe linke Seite... Überprüfe rechte Seite... Vereinfache den Ausdruck... Das Ergebnis stimmt überein. Die Rechnung ist korrekt.'
    : 'Analysiere die Berechnung Schritt für Schritt... Überprüfe linke Seite... Überprüfe rechte Seite... Diskrepanz gefunden! Das Ergebnis stimmt nicht überein. Die Rechnung enthält einen Fehler.'

  const words = reasoning.split(' ')
  for (const word of words) {
    onEvent({ type: 'token', data: word + ' ' })
    await delay(40)
    if (signal.cancelled) return
  }

  const result: VerifyResult = {
    valid: isValid,
    explanation: isValid
      ? 'Die Rechnung ist mathematisch korrekt. Alle Schritte sind nachvollziehbar und das Ergebnis stimmt überein.'
      : 'Die Rechnung enthält einen Fehler. Die Gleichheit der Ausdrücke konnte nicht bestätigt werden.',
    steps: [
      { description: 'Linke Seite ausgewertet', valid: true },
      { description: 'Rechte Seite ausgewertet', valid: true },
      { description: 'Gleichheit geprüft', valid: isValid },
    ],
  }

  onEvent({ type: 'result', data: result })
  await delay(200)

  const summary: TokenSummary = {
    t_in: 1240,
    t_out: 380,
    t_c_read: 900,
    t_c_write: 128,
    cost_usd: 0.001842,
  }
  onEvent({ type: 'done', data: summary })
}

export function submitVerifyText(text: string, onEvent: EventCallback): StreamHandle {
  const signal = { cancelled: false }
  runMockVerify(text, onEvent, signal)
  return { cancel: () => { signal.cancelled = true } }
}

export function submitVerifyImage(file: File, onEvent: EventCallback): StreamHandle {
  const signal = { cancelled: false }
  runMockVerify(`[Bild: ${file.name}]`, onEvent, signal)
  return { cancel: () => { signal.cancelled = true } }
}
