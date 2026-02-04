# Exercise 12: Advanced Workflows - CONNECTIONS

## Before You Start (5 minutes)

### What Do You Already Know?

Take a moment to reflect on these questions:

1. **Have you worked on a team project?**
   - Different people have different specialties and coordinate.

2. **Do you know how a company org chart works?**
   - Managers delegate to specialists, specialists report back.

3. **Have you used parallel processing or async?**
   - Running multiple things at once for efficiency.

### Real-World Analogy

Think of Multi-Agent Systems like a **Research Team**:

```
┌─────────────────────────────────────────────────────────────┐
│              THE RESEARCH TEAM ANALOGY                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Research Question: "What's the market potential for        │
│                      AI-powered education tools?"            │
│                                                              │
│  SUPERVISOR AGENT (Project Lead):                            │
│  "I'll coordinate this research project"                     │
│     │                                                        │
│     ├──▶ RESEARCHER AGENT: "Find market size data"          │
│     │         └──▶ Returns: "Market is $5B, growing 15%"    │
│     │                                                        │
│     ├──▶ ANALYST AGENT: "Analyze competitor landscape"      │
│     │         └──▶ Returns: "Top 5 competitors are..."      │
│     │                                                        │
│     ├──▶ WRITER AGENT: "Draft the report"                   │
│     │         └──▶ Returns: "Executive summary..."          │
│     │                                                        │
│     └──▶ REVIEWER AGENT: "Check for accuracy"               │
│               └──▶ Returns: "Approved with minor edits"      │
│                                                              │
│  FINAL OUTPUT: Complete market analysis report               │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Why Multiple Agents?

```
SINGLE AGENT (One person does everything):
┌─────────────────────────────────────────┐
│  Agent: "I need to research, analyze,   │
│          write, review... this is hard  │
│          to do all at once!"            │
│                                         │
│  Problems:                              │
│  - Context window overflow              │
│  - Jack of all trades, master of none   │
│  - No specialization                    │
│  - Serial execution (slow)              │
└─────────────────────────────────────────┘

MULTI-AGENT (Team of specialists):
┌─────────────────────────────────────────┐
│  Researcher: Expert at finding info     │
│  Analyst: Expert at data analysis       │
│  Writer: Expert at clear communication  │
│  Reviewer: Expert at quality control    │
│                                         │
│  Benefits:                              │
│  - Specialized system prompts           │
│  - Parallel execution (fast)            │
│  - Separation of concerns               │
│  - Easier to debug and improve          │
└─────────────────────────────────────────┘
```

### Prerequisite Checklist

Before starting this exercise, make sure you:

- [ ] Completed Exercises 01-11
- [ ] Understand async/await in Python
- [ ] Know about message passing patterns
- [ ] Have experience with concurrent programming concepts

### Connect to Your Goal

**Building RAG Systems**: Multi-agent RAG is state-of-the-art:

```
┌─────────────────────────────────────────────────────────────┐
│                  MULTI-AGENT RAG ARCHITECTURE                │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  User Query: "Compare our product to competitors"            │
│                                                              │
│  ORCHESTRATOR AGENT:                                         │
│  "I'll coordinate multiple retrieval sources"                │
│     │                                                        │
│     ├──▶ INTERNAL_RAG_AGENT: Search company docs            │
│     │         └──▶ "Our product features are..."            │
│     │                                                        │
│     ├──▶ COMPETITOR_RAG_AGENT: Search competitor info       │
│     │         └──▶ "Competitor A offers..."                 │
│     │                                                        │
│     ├──▶ MARKET_RAG_AGENT: Search market reports            │
│     │         └──▶ "Industry trends show..."                │
│     │                                                        │
│     └──▶ SYNTHESIS_AGENT: Combine all findings              │
│               └──▶ Final comparison report                   │
│                                                              │
│  All agents can run IN PARALLEL for speed!                   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Advanced RAG Patterns

```python
# Pattern 1: Parallel Retrieval
async def parallel_rag(query: str) -> str:
    # Run multiple retrievals in parallel
    results = await asyncio.gather(
        search_internal_docs(query),
        search_web(query),
        search_database(query),
    )
    return synthesize(results)

# Pattern 2: Hierarchical RAG
class HierarchicalRAG:
    supervisor: SupervisorAgent
    workers: Dict[str, WorkerAgent]
    
    def query(self, question: str):
        # Supervisor decides which workers to use
        plan = self.supervisor.plan(question)
        
        # Execute plan with appropriate workers
        results = []
        for task in plan.tasks:
            worker = self.workers[task.worker_type]
            result = worker.execute(task)
            results.append(result)
        
        # Supervisor synthesizes final answer
        return self.supervisor.synthesize(results)

# Pattern 3: Self-Correcting RAG
class SelfCorrectingRAG:
    retriever: RetrieverAgent
    generator: GeneratorAgent
    critic: CriticAgent
    
    def query(self, question: str):
        for attempt in range(3):
            docs = self.retriever.retrieve(question)
            answer = self.generator.generate(question, docs)
            
            # Critic checks the answer
            critique = self.critic.evaluate(question, answer, docs)
            
            if critique.is_acceptable:
                return answer
            
            # Retry with critique feedback
            question = f"{question}\n\nPrevious issues: {critique.issues}"
        
        return answer  # Best effort after 3 attempts
```

### Warm-Up Activity

Before coding, design a multi-agent RAG system:

**Scenario**: Customer support system that needs to answer complex questions

1. **What specialized agents would you create?**
   - Agent 1: _____________________ (role: _____)
   - Agent 2: _____________________ (role: _____)
   - Agent 3: _____________________ (role: _____)

2. **How would they communicate?**
   - _____________________

3. **What happens if one agent fails?**
   - _____________________

4. **What tasks can run in parallel?**
   - _____________________

---

**Ready?** Now proceed to `12_advanced_workflows.py` and implement the functions!
