# Exercise 11: Middleware - CONNECTIONS

## Before You Start (5 minutes)

### What Do You Already Know?

Take a moment to reflect on these questions:

1. **Have you used Express.js or Django middleware?**
   - Middleware intercepts requests/responses to add functionality.

2. **Do you know about logging and monitoring?**
   - Tracking what happens in your application.

3. **Have you used caching to speed up applications?**
   - Storing results to avoid repeated computation.

### Real-World Analogy

Think of Middleware like **Airport Security Checkpoints**:

```
┌─────────────────────────────────────────────────────────────┐
│             THE AIRPORT SECURITY ANALOGY                     │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Passenger (Request) → ✈️ Flight (Core Function) → Arrival  │
│                                                              │
│  WITHOUT MIDDLEWARE:                                         │
│  Passenger walks straight to plane. No checks. 😱           │
│                                                              │
│  WITH MIDDLEWARE (Security Checkpoints):                     │
│                                                              │
│  Passenger                                                   │
│     │                                                        │
│     ▼                                                        │
│  ┌─────────────────────┐                                    │
│  │ LOGGING MIDDLEWARE  │ "Passenger John, Flight 123"       │
│  └─────────────────────┘                                    │
│     │                                                        │
│     ▼                                                        │
│  ┌─────────────────────┐                                    │
│  │ VALIDATION MIDDLEWARE│ Check ID, boarding pass           │
│  └─────────────────────┘                                    │
│     │                                                        │
│     ▼                                                        │
│  ┌─────────────────────┐                                    │
│  │ SECURITY MIDDLEWARE │ Scan bags, check for prohibited    │
│  └─────────────────────┘                                    │
│     │                                                        │
│     ▼                                                        │
│  ✈️ FLIGHT (Core Function)                                  │
│     │                                                        │
│     ▼                                                        │
│  ┌─────────────────────┐                                    │
│  │ EXIT MIDDLEWARE     │ Customs, baggage claim             │
│  └─────────────────────┘                                    │
│     │                                                        │
│     ▼                                                        │
│  Arrival                                                     │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Common Middleware Patterns

```
┌─────────────────┬────────────────────────────────────────────┐
│ Middleware Type │ What It Does                               │
├─────────────────┼────────────────────────────────────────────┤
│ Logging         │ Records all requests/responses             │
│ Validation      │ Checks inputs are valid before processing  │
│ Caching         │ Returns cached result if available         │
│ Rate Limiting   │ Prevents too many requests                 │
│ Authentication  │ Verifies user identity                     │
│ Error Handling  │ Catches and formats errors                 │
│ Transformation  │ Modifies input/output format               │
│ Monitoring      │ Tracks performance metrics                 │
└─────────────────┴────────────────────────────────────────────┘
```

### Prerequisite Checklist

Before starting this exercise, make sure you:

- [ ] Completed Exercises 01-10
- [ ] Understand decorators in Python
- [ ] Know about the chain of responsibility pattern
- [ ] Have used logging before

### Connect to Your Goal

**Building RAG Systems**: Middleware enables production-ready RAG:

```python
# RAG Pipeline with Middleware

class RAGPipeline:
    middlewares = [
        LoggingMiddleware(),      # Log all queries
        CachingMiddleware(),      # Cache repeated queries
        ValidationMiddleware(),   # Validate query format
        RateLimitMiddleware(),    # Prevent abuse
        MetricsMiddleware(),      # Track performance
    ]
    
    def query(self, question: str) -> str:
        # Request passes through all middleware
        context = {"query": question}
        
        for mw in self.middlewares:
            context = mw.before(context)
        
        # Core RAG operation
        result = self.retrieve_and_generate(context)
        
        for mw in reversed(self.middlewares):
            result = mw.after(result)
        
        return result
```

### Why Middleware for RAG?

```
┌─────────────────────────────────────────────────────────────┐
│                    RAG MIDDLEWARE BENEFITS                   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  CACHING MIDDLEWARE:                                         │
│  "What's the refund policy?" asked 100 times                │
│  → Cache the answer, don't re-retrieve every time           │
│  → Saves API costs, improves latency                         │
│                                                              │
│  LOGGING MIDDLEWARE:                                         │
│  Track: query, retrieved_docs, response, latency            │
│  → Debug issues: "Why did it give wrong answer?"            │
│  → Improve system: "What queries fail most?"                │
│                                                              │
│  VALIDATION MIDDLEWARE:                                      │
│  Check: query not empty, not too long, not harmful          │
│  → Prevent: injection attacks, resource abuse               │
│                                                              │
│  MONITORING MIDDLEWARE:                                      │
│  Measure: retrieval_time, generation_time, total_latency    │
│  → Alert: if latency > 5s, if error_rate > 5%              │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Middleware Chain Flow

```
Request → MW1.before() → MW2.before() → MW3.before()
                                              │
                                              ▼
                                        Core Function
                                              │
                                              ▼
Response ← MW1.after() ← MW2.after() ← MW3.after()
```

### Warm-Up Activity

Before coding, design middleware for RAG:

**Scenario**: Production RAG system needs reliability and observability

1. **What would LoggingMiddleware log?**
   - Input: _____________________
   - Output: _____________________

2. **What would CachingMiddleware cache?**
   - Key: _____________________
   - Value: _____________________
   - TTL: _____________________

3. **What would ValidationMiddleware check?**
   - _____________________
   - _____________________

4. **What metrics would you track?**
   - _____________________
   - _____________________

---

**Ready?** Now proceed to `11_middleware.py` and implement the functions!
