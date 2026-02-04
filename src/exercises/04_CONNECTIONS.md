# Exercise 04: Basic Agents - CONNECTIONS

## Before You Start (5 minutes)

### What Do You Already Know?

Take a moment to reflect on these questions:

1. **Have you ever followed a recipe while cooking?**
   - You think about what to do, do it, check the result, then decide next step.

2. **Do you know how a GPS navigation works?**
   - It plans a route, checks your position, and adjusts if needed.

3. **Have you debugged code by reasoning through it?**
   - "If X is true, then Y should happen... let me check..."

### Real-World Analogy

Think of an Agent like a **Problem-Solving Detective**:

```
┌─────────────────────────────────────────────────────────────┐
│                  THE DETECTIVE ANALOGY                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Case: "Find out what the weather is in Paris and            │
│         calculate if I need an umbrella"                     │
│                                                              │
│  Detective (Agent) Process:                                  │
│                                                              │
│  🤔 THOUGHT: "I need to find the weather in Paris first"    │
│       ↓                                                      │
│  ⚙️ ACTION: Use weather_tool("Paris")                        │
│       ↓                                                      │
│  👀 OBSERVATION: "Paris: 65°F, 80% chance of rain"          │
│       ↓                                                      │
│  🤔 THOUGHT: "80% rain chance is high, need umbrella"       │
│       ↓                                                      │
│  ✅ ANSWER: "Yes, bring an umbrella. 80% rain chance."      │
│                                                              │
│  This is the ReAct Pattern:                                  │
│  Reasoning + Acting = ReAct                                  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### The ReAct Loop Visualized

```
         ┌─────────────┐
         │   START     │
         └──────┬──────┘
                │
                ▼
         ┌─────────────┐
    ┌───▶│   THINK     │ "What do I need to do?"
    │    └──────┬──────┘
    │           │
    │           ▼
    │    ┌─────────────┐
    │    │    ACT      │ Call a tool
    │    └──────┬──────┘
    │           │
    │           ▼
    │    ┌─────────────┐
    │    │  OBSERVE    │ See the result
    │    └──────┬──────┘
    │           │
    │           ▼
    │    ┌─────────────┐
    │    │  COMPLETE?  │───Yes──▶ FINAL ANSWER
    │    └──────┬──────┘
    │           │
    │          No
    └───────────┘
```

### Prerequisite Checklist

Before starting this exercise, make sure you:

- [ ] Completed Exercises 01-03 (Models, Messages, Tools)
- [ ] Understand how tools are defined and called
- [ ] Know how to work with dictionaries
- [ ] Understand iteration and loops

### Connect to Your Goal

**Building RAG Systems**: Agents are the "brain" of advanced RAG:

```
Basic RAG:
  Query → Retrieve → Generate → Answer
  (Simple, no reasoning)

Agentic RAG:
  Query → Agent thinks "What info do I need?"
        → Retrieves relevant docs
        → Agent thinks "Is this enough?"
        → Maybe retrieves more
        → Agent thinks "Now I can answer"
        → Generates answer with citations
  (Smart, adaptive retrieval)
```

Agents enable:
- **Multi-step retrieval** - "This doc mentions X, let me search for X too"
- **Query decomposition** - Breaking complex questions into sub-queries
- **Self-correction** - "This doesn't look right, let me try again"

### Key Insight: Agents vs Chains

```
Chain (Predetermined Steps):
  Step 1 → Step 2 → Step 3 → Done
  Always the same path, no matter what.

Agent (Dynamic Decisions):
  Think → Maybe Step 1 → Think → Maybe Step 3 → Think → Done
  Path depends on the problem and intermediate results.
```

### Warm-Up Activity

Before coding, trace through this agent scenario:

**User Query**: "What's the population of the capital of France?"

Write out the ReAct steps:

1. **Thought 1**: _____________________
2. **Action 1**: _____________________ (which tool?)
3. **Observation 1**: _____________________
4. **Thought 2**: _____________________
5. **Action 2**: _____________________ (which tool?)
6. **Observation 2**: _____________________
7. **Final Answer**: _____________________

---

**Ready?** Now proceed to `04_basic_agents.py` and implement the functions!
