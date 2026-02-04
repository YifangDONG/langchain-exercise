# Concept Guide: Structured Output

## Key Concepts

1. **LLM output is normally free text** - Unpredictable format, hard to parse
2. **Structured output guarantees a schema** - Pydantic models define shape and types
3. **Validation is automatic** - Invalid model output raises ValidationError
4. **Use for APIs and downstream code** - Get objects, not raw strings

## Visual: Unstructured vs Structured

```
┌─────────────────────────────────────────────────────────────┐
│                  UNSTRUCTURED vs STRUCTURED                   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   invoke(prompt)          with_structured_output(Person)     │
│        │                              │                      │
│        ▼                              ▼                      │
│   "Name: Alice,         Person(name="Alice",                │
│    Age: 30, ..."           age=30, email="a@b.com")          │
│   (string, may vary)      (validated object)                 │
│                                                              │
│   You parse by hand       You use result.name, result.age   │
│   or regex                Type-safe, IDE-friendly            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Code Example

```python
from pydantic import BaseModel, Field

class Person(BaseModel):
    name: str = Field(description="Person's full name")
    age: int = Field(description="Age in years", ge=0, le=150)
    email: str = Field(description="Email address")

# Get guaranteed structured output
result = model.with_structured_output(Person).invoke(prompt)
# result is a Person instance, not raw text
print(result.name, result.age)

# Validation catches bad output
try:
    result = model.with_structured_output(Person).invoke(prompt)
except ValidationError as e:
    print(f"Invalid output: {e}")
```

## Teach-Back

Explain in your own words:
1. When would you prefer structured output over plain invoke?
2. What does Field(ge=0, le=150) do?
3. What happens if the model returns "Name: Bob" but the schema expects name and age?
