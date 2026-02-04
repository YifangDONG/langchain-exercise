# Concept Guide: Model Basics

## Key Concepts

1. **Models are APIs** - You send text, get text back
2. **Three invocation modes** - `invoke()`, `stream()`, `batch()`
3. **Parameters control behavior** - Temperature affects creativity
4. **Provider abstraction** - Same code works for OpenAI, Anthropic, etc.

## Visual: Invocation Modes

```
┌─────────────────────────────────────────────────────────────┐
│                                                              │
│  invoke()   ───▶  [Wait for complete response]  ───▶ "..."  │
│                                                              │
│  stream()   ───▶  "H" ──▶ "e" ──▶ "l" ──▶ "l" ──▶ "o"      │
│                   (tokens arrive one by one)                 │
│                                                              │
│  batch()    ───▶  [Process all at once]  ───▶ ["...", "..."]│
│             ↑                                                │
│       Multiple prompts                                       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Code Example

```python
from langchain import init_chat_model

# Initialize (works for any provider!)
model = init_chat_model("openai/gpt-4-turbo")

# invoke: Get complete response
response = model.invoke("Hello!")
print(response.content)

# stream: Get tokens as they arrive
for chunk in model.stream("Tell me a story"):
    print(chunk.content, end="")

# batch: Process multiple prompts
responses = model.batch(["Hi", "Hello", "Hey"])
```

## Temperature Visual

```
Temperature: 0.0          0.5          1.0          2.0
             │            │            │            │
             ▼            ▼            ▼            ▼
         Deterministic  Balanced   Creative    Chaotic
         Same answer    Some        Varied     Random
         every time    variation   responses   outputs
         
Use 0.0 for: Facts, code, math
Use 0.7 for: General conversation
Use 1.0+for: Creative writing, brainstorming
```

## Teach-Back

Explain in your own words:
1. When would you use `stream()` instead of `invoke()`?
2. What does temperature=0 mean practically?
3. Why use `init_chat_model()` instead of `ChatOpenAI()`?
