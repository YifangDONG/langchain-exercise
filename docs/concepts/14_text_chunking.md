# Concept Guide: Text Chunking

## Key Concepts

1. **Chunk size vs quality** - Too small = missing context; too large = noise in retrieval
2. **Overlap preserves context** - Overlap characters so ideas aren't split at boundaries
3. **Token-aware chunking** - Respect LLM token limits when chunks are used in prompts
4. **Semantic chunking** - Split on meaning (e.g. paragraphs, sections) for coherent units
5. **Metadata propagation** - Carry source, page, and chunk index through the pipeline

## Visual: Chunking Strategies

```
┌─────────────────────────────────────────────────────────────┐
│                 CHUNKING STRATEGIES                          │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   Character    │████████│████████│████████│  (fixed size)   │
│   Separator    │  ¶  │  ¶  │  ¶  │  (split on \n\n, \n, .)  │
│   Recursive    │  §  │  ¶  │  .  │  (try separators in order)│
│   Token        │ ~256 tokens │ ~256 │  (LLM-aware size)     │
│   Semantic     │ paragraph │ paragraph │  (meaning boundaries)│
│                                                              │
│   Overlap:  │████████│██│████████│  (shared chars between)   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Code Example

```python
# Simple fixed-size chunks with overlap
def chunk_by_character(document, chunk_size=1000, chunk_overlap=200):
    # Split text into chunk_size chars, slide by (chunk_size - overlap)
    # Preserve metadata, add chunk index
    ...

# Structure-aware: split on separators (e.g. \n\n, \n, ". ")
def chunk_by_separator(document, separators=["\n\n", "\n", ". "], ...):
    ...

# Token-aware: measure by tokenizer, not characters
def chunk_by_tokens(document, max_tokens=256, ...):
    ...
```

## Tradeoffs

| Strategy     | Pros                    | Cons                 |
|-------------|-------------------------|----------------------|
| Character   | Simple, fast            | Can split mid-sentence |
| Separator   | Respects structure      | Depends on separators present |
| Recursive   | Adapts to document      | More complex         |
| Token       | Fits model context      | Needs tokenizer      |
| Semantic    | Coherent units          | Slower, model-based  |

## Teach-Back

Explain in your own words:
1. Why use overlap between chunks?
2. When would you choose token-based chunking over character-based?
3. How does chunking affect RAG retrieval quality?
