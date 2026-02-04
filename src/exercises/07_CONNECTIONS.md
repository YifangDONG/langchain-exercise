# Exercise 07: Structured Output - CONNECTIONS

## Before You Start (5 minutes)

### What Do You Already Know?

Take a moment to reflect on these questions:

1. **Have you ever parsed JSON from an API response?**
   - Structured output guarantees you get valid JSON every time.

2. **Do you know what data validation means?**
   - Checking that data matches expected format (email is valid, age is positive).

3. **Have you used TypeScript or type hints?**
   - Structured output enforces types at the AI response level.

### Real-World Analogy

Think of Structured Output like an **Order Form**:

```
┌─────────────────────────────────────────────────────────────┐
│                  THE ORDER FORM ANALOGY                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  WITHOUT STRUCTURED OUTPUT (Free-form text):                │
│                                                              │
│  Customer says: "I'd like 3 of those blue widgets,          │
│  maybe 5 actually, to 123 Main St, oh and my name           │
│  is John... or was it 4 widgets?"                           │
│                                                              │
│  → Hard to parse, ambiguous, might miss info                │
│                                                              │
│  WITH STRUCTURED OUTPUT (Order form):                        │
│                                                              │
│  ┌──────────────────────────────────────┐                   │
│  │ Name:     [John Smith          ]     │                   │
│  │ Quantity: [4                   ]     │                   │
│  │ Color:    [Blue ▼              ]     │                   │
│  │ Address:  [123 Main St         ]     │                   │
│  │ Email:    [john@email.com      ]     │                   │
│  └──────────────────────────────────────┘                   │
│                                                              │
│  → Clear fields, validated, complete                         │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Why This Matters

```python
# WITHOUT structured output:
response = model.invoke("Extract the person's info from: John is 25")
# response.content = "The person is John and he is 25 years old"
# response.content = "Name: John, Age: 25"  
# response.content = "John (25)"
# 🤷 Who knows what format you'll get?

# WITH structured output:
class Person(BaseModel):
    name: str
    age: int

response = model.with_structured_output(Person).invoke(...)
# response = Person(name="John", age=25)
# ✅ ALWAYS this exact format, guaranteed!
```

### Prerequisite Checklist

Before starting this exercise, make sure you:

- [ ] Completed Exercises 01-06
- [ ] Understand Python dataclasses or Pydantic models
- [ ] Know basic validation concepts
- [ ] Understand type hints

### Connect to Your Goal

**Building RAG Systems**: Structured output is essential for:

1. **Citation Extraction** - Force the model to cite sources properly
2. **Metadata Generation** - Extract structured info from documents
3. **Query Analysis** - Parse user intent into structured format
4. **Response Formatting** - Ensure consistent output format

### RAG Structured Output Examples

```python
# Force citations in responses
class RAGResponse(BaseModel):
    answer: str
    citations: List[Citation]
    confidence: float
    
class Citation(BaseModel):
    source_id: str
    quote: str
    relevance_score: float

# Extract structured info from documents
class DocumentMetadata(BaseModel):
    title: str
    author: Optional[str]
    date: Optional[date]
    topics: List[str]
    summary: str

# Parse user queries
class ParsedQuery(BaseModel):
    intent: Literal["search", "summarize", "compare", "explain"]
    entities: List[str]
    time_range: Optional[str]
    filters: Dict[str, str]
```

### The Validation Chain

```
User Input → Model → Pydantic Validation → Structured Output
                           ↓
                    If invalid:
                    Retry with feedback
                           ↓
                    Still invalid:
                    Raise ValidationError
```

### Warm-Up Activity

Before coding, design a structured output for RAG:

**Task**: Design a `SearchResult` model for RAG retrieval

```python
class SearchResult(BaseModel):
    # What fields would you need?
    # 1. _____________________
    # 2. _____________________
    # 3. _____________________
    # 4. _____________________
```

Think about:
- What makes a good search result?
- What validation rules would you add?
- How would the model populate this?

---

**Ready?** Now proceed to `07_structured_output.py` and implement the functions!
