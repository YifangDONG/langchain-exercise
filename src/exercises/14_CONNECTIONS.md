# Exercise 14: Text Chunking - CONNECTIONS

## Before You Start (5 minutes)

### What Do You Already Know?

Take a moment to reflect on these questions:

1. **Have you ever split a large file into smaller parts?**
   - Like breaking a book into chapters for easier reading.

2. **Do you know why search engines index paragraphs, not whole books?**
   - Smaller units enable more precise retrieval.

3. **Have you noticed how context helps understanding?**
   - "It was blue" makes no sense without knowing what "it" refers to.

### Real-World Analogy

Think of Text Chunking like **Preparing Ingredients for Cooking**:

```
┌─────────────────────────────────────────────────────────────┐
│              THE COOKING INGREDIENTS ANALOGY                 │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  You have a whole chicken to prepare:                        │
│                                                              │
│  TOO BIG (No chunking):                                      │
│  🐔 Whole chicken → Hard to cook evenly, wasteful           │
│                                                              │
│  TOO SMALL (Over-chunking):                                  │
│  🍖 Ground to paste → Lost all structure, can't identify    │
│                                                              │
│  JUST RIGHT (Smart chunking):                                │
│  🍗 Breast, thigh, wing, leg → Perfect cooking portions     │
│     Each piece is:                                           │
│     • Complete enough to be useful                           │
│     • Small enough to cook evenly                            │
│     • Labeled (metadata) for identification                  │
│                                                              │
│  RAG Chunking = Finding the "chicken breast" of your docs   │
│  Complete thoughts, optimal size, properly labeled           │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Why Chunk Size Matters

```
THE GOLDILOCKS PROBLEM:

┌─────────────────────────────────────────────────────────────┐
│  CHUNKS TOO SMALL (100 chars):                               │
│  "The refund policy allows"     ← Not enough context!       │
│  "returns within 30 days"       ← What about it?            │
│  "of purchase with receipt"     ← Disconnected pieces       │
│                                                              │
│  Result: Retrieves fragments, misses full answer            │
├─────────────────────────────────────────────────────────────┤
│  CHUNKS TOO LARGE (10,000 chars):                            │
│  "Chapter 5: Customer Service...                             │
│   [Refund policy buried in 2000 words of other content]     │
│   ...End of Chapter 5"                                       │
│                                                              │
│  Result: Retrieves too much, dilutes relevance              │
├─────────────────────────────────────────────────────────────┤
│  CHUNKS JUST RIGHT (500-1000 chars):                         │
│  "Refund Policy: Customers may return items within 30       │
│   days of purchase. A valid receipt is required. Items      │
│   must be unused and in original packaging. Refunds are     │
│   processed within 5-7 business days."                       │
│                                                              │
│  Result: Complete, focused, highly relevant ✓               │
└─────────────────────────────────────────────────────────────┘
```

### Prerequisite Checklist

Before starting this exercise, make sure you:

- [ ] Completed Exercise 13 (Document Loading)
- [ ] Understand string operations in Python
- [ ] Know about text tokenization basics
- [ ] Have seen how context windows work in LLMs

### Connect to Your Goal

**Building the Best RAG System**: Chunking determines retrieval quality.

```
Chunking Strategy Impact:

                      Chunk Size
            Small ←───────┼───────→ Large
                          │
    Precision ↑           │           ↑ Context
    Noise ↓               │           ↑ Noise
    Context loss ↓        │           ↓ Precision
                          │
              OPTIMAL ZONE
              (500-1500 chars typically)
```

### Warm-Up Activity

Before coding, analyze this text:

```
# Product Manual

## Chapter 1: Getting Started

Welcome to your new device. This chapter covers initial setup.

### 1.1 Unboxing

Carefully remove the device from packaging. You should find:
- Main device
- Power adapter
- Quick start guide

### 1.2 First Power On

Press and hold the power button for 3 seconds. The LED will 
turn blue when the device is ready.

## Chapter 2: Features

This chapter covers the main features of your device.
```

Questions:
1. **Where would you split this for RAG?**
   - _____________________

2. **What metadata would help retrieval?**
   - _____________________

3. **How much overlap would you use?**
   - _____________________

---

**Ready?** Now proceed to `14_text_chunking.py` and implement the functions!
