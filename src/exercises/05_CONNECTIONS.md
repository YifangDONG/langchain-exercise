# Exercise 05: Tool Execution - CONNECTIONS

## Before You Start (5 minutes)

### What Do You Already Know?

Take a moment to reflect on these questions:

1. **Have you ever handled exceptions in code?**
   - Tools can fail, and we need to handle that gracefully.

2. **Do you know what "retry logic" means?**
   - When something fails, sometimes trying again works.

3. **Have you used logging to debug issues?**
   - Tracking what happened is crucial for production systems.

### Real-World Analogy

Think of Tool Execution like a **Restaurant Kitchen**:

```
┌─────────────────────────────────────────────────────────────┐
│                  THE KITCHEN ANALOGY                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Order (Tool Call Request):                                  │
│  "Make a Caesar salad"                                       │
│                                                              │
│  Kitchen (Tool Execution):                                   │
│                                                              │
│  1. VALIDATE: "Do we have all ingredients?"                 │
│     - If no romaine lettuce → Error: "Missing ingredient"   │
│     - If all good → Proceed                                  │
│                                                              │
│  2. EXECUTE: Actually make the salad                         │
│     - Might fail: "Oven broken" → Retry with backup oven    │
│     - Might succeed: Salad ready!                           │
│                                                              │
│  3. LOG: "Order #42: Caesar salad, 3min, success"           │
│     - Track timing, success/failure, any issues             │
│                                                              │
│  4. HANDLE ERRORS:                                           │
│     - Ingredient missing? Tell customer, suggest alternative │
│     - Equipment failed? Retry or graceful failure            │
│     - Timeout? Don't leave customer waiting forever          │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Why Tool Execution Matters

```
Without Proper Execution Handling:

  User: "What's the weather in Paris?"
  Agent: *calls weather API*
  API: *times out*
  System: *crashes*
  User: "???"

With Proper Execution Handling:

  User: "What's the weather in Paris?"
  Agent: *calls weather API*
  API: *times out*
  System: *retries with backoff*
  API: *still failing*
  System: *returns graceful error*
  Agent: "I couldn't fetch the weather right now. Try again later."
  User: "Thanks for letting me know!"
```

### Prerequisite Checklist

Before starting this exercise, make sure you:

- [ ] Completed Exercises 01-04
- [ ] Understand try/except error handling
- [ ] Know about Python decorators
- [ ] Understand basic logging concepts

### Connect to Your Goal

**Building RAG Systems**: Robust tool execution is critical because:

1. **Vector DB queries can fail** - Network issues, timeouts
2. **Embedding API calls can fail** - Rate limits, service outages
3. **Document parsing can fail** - Corrupted files, unsupported formats
4. **Production RAG needs reliability** - Users expect it to work

### The Execution Loop Pattern

```python
# This is the pattern you'll implement:

def tool_execution_loop(agent, query, max_iterations=10):
    """
    The core agent loop with proper execution handling.
    """
    for i in range(max_iterations):
        # 1. Agent decides what to do
        action = agent.decide(query)
        
        if action.is_final_answer:
            return action.answer
        
        # 2. Execute the tool with error handling
        try:
            result = execute_tool_safely(action.tool, action.input)
        except ToolError as e:
            result = handle_error(e)
        
        # 3. Feed result back to agent
        query = add_observation(query, result)
    
    return "Max iterations reached"
```

### Error Types to Handle

```
┌──────────────────┬──────────────────────────────────────┐
│ Error Type       │ How to Handle                        │
├──────────────────┼──────────────────────────────────────┤
│ ValidationError  │ Return helpful message, don't retry  │
│ TimeoutError     │ Retry with exponential backoff       │
│ RateLimitError   │ Wait and retry                       │
│ NetworkError     │ Retry, then fail gracefully          │
│ PermissionError  │ Return error, suggest alternative    │
│ UnknownError     │ Log details, fail gracefully         │
└──────────────────┴──────────────────────────────────────┘
```

### Warm-Up Activity

Before coding, plan error handling for a RAG retrieval tool:

**Tool**: `search_documents(query: str) -> List[Document]`

What could go wrong?

1. **Error**: _____________________
   **Handle by**: _____________________

2. **Error**: _____________________
   **Handle by**: _____________________

3. **Error**: _____________________
   **Handle by**: _____________________

---

**Ready?** Now proceed to `05_tool_execution.py` and implement the functions!
