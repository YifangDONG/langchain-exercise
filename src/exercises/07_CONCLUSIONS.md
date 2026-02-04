# Exercise 07: Structured Output - CONCLUSIONS

## Congratulations!

You've learned to force consistent, validated output from language models.

---

## Skills Checklist

### I Can Now...

- [ ] Define Pydantic schemas for LLM output
- [ ] Use `with_structured_output()` for guaranteed formats
- [ ] Add validation rules with Pydantic validators
- [ ] Handle batch structured output
- [ ] Implement parse-with-retry for unreliable outputs
- [ ] Generate schema prompts automatically

### Key Takeaways

1. **Structured output eliminates parsing** - No more regex nightmares
2. **Pydantic validates automatically** - Catch bad output early
3. **Schemas are self-documenting** - Clear contracts for data
4. **Retry improves reliability** - Sometimes models need a second chance

---

## Reflection Questions

1. **Why is structured output critical for production systems?**
   - Your answer: _____________________

2. **What happens when model output doesn't match the schema?**
   - Your answer: _____________________

3. **How would you design a schema for RAG citations?**
   - Your answer: _____________________

---

## Common Mistakes to Avoid

| Mistake | Better Approach |
|---------|-----------------|
| Complex nested schemas | Start simple, add complexity as needed |
| No default values | Provide defaults for optional fields |
| Missing validation | Add Field constraints and validators |
| Ignoring parse failures | Implement retry logic |

---

## Mini-Project Challenge

### Project: RAG Response with Citations

Design a structured output for RAG responses:

```python
from pydantic import BaseModel, Field
from typing import List
from enum import Enum

class ConfidenceLevel(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

class Citation(BaseModel):
    document_id: str
    quote: str = Field(..., min_length=10)
    relevance: float = Field(..., ge=0, le=1)

class RAGResponse(BaseModel):
    answer: str = Field(..., min_length=10)
    citations: List[Citation] = Field(..., min_items=1)
    confidence: ConfidenceLevel
    follow_up_questions: List[str] = Field(default_factory=list)
    
    @validator('citations')
    def citations_not_empty(cls, v):
        if not v:
            raise ValueError("At least one citation required")
        return v
```

---

## Connect to RAG

```
Structured Output in RAG:

┌─────────────────────────────────────────────────────────────┐
│  WITHOUT STRUCTURED OUTPUT:                                  │
│                                                              │
│  Model: "The refund policy says you can return items        │
│          within 30 days. Source: policy doc."               │
│                                                              │
│  Problem: How do you extract the citation? Regex? Hope?     │
├─────────────────────────────────────────────────────────────┤
│  WITH STRUCTURED OUTPUT:                                     │
│                                                              │
│  RAGResponse(                                                │
│    answer="You can return items within 30 days",            │
│    citations=[                                               │
│      Citation(                                               │
│        document_id="policy_v2.pdf",                         │
│        quote="Returns accepted within 30 days...",          │
│        relevance=0.95                                        │
│      )                                                       │
│    ],                                                        │
│    confidence=ConfidenceLevel.HIGH                          │
│  )                                                           │
│                                                              │
│  Benefit: Programmatically access any field! ✅             │
└─────────────────────────────────────────────────────────────┘
```

---

## What's Next?

**Exercise 08: System Prompts** - Master prompt engineering for better results.

Before moving on:
- [ ] All tests pass for Exercise 07
- [ ] You can define and validate Pydantic schemas
- [ ] You understand parse-with-retry patterns

---

## Quick Reference Card

```python
from pydantic import BaseModel, Field, validator
from langchain import init_chat_model

class Person(BaseModel):
    name: str = Field(..., min_length=1)
    age: int = Field(..., ge=0, le=150)
    email: str
    
    @validator('email')
    def valid_email(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email')
        return v

# Get structured output
model = init_chat_model("openai/gpt-4-turbo")
structured_model = model.with_structured_output(Person)
result = structured_model.invoke("John is 25, email john@test.com")
# result is a Person instance!

print(result.name)  # "John"
print(result.age)   # 25
```

---

**Structured output mastered! Time for prompt engineering!**
