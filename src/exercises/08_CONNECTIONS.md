# Exercise 08: System Prompts - CONNECTIONS

## Before You Start (5 minutes)

### What Do You Already Know?

Take a moment to reflect on these questions:

1. **Have you ever given someone detailed instructions before they started a task?**
   - "Remember to be polite, check your work, and ask if unsure."

2. **Do you know about "personas" in UX design?**
   - A persona is a defined character with specific traits.

3. **Have you used templates with placeholders?**
   - Like "Dear {name}, thank you for your {purchase}."

### Real-World Analogy

Think of System Prompts like **Job Training**:

```
┌─────────────────────────────────────────────────────────────┐
│                THE JOB TRAINING ANALOGY                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  New Employee (LLM) arrives at work...                       │
│                                                              │
│  SYSTEM PROMPT = Employee Handbook + Training                │
│                                                              │
│  "Welcome! Here's how to do your job:                        │
│                                                              │
│  1. YOUR ROLE:                                               │
│     You are a customer support specialist for TechCorp.      │
│                                                              │
│  2. YOUR PERSONALITY:                                        │
│     Be friendly, patient, and professional.                  │
│                                                              │
│  3. YOUR KNOWLEDGE:                                          │
│     Use the company knowledge base to answer questions.      │
│     If you don't know, say 'Let me check on that.'          │
│                                                              │
│  4. YOUR RULES:                                              │
│     - Never share confidential information                   │
│     - Always cite your sources                               │
│     - Escalate complex issues to humans                      │
│                                                              │
│  5. YOUR FORMAT:                                             │
│     Start with greeting, provide answer, end with offer      │
│     to help more."                                           │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### The Power of Good Prompts

```
BAD PROMPT:
"Answer questions."

Result: Generic, inconsistent answers

GOOD PROMPT:
"You are a technical documentation assistant. Your responses should:
1. Be accurate and cite sources
2. Use clear, concise language
3. Include code examples when relevant
4. Acknowledge uncertainty with 'Based on available information...'
5. Format output with headers and bullet points"

Result: Consistent, high-quality, well-formatted answers
```

### Prerequisite Checklist

Before starting this exercise, make sure you:

- [ ] Completed Exercises 01-07
- [ ] Understand string formatting and templates
- [ ] Know about f-strings and string substitution
- [ ] Have experimented with different prompt styles

### Connect to Your Goal

**Building RAG Systems**: The system prompt is CRITICAL for RAG:

```python
# RAG System Prompt Template

RAG_PROMPT = """You are a knowledgeable assistant that answers questions 
based on the provided context.

CONTEXT:
{retrieved_documents}

RULES:
1. Only use information from the context above
2. If the answer isn't in the context, say "I don't have information about that"
3. Always cite which document your answer comes from
4. If multiple documents conflict, acknowledge the discrepancy

USER QUESTION: {question}

Provide a clear, accurate answer based on the context."""
```

### Chain of Thought for RAG

```python
COT_RAG_PROMPT = """Answer the question using the provided context.

Context: {context}
Question: {question}

Think through this step-by-step:
1. What specific information does the question ask for?
2. Which parts of the context are relevant?
3. What is the answer based on this context?
4. What sources support this answer?

Now provide your answer with citations."""
```

### Prompt Engineering Principles

```
┌──────────────────┬──────────────────────────────────────┐
│ Principle        │ Example                              │
├──────────────────┼──────────────────────────────────────┤
│ Be Specific      │ "Answer in 2-3 sentences" not "Be    │
│                  │ concise"                             │
├──────────────────┼──────────────────────────────────────┤
│ Give Examples    │ "Format like: 'According to [doc],  │
│                  │ the answer is...'"                   │
├──────────────────┼──────────────────────────────────────┤
│ Set Boundaries   │ "Only use provided context, don't   │
│                  │ use prior knowledge"                 │
├──────────────────┼──────────────────────────────────────┤
│ Define Persona   │ "You are an expert in {domain}"     │
├──────────────────┼──────────────────────────────────────┤
│ Handle Edge      │ "If unsure, say 'Based on available │
│ Cases            │ information...'"                     │
└──────────────────┴──────────────────────────────────────┘
```

### Warm-Up Activity

Before coding, write a RAG system prompt:

**Scenario**: A customer support chatbot with access to product documentation

Write your system prompt (consider role, rules, format, edge cases):

```
You are _____________________.

Your knowledge base contains: _____________________.

When answering:
1. _____________________
2. _____________________
3. _____________________

If you don't know: _____________________

Response format: _____________________
```

---

**Ready?** Now proceed to `08_system_prompts.py` and implement the functions!
