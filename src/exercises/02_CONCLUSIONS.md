# Exercise 02: Messages - CONCLUSIONS

## Congratulations!

You've mastered the message system - the language of LLM communication.

---

## Skills Checklist

### I Can Now...

- [ ] Create `SystemMessage`, `HumanMessage`, and `AIMessage` objects
- [ ] Build multi-turn conversations as message lists
- [ ] Format conversation history for display
- [ ] Manage conversation context (add, retrieve, limit)
- [ ] Understand how message roles affect model behavior

### Key Takeaways

1. **Messages are structured** - Not just text, but typed objects with roles
2. **Order matters** - System → Human → AI sequence is important
3. **Context is everything** - Models need conversation history to understand references
4. **Memory has limits** - Context windows require smart management

---

## Reflection Questions

1. **Why use `SystemMessage` instead of putting instructions in `HumanMessage`?**
   - Your answer: _____________________

2. **What happens if you send messages without conversation history?**
   - Your answer: _____________________

3. **How would you handle a conversation that exceeds the context window?**
   - Your answer: _____________________

---

## Common Mistakes to Avoid

| Mistake | Better Approach |
|---------|-----------------|
| Forgetting SystemMessage | Always set behavior expectations |
| Losing conversation history | Store and pass previous messages |
| Ignoring message order | System first, then alternating Human/AI |
| Unlimited history | Implement max_messages or summarization |

---

## Mini-Project Challenge

### Project: Conversation Summarizer

Build a function that:
1. Takes a long conversation (>20 messages)
2. Summarizes older messages to save context space
3. Keeps recent messages intact

```python
def smart_context_manager(
    messages: List[BaseMessage],
    max_tokens: int = 4000
) -> List[BaseMessage]:
    """
    Manage context by summarizing old messages.
    
    Returns a list that fits within max_tokens while
    preserving the most important context.
    """
    # Your implementation here
    pass
```

---

## Connect to RAG

```
In RAG systems, messages are used to:

1. SystemMessage: "Answer using only the provided context"
2. HumanMessage: "Context: {retrieved_docs}\n\nQuestion: {query}"
3. AIMessage: Store previous answers for follow-up questions

┌────────────────────────────────────────────────────────┐
│ SystemMessage: RAG Instructions                         │
│ "You are a helpful assistant. Answer questions based   │
│  on the provided context. Cite your sources."          │
├────────────────────────────────────────────────────────┤
│ HumanMessage: Retrieved Context + User Query           │
│ "Context: [Doc1: ...] [Doc2: ...]                      │
│                                                        │
│  Question: What is the refund policy?"                 │
├────────────────────────────────────────────────────────┤
│ AIMessage: Previous Response (for follow-ups)          │
│ "Based on Doc1, the refund policy states..."           │
└────────────────────────────────────────────────────────┘
```

---

## What's Next?

**Exercise 03: Tool Definition** - Learn how to give models the ability to take actions.

Before moving on:
- [ ] All tests pass for Exercise 02
- [ ] You understand all message types
- [ ] You can build and manage conversations

---

## Quick Reference Card

```python
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)

# Build a conversation
messages = [
    SystemMessage("You are a helpful assistant."),
    HumanMessage("What is Python?"),
    AIMessage("Python is a programming language..."),
    HumanMessage("What can I build with it?"),
]

# Send to model
response = model.invoke(messages)

# Add to history
messages.append(response)
```

---

**Messages mastered! Onward to tools!**
