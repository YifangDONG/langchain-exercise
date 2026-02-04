# Exercise 06: Advanced Tools - CONNECTIONS

## Before You Start (5 minutes)

### What Do You Already Know?

Take a moment to reflect on these questions:

1. **Have you used apps with user roles?** (Admin, User, Guest)
   - Different users can do different things - that's permissions.

2. **Do you know what "context" means in programming?**
   - Information about the current situation that affects behavior.

3. **Have you worked with state management?** (Redux, session storage)
   - Keeping track of data that persists across operations.

### Real-World Analogy

Think of Advanced Tools like a **Smart Office Building**:

```
┌─────────────────────────────────────────────────────────────┐
│                THE SMART OFFICE ANALOGY                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  CONTEXT: "Who is using this and what's the situation?"     │
│                                                              │
│  Employee Badge (Context):                                   │
│  - Name: "Alice"                                            │
│  - Role: "Engineer"                                          │
│  - Department: "R&D"                                         │
│  - Security Level: 3                                         │
│                                                              │
│  TOOL FILTERING: "What can this person access?"             │
│                                                              │
│  Alice can use:                                              │
│  ✅ Code Repository (Engineering tool)                       │
│  ✅ Lab Equipment (R&D access)                               │
│  ✅ Meeting Rooms (Everyone)                                 │
│  ❌ Financial Systems (Finance only)                         │
│  ❌ Executive Suite (Level 5 required)                       │
│                                                              │
│  TOOL STATE: "What has happened during this session?"       │
│                                                              │
│  - Lab equipment last calibrated: 2 hours ago               │
│  - Alice's last query: "protein analysis"                   │
│  - Current project: "Project Alpha"                         │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Why Context Matters

```
Without Context:
  User: "Delete the production database"
  Tool: *deletes database*
  Result: DISASTER 💥

With Context:
  User: "Delete the production database"
  Context: user_role="junior_dev", environment="production"
  Tool: *checks permissions*
  Result: "You don't have permission to delete production databases"
  
  User: "Delete the test database"  
  Context: user_role="junior_dev", environment="test"
  Tool: *checks permissions*
  Result: "Test database deleted successfully"
```

### Prerequisite Checklist

Before starting this exercise, make sure you:

- [ ] Completed Exercises 01-05
- [ ] Understand Python dataclasses
- [ ] Know about dependency injection patterns
- [ ] Understand basic access control concepts

### Connect to Your Goal

**Building RAG Systems**: Advanced tools enable:

1. **Multi-tenant RAG** - Different users see different documents
2. **Permission-aware retrieval** - "Only search docs user has access to"
3. **Context-aware responses** - "Use user's department context"
4. **Stateful conversations** - "Remember what we discussed"

### The Context Pattern

```python
@dataclass
class RAGContext:
    """Context for RAG tool operations."""
    user_id: str
    user_role: str
    allowed_collections: List[str]
    conversation_id: str
    retrieved_docs: List[str] = field(default_factory=list)

# Tool uses context for filtering
@tool
def search_documents(query: str, context: RAGContext) -> List[str]:
    """Search documents user has access to."""
    # Only search collections user can access
    results = vector_db.search(
        query=query,
        collections=context.allowed_collections  # Filtered by context!
    )
    # Track what we retrieved
    context.retrieved_docs.extend(results)
    return results
```

### Dynamic Tool Selection

```
User Query: "Show me the financial projections"

Context: {role: "engineer"}
Available Tools: [code_search, docs_search, api_docs]
→ No financial tools available for this role

Context: {role: "finance_manager"}  
Available Tools: [financial_reports, budget_tools, projections]
→ Financial tools now available!
```

### Warm-Up Activity

Before coding, design a context-aware RAG system:

**Scenario**: A company knowledge base with different access levels

1. **What context fields would you need?**
   - user_id: _____
   - role: _____
   - department: _____
   - other: _____

2. **How would you filter search results by context?**
   - _____________________

3. **What state would you track during a conversation?**
   - _____________________

---

**Ready?** Now proceed to `06_advanced_tools.py` and implement the functions!
