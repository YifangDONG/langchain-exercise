# Exercise 08: System Prompts - CONCLUSIONS

## Congratulations!

You've learned prompt engineering - the art of guiding AI behavior effectively.

---

## Skills Checklist

### I Can Now...

- [ ] Create effective system prompts
- [ ] Use dynamic prompts with variable substitution
- [ ] Create reusable prompt templates
- [ ] Implement chain-of-thought prompting
- [ ] Inject context into prompts
- [ ] Compare and measure prompt quality

### Key Takeaways

1. **Prompts define behavior** - Clear instructions = better results
2. **Be specific** - Vague prompts get vague answers
3. **Use templates** - Reusability and consistency
4. **Chain-of-thought works** - Step-by-step improves reasoning

---

## Reflection Questions

1. **What makes a good RAG system prompt?**
   - Your answer: _____________________

2. **When should you use chain-of-thought prompting?**
   - Your answer: _____________________

3. **How do you prevent the model from using prior knowledge in RAG?**
   - Your answer: _____________________

---

## Common Mistakes to Avoid

| Mistake | Better Approach |
|---------|-----------------|
| Vague instructions | Be specific: "2-3 sentences" not "be brief" |
| No examples | Include few-shot examples |
| Ignoring edge cases | Tell model what to do when unsure |
| One-size-fits-all | Customize prompts for different tasks |

---

## Mini-Project Challenge

### Project: RAG Prompt Library

Build a library of prompts for different RAG scenarios:

```python
RAG_PROMPTS = {
    "factual_qa": """You answer factual questions using ONLY the provided context.
    
Context:
{context}

Rules:
1. Only use information from the context
2. If the answer isn't in the context, say "I don't have that information"
3. Cite the source document for each fact

Question: {question}""",

    "summarization": """Summarize the following documents concisely.

Documents:
{documents}

Provide:
1. A 2-3 sentence summary
2. Key points as bullet points
3. Any important caveats""",

    "comparison": """Compare and contrast information from multiple sources.

Sources:
{sources}

Question: {question}

Format your response as:
- Similarities
- Differences
- Conclusion"""
}
```

---

## Connect to RAG

```
RAG Prompt Anatomy:

┌─────────────────────────────────────────────────────────────┐
│  SYSTEM PROMPT COMPONENTS FOR RAG:                           │
│                                                              │
│  1. ROLE DEFINITION                                          │
│     "You are a knowledgeable assistant that answers         │
│      questions based on company documentation."              │
│                                                              │
│  2. CONTEXT PLACEMENT                                        │
│     "Use the following documents to answer:                  │
│      {retrieved_documents}"                                  │
│                                                              │
│  3. CONSTRAINTS                                              │
│     "Only use information from the provided context.         │
│      Do not use prior knowledge."                            │
│                                                              │
│  4. OUTPUT FORMAT                                            │
│     "Format your answer with:                                │
│      - A direct answer                                       │
│      - Supporting quotes                                     │
│      - Source citations"                                     │
│                                                              │
│  5. EDGE CASE HANDLING                                       │
│     "If the information is not in the context, respond:      │
│      'Based on the available documents, I cannot answer      │
│       this question. Try asking about [related topic]'"      │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## What's Next?

**Exercise 09: Streaming** - Provide real-time feedback for better UX.

Before moving on:
- [ ] All tests pass for Exercise 08
- [ ] You can write effective system prompts
- [ ] You understand prompt templates

---

## Quick Reference Card

```python
from string import Template

# Simple template
RAG_PROMPT = Template("""
You are an expert in $domain.

Context:
$context

Question: $question

Answer based only on the context provided.
""")

prompt = RAG_PROMPT.substitute(
    domain="company policies",
    context="[Retrieved documents here]",
    question="What is the vacation policy?"
)

# Chain-of-thought template
COT_PROMPT = """
Answer the following question step by step:

Question: {question}

Think through this:
1. What information do I need?
2. What does the context tell me?
3. How do I synthesize an answer?

Context: {context}

Now provide your answer:
"""
```

---

**Prompt engineering complete! Time for streaming!**
