# Exercise 06: Advanced Tools - CONCLUSIONS

## Congratulations!

You've mastered context-aware tools with state management and permissions.

---

## Skills Checklist

### I Can Now...

- [ ] Create tools that use runtime context
- [ ] Filter tools dynamically based on permissions
- [ ] Manage tool state across invocations
- [ ] Implement permission checking for tools
- [ ] Access persistent memory from tools
- [ ] Create middleware for tool filtering

### Key Takeaways

1. **Context enables personalization** - Same tool, different behavior per user
2. **State enables memory** - Tools can remember across calls
3. **Permissions enable security** - Not all users can do all things
4. **Dynamic filtering** - Right tools for the right situation

---

## Reflection Questions

1. **Why is context important for multi-tenant RAG?**
   - Your answer: _____________________

2. **How would you implement document-level permissions?**
   - Your answer: _____________________

3. **When should state be stored in tools vs externally?**
   - Your answer: _____________________

---

## Common Mistakes to Avoid

| Mistake | Better Approach |
|---------|-----------------|
| Hardcoded permissions | Use context-based permission checks |
| Global state | Scope state to user/session |
| No access control | Always verify permissions |
| Context not thread-safe | Use proper isolation |

---

## Mini-Project Challenge

### Project: Multi-Tenant RAG Tool

Build a retrieval tool that respects user permissions:

```python
@dataclass
class UserContext:
    user_id: str
    role: str
    department: str
    allowed_collections: List[str]

@tool
def secure_search(
    query: str,
    context: UserContext
) -> List[Document]:
    """
    Search documents the user has access to.
    
    Filters results based on user's allowed_collections.
    """
    # Your implementation here
    pass
```

---

## Connect to RAG

```
Context-Aware RAG:

┌─────────────────────────────────────────────────────────────┐
│  USER: Sales Manager, West Region                            │
│  ├── Can access: Sales docs, West region data               │
│  └── Cannot access: HR docs, East region data               │
│                                                              │
│  Query: "Show me Q3 sales performance"                       │
│                                                              │
│  Context-Aware Retrieval:                                    │
│  1. Get user context → {role: "sales", region: "west"}      │
│  2. Filter collections → ["sales_docs", "west_reports"]     │
│  3. Search only allowed collections                          │
│  4. Return results user can see                              │
│                                                              │
│  Without Context: User might see confidential East data! ❌  │
│  With Context: User sees only their authorized data ✅       │
└─────────────────────────────────────────────────────────────┘
```

---

## What's Next?

**Exercise 07: Structured Output** - Force consistent, parseable output from models.

Before moving on:
- [ ] All tests pass for Exercise 06
- [ ] You understand context and state management
- [ ] You can implement permission-based filtering

---

## Quick Reference Card

```python
from dataclasses import dataclass
from typing import List

@dataclass
class ToolContext:
    user_id: str
    session_id: str
    permissions: List[str]
    
# Context-aware tool
def create_tool_with_context(context: ToolContext):
    @tool
    def search(query: str) -> List[str]:
        """Search with user context."""
        if "search" not in context.permissions:
            return ["Permission denied"]
        # Perform search with context filtering
        return results
    return search

# Dynamic tool selection
def select_tools(context: ToolContext) -> List:
    available = []
    if "search" in context.permissions:
        available.append(search_tool)
    if "write" in context.permissions:
        available.append(write_tool)
    return available
```

---

**Advanced tools complete! On to structured output!**
