# Exercise 16: Retrieval Chains - CONNECTIONS

## Before You Start (5 minutes)

### What Do You Already Know?

Take a moment to reflect on these questions:

1. **Have you ever combined two things to get a better result?**
   - Like mixing ingredients to make a recipe.

2. **Do you understand the difference between search and answer?**
   - Finding information vs explaining it.

3. **Have you dealt with follow-up questions in conversation?**
   - "What about the other one?" - requires context.

### Real-World Analogy

Think of RAG Chains like a **Research Librarian**:

```
┌─────────────────────────────────────────────────────────────┐
│              THE RESEARCH LIBRARIAN ANALOGY                  │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  You ask: "What's the company refund policy?"               │
│                                                              │
│  WITHOUT RAG (LLM alone):                                    │
│  Librarian guesses based on general knowledge               │
│  "Typically, companies have 30-day policies..." (maybe wrong)│
│                                                              │
│  WITH RAG (Librarian + Library):                             │
│                                                              │
│  1. RETRIEVE: Librarian searches shelves                     │
│     "Let me find our policy documents..."                   │
│     📚 → Finds: policy.pdf, faq.pdf, terms.pdf              │
│                                                              │
│  2. READ: Librarian reads relevant sections                  │
│     "According to section 5.2..."                           │
│                                                              │
│  3. GENERATE: Librarian answers with citations               │
│     "Our refund policy (see policy.pdf, page 5) states     │
│      that returns are accepted within 30 days with          │
│      receipt."                                               │
│                                                              │
│  Result: Accurate answer + Sources you can verify            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### The RAG Formula

```
RAG = Retrieval + Augmented Generation

┌─────────────────────────────────────────────────────────────┐
│                                                              │
│  Step 1: RETRIEVAL                                           │
│  Query → Vector Search → Relevant Documents                  │
│                                                              │
│  Step 2: AUGMENTATION                                        │
│  Combine Query + Retrieved Context                           │
│                                                              │
│  Step 3: GENERATION                                          │
│  Augmented Input → LLM → Answer with Sources                │
│                                                              │
└─────────────────────────────────────────────────────────────┘

This exercise: Putting all three steps together!
```

### Prerequisite Checklist

Before starting this exercise, make sure you:

- [ ] Completed Exercises 13-15 (Loading, Chunking, Embeddings)
- [ ] Understand how vector stores work
- [ ] Know how to format prompts for LLMs
- [ ] Have seen the exercises on structured output (07)

### Connect to Your Goal

**Building the Best RAG System**: This is where it all comes together!

```
You've learned:
  ✓ Loading documents (Exercise 13)
  ✓ Chunking text (Exercise 14)
  ✓ Creating embeddings & vector stores (Exercise 15)

Now you'll learn:
  → Combining retrieval + generation (THIS EXERCISE!)
  → Different retrieval strategies
  → Handling edge cases
  → Adding citations
```

### RAG Chain Patterns

```
┌─────────────────────────────────────────────────────────────┐
│  BASIC RAG:                                                  │
│  Query → Retrieve → Generate → Answer                        │
│  (Simple, fast, good for most cases)                         │
├─────────────────────────────────────────────────────────────┤
│  CONVERSATIONAL RAG:                                         │
│  Query + History → Condense → Retrieve → Generate → Answer  │
│  (For chatbots, follow-up questions)                         │
├─────────────────────────────────────────────────────────────┤
│  MULTI-QUERY RAG:                                            │
│  Query → Generate Variations → Retrieve Each → Combine      │
│  (Better recall, more comprehensive)                         │
├─────────────────────────────────────────────────────────────┤
│  SELF-QUERY RAG:                                             │
│  Query → Extract Filters → Filtered Retrieve → Generate     │
│  (When users want to filter by metadata)                     │
└─────────────────────────────────────────────────────────────┘
```

### Warm-Up Activity

Before coding, design a RAG chain:

**Scenario**: Customer support bot for an e-commerce site

1. **What should the basic RAG chain do?**
   - _____________________

2. **How would you handle "What's the warranty on that?"**
   - (Hint: conversational RAG)
   - _____________________

3. **How would you handle "Show me electronics under $100"?**
   - (Hint: self-query RAG)
   - _____________________

---

**Ready?** Now proceed to `16_retrieval_chains.py` and implement the functions!
