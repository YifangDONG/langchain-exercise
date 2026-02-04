# Exercise 02: Messages - CONNECTIONS

## Before You Start (5 minutes)

### What Do You Already Know?

Take a moment to reflect on these questions:

1. **Have you ever had a text conversation?** (SMS, WhatsApp, Slack)
   - If yes, you already understand the concept of message exchanges!

2. **Do you know what "context" means in a conversation?**
   - When someone says "it" or "that" - you know what they mean because of previous messages.

3. **Have you used chat applications with different user roles?**
   - Admin vs User vs Bot messages are displayed differently.

### Real-World Analogy

Think of Messages like a **group chat with specific roles**:

```
┌─────────────────────────────────────────────────────────────┐
│                    THE GROUP CHAT ANALOGY                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  SystemMessage = The "pinned rules" at the top of the chat  │
│                  "This is a professional workspace.          │
│                   Be helpful and respectful."                │
│                  Everyone follows these guidelines.          │
│                                                              │
│  HumanMessage  = Your messages in the chat                   │
│                  Questions, requests, instructions           │
│                                                              │
│  AIMessage     = The assistant's responses                   │
│                  Answers, explanations, suggestions          │
│                                                              │
│  ToolMessage   = Automated bot messages                      │
│                  "Weather Bot: Current temp is 72°F"         │
│                  Results from external services              │
│                                                              │
│  Conversation  = The entire chat history                     │
│                  Context that helps everyone understand      │
│                  what "it" and "that" refer to               │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Prerequisite Checklist

Before starting this exercise, make sure you:

- [ ] Completed Exercise 01 (Model Basics)
- [ ] Understand Python lists and list operations
- [ ] Know how to work with Python classes/objects
- [ ] Understand string formatting

### Connect to Your Goal

**Building RAG Systems**: Messages are crucial for RAG because:
1. **SystemMessage** sets the RAG behavior ("Answer based on the context provided")
2. **HumanMessage** contains the user's query
3. **AIMessage** stores previous responses for multi-turn conversations
4. **Context management** ensures the model has relevant retrieved information

### Mental Model

```
User Query: "What was the revenue last quarter?"

RAG System builds messages:
┌────────────────────────────────────────────────────────┐
│ SystemMessage: "Answer questions using the provided    │
│                 context. If unsure, say so."           │
├────────────────────────────────────────────────────────┤
│ HumanMessage:  "Context: [Retrieved documents...]      │
│                                                        │
│                 Question: What was the revenue?"       │
├────────────────────────────────────────────────────────┤
│ AIMessage:     "Based on the Q3 report, revenue was..."│
└────────────────────────────────────────────────────────┘
```

### Warm-Up Activity

Before coding, answer these questions:

1. **Why can't we just send raw text to the model?**
   - Hint: Think about how the model knows who said what.

2. **What happens if we don't include conversation history?**
   - Hint: What does "it" mean without context?

3. **Why is SystemMessage important for RAG?**
   - Hint: How do you tell the model to use retrieved context?

---

**Ready?** Now proceed to `02_messages.py` and implement the functions!
