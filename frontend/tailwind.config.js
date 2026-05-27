/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,ts}'],
  theme: {
    extend: {
      colors: {
        navy: {
          950: '#0a0f1e',
          900: '#0d1326',
          800: '#111827',
          700: '#1a2235',
          600: '#243047',
        },
        glow: {
          300: '#93c5fd',
          400: '#60a5fa',
          500: '#3b82f6',
          600: '#2563eb',
        },
      },
      fontFamily: {
        mono: ['"JetBrains Mono"', '"Fira Code"', 'monospace'],
        sans: ['Inter', 'system-ui', 'sans-serif'],
      },
      boxShadow: {
        'glow-sm':       '0 0 6px 0px rgba(96,165,250,0.12)',
        'glow-md':       '0 0 10px 1px rgba(96,165,250,0.18)',
        'glow-lg':       '0 0 16px 2px rgba(96,165,250,0.14)',
        'glow-btn':      '0 0 8px 1px rgba(96,165,250,0.20)',
        'glow-btn-hover':'0 0 12px 2px rgba(96,165,250,0.28)',
      },
      animation: {
        'cursor-blink': 'cursorBlink 1s step-end infinite',
        'fade-in':      'fadeIn 0.3s ease-out',
        'slide-up':     'slideUp 0.4s ease-out',
      },
      keyframes: {
        cursorBlink: {
          '0%, 100%': { opacity: '1' },
          '50%':      { opacity: '0' },
        },
        fadeIn: {
          from: { opacity: '0', transform: 'translateY(4px)' },
          to:   { opacity: '1', transform: 'translateY(0)' },
        },
        slideUp: {
          from: { opacity: '0', transform: 'translateY(12px)' },
          to:   { opacity: '1', transform: 'translateY(0)' },
        },
      },
    },
  },
  plugins: [],
}
