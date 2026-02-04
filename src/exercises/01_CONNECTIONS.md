# Exercise 01: Model Basics - CONNECTIONS

## Before You Start (5 minutes)

### What Do You Already Know?

Take a moment to reflect on these questions:

1. **Have you ever used an API before?** (REST APIs, GraphQL, etc.)
   - If yes, you already understand the request/response pattern that LLMs use!

2. **Have you used any AI assistants?** (ChatGPT, Claude, Copilot)
   - If yes, you've experienced what we're about to build programmatically.

3. **Do you know what "streaming" means in video/audio?**
   - The same concept applies to LLM responses - getting data piece by piece.

### Real-World Analogy

Think of a Language Model like a **very knowledgeable consultant**:

```
┌─────────────────────────────────────────────────────────────┐
│                    THE CONSULTANT ANALOGY                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  invoke()  = Asking a question and waiting for full answer  │
│              "What's the best approach for X?"              │
│              → Consultant thinks, then gives complete answer │
│                                                              │
│  stream()  = Getting the answer as they speak               │
│              Like a live conversation where you hear        │
│              each word as it's spoken                        │
│                                                              │
│  batch()   = Asking multiple questions at once              │
│              "Here are 5 questions - answer all of them"    │
│              → More efficient than asking one by one         │
│                                                              │
│  temperature = How creative vs consistent the consultant is │
│              0.0 = By the book, predictable                  │
│              1.0 = Creative, varied responses                │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Prerequisite Checklist

Before starting this exercise, make sure you can:

- [ ] Write basic Python functions with type hints
- [ ] Use iterators and generators (`yield` keyword)
- [ ] Work with environment variables
- [ ] Understand basic API concepts (request/response)

### Connect to Your Goal

**Building RAG Systems**: This exercise teaches you the foundation - how to communicate with LLMs. Every RAG system needs to:
1. Send prompts to a model (invoke)
2. Get responses efficiently (batch for processing many documents)
3. Show real-time progress (stream for user experience)

### Warm-Up Activity

Before coding, try this mental exercise:

> Imagine you're building a customer service bot. List 3 situations where you'd want:
> - A complete answer before showing anything (invoke)
> - Real-time typing effect (stream)  
> - Process many customer queries efficiently (batch)

Write your answers here (or just think about them):
1. invoke: _______________
2. stream: _______________
3. batch: _______________

---

**Ready?** Now proceed to `01_model_basics.py` and implement the functions!
