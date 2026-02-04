# Concept Guide: Advanced RAG Techniques

## Key Concepts

1. **Reranking improves precision** - Cross-encoders are more accurate than bi-encoders
2. **Hybrid search handles edge cases** - Combines semantic + keyword matching
3. **HyDE bridges vocabulary gaps** - Generate hypothetical answer, then search
4. **Query decomposition helps complex questions** - Break into simpler parts

## Visual: Two-Stage Retrieval

```
┌─────────────────────────────────────────────────────────────┐
│               TWO-STAGE RETRIEVAL (Reranking)                │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   Query                                                      │
│     │                                                        │
│     ▼                                                        │
│   ┌─────────────────────────────────────────────────────┐   │
│   │ STAGE 1: Bi-Encoder (Fast, Less Accurate)           │   │
│   │ Retrieve top 20-50 candidates                        │   │
│   │ Uses: Embeddings + Vector Search (ANN)              │   │
│   └──────────────────────┬──────────────────────────────┘   │
│                          │ 20+ candidates                    │
│                          ▼                                   │
│   ┌─────────────────────────────────────────────────────┐   │
│   │ STAGE 2: Cross-Encoder (Slow, More Accurate)        │   │
│   │ Score each (query, doc) pair together                │   │
│   │ Rerank and keep top 5                                │   │
│   └──────────────────────┬──────────────────────────────┘   │
│                          │ Top 5                             │
│                          ▼                                   │
│                    High-quality results                      │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Visual: Hybrid Search

```
┌─────────────────────────────────────────────────────────────┐
│                     HYBRID SEARCH                            │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   Query: "Error code E-401"                                  │
│                │                                             │
│        ┌───────┴───────┐                                    │
│        ▼               ▼                                    │
│   ┌─────────┐    ┌─────────┐                               │
│   │ Vector  │    │  BM25   │                               │
│   │ Search  │    │ Search  │                               │
│   └────┬────┘    └────┬────┘                               │
│        │               │                                    │
│   Semantic         Exact term                               │
│   matches          matches                                   │
│        │               │                                    │
│        └───────┬───────┘                                    │
│                ▼                                             │
│   ┌─────────────────────┐                                   │
│   │ Reciprocal Rank     │                                   │
│   │ Fusion (RRF)        │                                   │
│   └──────────┬──────────┘                                   │
│              │                                               │
│              ▼                                               │
│   Combined results (best of both worlds)                     │
│                                                              │
│   α = 0: Pure keyword     α = 1: Pure semantic              │
│   α = 0.5: Balanced hybrid                                   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Visual: HyDE

```
┌─────────────────────────────────────────────────────────────┐
│            HyDE (Hypothetical Document Embeddings)           │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   Problem: Query vocabulary ≠ Document vocabulary           │
│                                                              │
│   User asks:  "How to fix slow computer"                    │
│   Docs say:   "Performance optimization techniques"         │
│               (Low similarity!)                              │
│                                                              │
│   HyDE Solution:                                             │
│                                                              │
│   Query ──▶ LLM generates hypothetical answer               │
│              "To fix a slow computer, try these             │
│               performance optimization techniques:           │
│               1. Clear cache..."                            │
│                     │                                        │
│                     ▼                                        │
│              Embed hypothetical                              │
│                     │                                        │
│                     ▼                                        │
│              Search for similar REAL docs                   │
│                     │                                        │
│                     ▼                                        │
│              Found: "Performance optimization guide"        │
│              (High similarity to hypothesis!)               │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Code Example

```python
# Reranking with cross-encoder
from sentence_transformers import CrossEncoder
reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

def rerank(query, docs, top_k=5):
    pairs = [(query, doc.page_content) for doc in docs]
    scores = reranker.predict(pairs)
    ranked = sorted(zip(docs, scores), key=lambda x: x[1], reverse=True)
    return [doc for doc, _ in ranked[:top_k]]

# Hybrid search
def hybrid_search(query, vector_store, bm25_index, alpha=0.5):
    vector_results = vector_store.similarity_search(query, k=10)
    bm25_results = bm25_index.search(query, k=10)
    return reciprocal_rank_fusion([vector_results, bm25_results])

# HyDE
def hyde_search(query, vector_store, llm):
    hypothesis = llm.invoke(f"Write a passage answering: {query}")
    return vector_store.similarity_search(hypothesis.content, k=5)
```

## Teach-Back

Explain in your own words:
1. Why are cross-encoders more accurate but slower?
2. When would hybrid search outperform pure semantic search?
3. How does HyDE help with vocabulary mismatch?
