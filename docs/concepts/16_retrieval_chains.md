# Concept Guide: Retrieval Chains

## Key Concepts

1. **RAG = Retrieve + Generate** - Find relevant context, then answer
2. **Different patterns for different needs** - Basic, conversational, multi-query
3. **Context formatting matters** - How you present docs affects answers
4. **Citations build trust** - Users can verify your answers

## Visual: The RAG Flow

```
┌─────────────────────────────────────────────────────────────┐
│                      THE RAG FLOW                            │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   User Question                                              │
│        │                                                     │
│        ▼                                                     │
│   ┌─────────────┐                                           │
│   │  RETRIEVE   │ ◄── Find relevant documents               │
│   └──────┬──────┘                                           │
│          │                                                   │
│          ▼                                                   │
│   ┌─────────────┐                                           │
│   │  AUGMENT    │ ◄── Combine query + context               │
│   └──────┬──────┘                                           │
│          │                                                   │
│          ▼                                                   │
│   ┌─────────────┐                                           │
│   │  GENERATE   │ ◄── LLM creates answer using context      │
│   └──────┬──────┘                                           │
│          │                                                   │
│          ▼                                                   │
│   Answer with Sources                                        │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## RAG Patterns Comparison

```
BASIC RAG:
Query ──▶ Retrieve ──▶ Generate ──▶ Answer
Best for: Simple factual questions

CONVERSATIONAL RAG:
Query + History ──▶ Condense ──▶ Retrieve ──▶ Generate ──▶ Answer
Best for: Follow-up questions, chatbots

MULTI-QUERY RAG:
Query ──▶ Generate Variations ──▶ Retrieve Each ──▶ Combine ──▶ Generate
Best for: Better recall, comprehensive answers

SELF-QUERY RAG:
Query ──▶ Extract Filters ──▶ Filtered Retrieve ──▶ Generate
Best for: "Show me X from 2023" type queries
```

## Code Example

```python
def basic_rag(query: str, retriever, llm) -> str:
    # 1. Retrieve relevant documents
    docs = retriever.get_relevant_documents(query)
    
    # 2. Format context
    context = "\n\n".join([
        f"[{i+1}] {doc.page_content}" 
        for i, doc in enumerate(docs)
    ])
    
    # 3. Generate answer
    prompt = f"""Answer based on the context below.
    
Context:
{context}

Question: {query}

Answer (cite sources using [1], [2], etc.):"""
    
    return llm.invoke(prompt).content

# Conversational RAG adds history handling
def conversational_rag(query, history, retriever, llm):
    # First, resolve references like "it", "that"
    standalone = condense_question(query, history, llm)
    # Then do basic RAG
    return basic_rag(standalone, retriever, llm)
```

## Context Formatting

```
GOOD FORMAT:
"[1] Source: policy.pdf, Page 5
Our refund policy allows returns within 30 days with receipt.

[2] Source: faq.pdf, Page 12
Refunds are processed within 5-7 business days."

→ Clear numbering for citations
→ Source info for verification
→ Separated for readability

BAD FORMAT:
"Our refund policy allows returns within 30 days with receipt. Refunds are processed within 5-7 business days."

→ No way to cite specific sources
→ Can't verify information
→ Mixed content is confusing
```

## Teach-Back

Explain in your own words:
1. Why do we need to "condense" questions in conversational RAG?
2. When would multi-query RAG outperform basic RAG?
3. What happens if retrieved context is irrelevant?
