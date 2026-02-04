# Exercise 03: Tool Definition - CONNECTIONS

## Before You Start (5 minutes)

### What Do You Already Know?

Take a moment to reflect on these questions:

1. **Have you ever used a calculator app on your phone?**
   - That's a "tool" - a function that does something specific.

2. **Do you know what an API endpoint does?**
   - Tools are like internal APIs that the AI can call.

3. **Have you documented a function with docstrings?**
   - Tool definitions rely heavily on good documentation.

### Real-World Analogy

Think of Tools like a **Swiss Army Knife for AI**:

```
┌─────────────────────────────────────────────────────────────┐
│                  THE SWISS ARMY KNIFE ANALOGY                │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  The AI (GPT/Claude) is like a very smart person who:       │
│  - Can reason and understand language                        │
│  - Can explain concepts and write text                       │
│  - BUT cannot actually DO things in the real world          │
│                                                              │
│  Tools are the "attachments" that let the AI:               │
│                                                              │
│  🔧 calculator  = The blade - does precise calculations     │
│  🌤️ weather     = The thermometer - checks external data    │
│  🔍 search      = The magnifying glass - finds information  │
│  📧 email       = The pen - sends messages                  │
│  🗄️ database    = The storage - saves/retrieves data        │
│                                                              │
│  The AI decides WHICH tool to use and HOW to use it.        │
│  The tool does the actual work.                              │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Why Can't AI Just "Do Things"?

```
Without Tools:
  User: "What's 847293 × 938472?"
  AI: "Let me calculate... approximately 795 billion" (might be wrong!)

With Tools:
  User: "What's 847293 × 938472?"
  AI: "I'll use the calculator tool"
  Tool: calculate("847293 * 938472") → 795,087,389,256
  AI: "The answer is 795,087,389,256" (guaranteed correct!)
```

### Prerequisite Checklist

Before starting this exercise, make sure you:

- [ ] Completed Exercises 01-02
- [ ] Understand Python decorators (`@decorator`)
- [ ] Know how to write good docstrings
- [ ] Understand type hints (str, int, List, etc.)

### Connect to Your Goal

**Building RAG Systems**: Tools are essential for RAG because:
1. **Retrieval Tool** - Searches your vector database for relevant documents
2. **Search Tool** - Fetches real-time information from the web
3. **Database Tool** - Queries structured data sources
4. **File Tool** - Reads and processes documents

In a RAG system, the retrieval step IS a tool call!

### The Tool Schema Connection

```python
@tool
def search_documents(query: str, top_k: int = 5) -> List[str]:
    """Search the knowledge base for relevant documents.
    
    Args:
        query: The search query
        top_k: Number of results to return
        
    Returns:
        List of relevant document chunks
    """
    # This becomes a RAG retrieval tool!
```

The `@tool` decorator automatically creates a schema that tells the AI:
- What the tool does (from docstring)
- What parameters it needs (from type hints)
- What it returns (from return type)

### Warm-Up Activity

Before coding, design a tool in plain English:

1. **Tool Name**: `search_knowledge_base`
2. **What it does**: _____________________
3. **Parameters needed**: _____________________
4. **What it returns**: _____________________
5. **When would an AI use this?**: _____________________

Think about error cases:
- What if the search returns no results?
- What if the query is empty?

---

**Ready?** Now proceed to `03_tool_definition.py` and implement the functions!
