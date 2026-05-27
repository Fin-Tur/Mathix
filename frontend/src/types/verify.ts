import type { TokenSummary } from './solve'

export type { TokenSummary }

export interface VerifyStep {
  description: string
  valid: boolean
}

export interface VerifyResult {
  valid: boolean
  explanation: string
  steps?: VerifyStep[]
}

export type VerifyStreamEvent =
  | { type: 'token'; data: string }
  | { type: 'result'; data: VerifyResult }
  | { type: 'done'; data: TokenSummary }
