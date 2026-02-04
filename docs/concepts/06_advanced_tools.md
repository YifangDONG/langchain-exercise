# Concept Guide: Advanced Tools

## Key Concepts

1. **Tools can be composed** - One tool can call others or combine results
2. **Structured inputs/outputs** - Use Pydantic for complex arguments and return types
3. **Async tools** - Support I/O-bound tools with async def
4. **Tool choice** - Good naming and descriptions help the agent pick the right tool

## Visual: Tool Composition

```
┌─────────────────────────────────────────────────────────────┐
│                 ADVANCED TOOL PATTERNS                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   Single tool     get_weather("Paris") → "72°F"             │
│                                                              │
│   Composed        search_docs(query) → fetch_page(url) →     │
│                   summarize(content) → summary               │
│                                                              │
│   Structured      book_flight(origin, destination, date)     │
│   input             → FlightResult(confirmation_id, ...)    │
│                                                              │
│   Agent sees all tools; picks based on task and descriptions │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Code Example

```python
from langchain_core.tools import tool
from pydantic import BaseModel, Field

class SearchResult(BaseModel):
    title: str
    snippet: str
    url: str

@tool
def search_docs(query: str, max_results: int = 5) -> list[SearchResult]:
    """Search the document store. Use for factual questions.
    Args:
        query: Search query
        max_results: Maximum number of results (default 5)
    """
    # Implementation returns list of SearchResult
    return [...]

# Async tool for I/O
@tool
async def fetch_url(url: str) -> str:
    """Fetch raw content from a URL."""
    async with aiohttp.get(url) as resp:
        return await resp.text()
```

## Teach-Back

Explain in your own words:
1. When would you use a structured return type instead of a string?
2. Why might an agent need both search_docs and fetch_url?
3. What's the benefit of async tools?
