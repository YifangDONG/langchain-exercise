# Concept Guide: Streaming

## Key Concepts

1. **Stream tokens as they're generated** - Don't wait for the full response
2. **Better UX** - User sees progress; feels faster
3. **Same for agents** - Stream events: AI chunks, tool calls, tool results
4. **Collect if needed** - Loop and concatenate for a full string

## Visual: Invoke vs Stream

```
┌─────────────────────────────────────────────────────────────┐
│                  INVOKE vs STREAM                             │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   invoke()   ───▶ [.......... wait ..........] ───▶ "Full   │
│                   (user sees nothing)             response" │
│                                                              │
│   stream()   ───▶ "The" ──▶ " capital" ──▶ " of" ──▶ ...   │
│                   (user sees text appear in real time)       │
│                                                              │
│   Use stream for: chat UIs, long answers, showing progress  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Code Example

```python
# Stream individual tokens from model
for chunk in model.stream("Hello world"):
    print(chunk.content, end="", flush=True)

# Collect complete response
complete = ""
for chunk in model.stream(prompt):
    complete += chunk.content
```

### Event Streaming (Agents)

```python
# Agents emit detailed events
events = agent.stream({"messages": [...]})

for event in events:
    if event.get("type") == "ai":
        print("Agent thinking:", event["content"])
    elif event.get("type") == "tool":
        print("Agent using tool:", event["tool"])
    elif event.get("type") == "result":
        print("Tool result:", event["output"])
```

## Teach-Back

Explain in your own words:
1. When would you use stream() instead of invoke()?
2. What kind of events might an agent stream?
3. How would you get the full response when streaming?
