# Concept Guide: Embeddings & Vector Stores

## Key Concepts

1. **Embeddings capture meaning** - Similar text → similar vectors
2. **Vector stores enable fast search** - Find similar items quickly
3. **Similarity metrics matter** - Cosine is most common
4. **Metadata filtering is powerful** - Narrow search before similarity

## Visual: How Embeddings Work

```
┌─────────────────────────────────────────────────────────────┐
│                    EMBEDDING SPACE                           │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   Text                    Embedding Model           Vector   │
│                                                              │
│   "dog"        ────▶     [Neural Network]    ────▶ [0.2, 0.8, -0.3, ...]
│                                                              │
│   "puppy"      ────▶     [Neural Network]    ────▶ [0.3, 0.7, -0.2, ...]
│                                │                    ↑ Similar!
│   "cat"        ────▶     [Neural Network]    ────▶ [0.1, 0.6, 0.4, ...]
│                                │                    ↑ Less similar
│   "car"        ────▶     [Neural Network]    ────▶ [-0.5, 0.1, 0.8, ...]
│                                                     ↑ Very different
│                                                              │
│   Key insight: Semantic similarity → Vector proximity        │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Visual: Vector Store Search

```
┌─────────────────────────────────────────────────────────────┐
│                   VECTOR STORE SEARCH                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   1. INDEX TIME (once)                                       │
│      Documents → Embed → Store in Vector DB                  │
│                                                              │
│   2. QUERY TIME (every search)                               │
│                                                              │
│      Query: "How to train a dog?"                           │
│         │                                                    │
│         ▼                                                    │
│      Embed Query → [0.25, 0.75, -0.25, ...]                 │
│         │                                                    │
│         ▼                                                    │
│      Find Similar Vectors (Approximate Nearest Neighbor)    │
│         │                                                    │
│         ▼                                                    │
│      Return Top K Documents                                  │
│         • "Dog training basics" (score: 0.92)               │
│         • "Puppy obedience tips" (score: 0.88)              │
│         • "Pet care guide" (score: 0.75)                    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Code Example

```python
# Create embeddings
from langchain_openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings()

# Single text
vector = embeddings.embed_query("Hello world")
# Returns: [0.01, -0.02, 0.03, ...] (1536 dimensions)

# Multiple texts
vectors = embeddings.embed_documents(["Doc 1", "Doc 2"])

# Create vector store
from langchain_community.vectorstores import FAISS
store = FAISS.from_documents(documents, embeddings)

# Search
results = store.similarity_search("my query", k=5)

# Search with filter
results = store.similarity_search(
    "my query",
    k=5,
    filter={"category": "technical"}
)
```

## Cosine Similarity Visual

```
        Identical (cos=1.0)
             ↑
         A ←─┼
             │
             │
             ├─────▶ B    Orthogonal (cos=0.0)
             │
             │
             ▼
        Opposite (cos=-1.0)

cos(A,B) = (A · B) / (|A| × |B|)

Higher cosine = More similar meaning
```

## Teach-Back

Explain in your own words:
1. Why do similar meanings produce similar vectors?
2. What's the difference between exact search and ANN?
3. When would you use metadata filtering?
