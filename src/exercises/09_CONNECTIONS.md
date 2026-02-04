# Exercise 09: Streaming - CONNECTIONS

## Before You Start (5 minutes)

### What Do You Already Know?

Take a moment to reflect on these questions:

1. **Have you watched a video that buffers vs one that plays smoothly?**
   - Streaming lets you see content as it loads.

2. **Do you know how a typewriter effect works in chat UIs?**
   - Each character appears one by one, not all at once.

3. **Have you used progress bars in long operations?**
   - Feedback during waiting makes the experience better.

### Real-World Analogy

Think of Streaming like **Live TV vs Recorded Shows**:

```
┌─────────────────────────────────────────────────────────────┐
│             THE TV BROADCAST ANALOGY                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  WITHOUT STREAMING (Recorded Show):                         │
│                                                              │
│  1. Wait for entire show to download... ⏳                  │
│  2. Wait more... ⏳⏳                                        │
│  3. Still waiting... ⏳⏳⏳                                  │
│  4. Finally! Watch entire show at once. 📺                  │
│                                                              │
│  User experience: "Is this thing even working?"             │
│                                                              │
│  WITH STREAMING (Live TV):                                   │
│                                                              │
│  1. Start watching immediately! 📺                          │
│  2. Content arrives as it's produced                         │
│  3. See progress in real-time                                │
│  4. Know it's working because you see updates               │
│                                                              │
│  User experience: "Great, I can see it's responding!"       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Why Streaming Matters for UX

```
Request: "Summarize this 50-page document"

WITHOUT STREAMING:
┌────────────────────────────────────┐
│  Processing...                      │
│                                     │
│  [Nothing for 30 seconds]           │
│                                     │
│  User: "Is it frozen? Should I     │
│         refresh? Did it crash?"     │
└────────────────────────────────────┘

WITH STREAMING:
┌────────────────────────────────────┐
│  The document discusses several     │
│  key topics including...            │
│  [typing indicator]█                │
│                                     │
│  User: "Oh good, it's working!     │
│         I can read as it types."    │
└────────────────────────────────────┘
```

### Prerequisite Checklist

Before starting this exercise, make sure you:

- [ ] Completed Exercises 01-08
- [ ] Understand Python generators and `yield`
- [ ] Know about async/await basics
- [ ] Have used iterators before

### Connect to Your Goal

**Building RAG Systems**: Streaming enables:

1. **Long document processing** - Show progress as you process
2. **Real-time retrieval feedback** - "Searching...", "Found 5 docs...", "Generating..."
3. **Better perceived performance** - Users see activity immediately
4. **Interruptible operations** - User can cancel if output looks wrong

### Streaming in RAG Pipeline

```
Traditional RAG (No Streaming):
┌─────────────────────────────────────────────────────────────┐
│  Query → [BLACK BOX - Wait 10 sec] → Full Answer            │
└─────────────────────────────────────────────────────────────┘

Streaming RAG:
┌─────────────────────────────────────────────────────────────┐
│  Query                                                       │
│    │                                                         │
│    ▼ Stream Event: "Searching knowledge base..."            │
│    ▼ Stream Event: "Found 5 relevant documents"             │
│    ▼ Stream Event: "Generating response..."                 │
│    ▼ Stream Token: "Based"                                  │
│    ▼ Stream Token: " on"                                    │
│    ▼ Stream Token: " the"                                   │
│    ▼ Stream Token: " documents"                             │
│    ▼ ...                                                    │
│    ▼ Stream Event: "Complete!"                              │
└─────────────────────────────────────────────────────────────┘
```

### Types of Streaming

```python
# 1. Token Streaming - Each word/token as it's generated
for token in model.stream("Summarize this"):
    print(token, end="", flush=True)
# Output: "The" "document" "discusses" "..."

# 2. Event Streaming - Structured events from agent
for event in agent.stream_events(query):
    if event.type == "retrieval_start":
        print("Searching...")
    elif event.type == "retrieval_complete":
        print(f"Found {event.count} documents")
    elif event.type == "generation_token":
        print(event.token, end="")

# 3. Buffered Streaming - Collect chunks before sending
buffer = ""
for token in model.stream(prompt):
    buffer += token
    if len(buffer) > 50 or token.endswith("."):
        yield buffer
        buffer = ""
```

### Warm-Up Activity

Before coding, think about streaming UX:

**Scenario**: You're building a RAG chatbot UI

1. **What should the user see during retrieval?**
   - _____________________

2. **What should the user see during generation?**
   - _____________________

3. **How would you handle errors mid-stream?**
   - _____________________

4. **How would you let users cancel a long response?**
   - _____________________

---

**Ready?** Now proceed to `09_streaming.py` and implement the functions!
