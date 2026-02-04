# Concept Guide: Memory & State

## Key Concepts

1. **Short-term = conversation history** - Recent messages in the thread
2. **Long-term = persistent storage** - User preferences, facts, past summaries
3. **State checkpoints** - Save and restore agent state (e.g. messages, tools used)
4. **Context window** - Balance history length vs token limits

## Visual: Memory Layers

```
┌─────────────────────────────────────────────────────────────┐
│                    MEMORY LAYERS                             │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   SHORT-TERM (current run)                                   │
│   [SystemMessage, HumanMessage, AIMessage, HumanMessage, ...]│
│   → Passed to model each turn; defines "current conversation"│
│                                                              │
│   LONG-TERM (stored)                                         │
│   user_preferences, past_conversations, user_info            │
│   → Retrieved and injected when relevant                     │
│                                                              │
│   CHECKPOINTS (save/restore)                                 │
│   { messages, tools_used, timestamp }                        │
│   → Restore state to continue or branch                      │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Code Example

### Short-term (conversation history)

```python
recent_messages = [
    SystemMessage("You are helpful"),
    HumanMessage("What is Python?"),
    AIMessage("Python is..."),
    HumanMessage("Tell me more"),  # Agent remembers previous
]
response = model.invoke(recent_messages)
```

### Long-term (persistent)

```python
memory = {
    "user_preferences": {"language": "python"},
    "past_conversations": ["...", "..."],
    "user_info": {"name": "Alice"},
}
context = memory.get("user_preferences")
```

### State checkpoints

```python
checkpoint = {
    "messages": current_messages,
    "tools_used": tools_called,
    "timestamp": datetime.now(),
}
restored_state = load_checkpoint(checkpoint_id)
```

## Teach-Back

Explain in your own words:
1. What's the difference between short-term and long-term memory in an agent?
2. When would you use a checkpoint?
3. Why might you trim old messages from conversation history?
