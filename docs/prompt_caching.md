# Prompt Caching — Analysis & Recommendations

## Current State: No Caching

The project currently uses **zero prompt caching**. No `cache_control` field appears anywhere — not on tool definitions, the system prompt, or message history.

---

## What Can Be Cached

The Anthropic API offers two mechanisms:

| Method | How | Best for |
|---|---|---|
| **Automatic** | `cache_control={"type": "ephemeral"}` at request top level | Growing multi-turn conversations |
| **Explicit breakpoints** | `cache_control` directly on a content block | Specific static blocks (tools, system) |

Up to **4 explicit breakpoints** per request. Both methods can be combined.

**Minimum token threshold for `claude-haiku-4-5`:** 4,096 tokens per cached block.

---

## Recommended Caching for This Project

### 1. Tool Definitions — Explicit Breakpoint (Highest Priority)

**Location:** `src/models/tools.py`, last entry of `TOOLS`

The 46 tool definitions are static and re-sent on every API call inside the `run_task()` while-loop.
With `claude-haiku-4-5`, tool tokens cost $1/MTok uncached vs. $0.10/MTok cached — **90% savings on tool tokens per tool-use loop iteration.**

The full TOOLS list is well above the 4,096-token threshold (~10,000–15,000 tokens estimated).

```python
# In TOOLS list, add cache_control to the LAST entry only:
{
    "name": "solve_matrix_equation",
    "description": "...",
    "input_schema": { ... },
    "cache_control": {"type": "ephemeral"},   # ← add this
},
```

The breakpoint on the *last* tool covers the entire tools array as a prefix.

---

### 2. System Prompt — Explicit Breakpoint (High Priority)

**Location:** `src/main.py`, `run_task()` → `client.messages.parse(..., system=...)`

The system string is identical on every call. Pass it as an array with `cache_control`:

```python
system=[{
    "type": "text",
    "text": "You are a brilliant mathematician and problem solver. ...",
    "cache_control": {"type": "ephemeral"},
}],
```

Note: The system prompt alone (~20 tokens) is far below the 4,096-token threshold.
It will only be cached as part of a combined prefix that includes the tool definitions.
When tools are cached with an explicit breakpoint and the system prompt block precedes them,
the two are combined and the threshold is easily met.

---

### 3. Multi-Turn Message History — Automatic Caching (High Priority)

**Location:** `src/main.py`, `run_task()` → `client.messages.parse(...)`

The while-loop in `run_task()` extends `messages` with each tool-use round.
Automatic caching handles this transparently:

```python
response = client.messages.parse(
    model="claude-haiku-4-5",
    max_tokens=1024,
    cache_control={"type": "ephemeral"},   # ← top-level automatic caching
    system=[{
        "type": "text",
        "text": "You are a brilliant mathematician and problem solver. ...",
        "cache_control": {"type": "ephemeral"},
    }],
    tools=TOOLS,
    output_format=Solution,
    messages=messages,
)
```

On each loop iteration the API automatically caches up to the last stable message block.
The next iteration reads all previous messages from cache instead of re-sending them.

---

### 4. PDF Extraction Instruction — Low Priority

**Location:** `src/models/task.py`, `extract_tasks_from_pdf()`

`_EXTRACT_INSTRUCTION` is static but `extract_tasks_from_pdf()` is called once per PDF (one-shot).
No repeated calls → no cache hits. Only worth adding if multiple PDFs are processed per session.

If needed:
```python
content = [
    {"type": "text", "text": _EXTRACT_INSTRUCTION, "cache_control": {"type": "ephemeral"}},
    {"type": "text", "text": pdf_text},
]
```

---

## Combined Implementation for `run_task()`

```python
def run_task(task: Task) -> Solution:
    messages = [{"role": "user", "content": f"{task.description}\nParameters: {task.parameters}"}]

    while True:
        response = client.messages.parse(
            model="claude-haiku-4-5",
            max_tokens=1024,
            # NOTE: top-level cache_control is NOT supported by messages.parse().
            # Automatic multi-turn caching only works with messages.create().
            # Explicit breakpoints on system + last tool still apply.
            system=[{
                "type": "text",
                "text": "You are a brilliant mathematician and problem solver. "
                        "You will be given mathematical problems per text or via pdf "
                        "and you will solve them using the tools at your disposal.",
                "cache_control": {"type": "ephemeral"}, # explicit system cache
            }],
            tools=TOOLS,                                # last tool has cache_control
            output_format=Solution,
            messages=messages,
        )
        # ... rest unchanged
```

---

## How to Verify Cache Hits

Add usage logging after each API call:

```python
u = response.usage
print(f"[cache] write={u.cache_creation_input_tokens}  "
      f"read={u.cache_read_input_tokens}  "
      f"uncached={u.input_tokens}")
```

| Field | Meaning |
|---|---|
| `cache_creation_input_tokens` | Tokens written to cache (first call, or after TTL expired) |
| `cache_read_input_tokens` | Tokens served from cache (hit) |
| `input_tokens` | Tokens processed normally (not cached) |

**Expected pattern for `run_task()` with a 3-step tool loop:**

| Iteration | cache_creation | cache_read | Meaning |
|---|---|---|---|
| 1st API call | > 0 | 0 | Tools + system written to cache |
| 2nd (tool result) | small | large | Previous messages read from cache |
| 3rd (tool result) | small | larger | Even more read from cache |

A `cache_read_input_tokens` value of `0` after the first call means the cache is not being hit — check that the content reaching the 4,096-token minimum threshold.

---

## Summary

| What | Method | Priority | Estimated Savings |
|---|---|---|---|
| Tool definitions (46 tools) | Explicit breakpoint on last tool | **Critical** | ~90% on tool tokens per iteration |
| System prompt | Explicit breakpoint | **High** | Marginal alone, combined with tools |
| Message history in while-loop | Automatic (top-level) | **High** | Grows with each tool-use round |
| PDF extraction instruction | Explicit on text block | Low | Only if multiple PDFs per session |

**TTL:** Default 5 minutes. Since `run_task()` completes within seconds to a few minutes, the default TTL is sufficient. No need for the 1-hour option.
