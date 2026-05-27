export const BASE_URL = import.meta.env.VITE_API_URL ?? 'http://localhost:8000'

export interface StreamHandle {
  cancel(): void
}

type ChunkCallback<T> = (event: T) => void
type DoneCallback = () => void
type ErrorCallback = (err: Error) => void

export function createSSEStream<T>(
  url: string,
  body: FormData | string,
  onChunk: ChunkCallback<T>,
  onDone: DoneCallback,
  onError: ErrorCallback,
): StreamHandle {
  const controller = new AbortController()

  const headers: Record<string, string> = { Accept: 'text/event-stream' }
  if (typeof body === 'string') headers['Content-Type'] = 'application/json'

  fetch(url, {
    method: 'POST',
    headers,
    body,
    signal: controller.signal,
  })
    .then(async (res) => {
      if (!res.ok || !res.body) throw new Error(`HTTP ${res.status}`)

      const reader = res.body.getReader()
      const decoder = new TextDecoder()
      let buffer = ''

      while (true) {
        const { done, value } = await reader.read()
        if (done) break

        buffer += decoder.decode(value, { stream: true })
        const parts = buffer.split('\n\n')
        buffer = parts.pop() ?? ''

        for (const part of parts) {
          const line = part.trim()
          if (!line.startsWith('data:')) continue
          const raw = line.slice(5).trim()
          if (raw === '[DONE]') {
            onDone()
            return
          }
          try {
            onChunk(JSON.parse(raw) as T)
          } catch {
            // non-JSON data line, skip
          }
        }
      }
      onDone()
    })
    .catch((err: Error) => {
      if (err.name !== 'AbortError') onError(err)
    })

  return { cancel: () => controller.abort() }
}
