# Concept Guide: System Prompts

## Key Concepts

1. **System prompt defines behavior** - Personality, rules, and style for the assistant
2. **Chain of thought improves reasoning** - Ask for step-by-step thinking when needed
3. **Dynamic prompts** - Use templates and variables for domain-specific tasks
4. **Place system first** - Usually SystemMessage then conversation

## Visual: Prompt Layers

```
┌─────────────────────────────────────────────────────────────┐
│                    PROMPT LAYERS                             │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   SystemMessage (fixed or rarely changed)                    │
│   "You are a helpful math tutor. Explain step-by-step."      │
│        │                                                     │
│        ▼                                                     │
│   HumanMessage (user input)                                  │
│   "How do I solve quadratic equations?"                     │
│        │                                                     │
│        ▼                                                     │
│   Optional: Few-shot examples in system or earlier messages  │
│        │                                                     │
│        ▼                                                     │
│   Model response follows system instructions                 │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Code Example

```python
system_prompt = """You are a helpful math tutor.
- Explain concepts clearly
- Show step-by-step solutions
- Encourage the student"""

messages = [
    SystemMessage(system_prompt),
    HumanMessage("How do I solve quadratic equations?"),
]
response = model.invoke(messages)
```

### Chain of Thought

```python
prompt = """
Let's think through this step-by-step:
Question: {question}
1. Identify the key information
2. Break down the problem
3. Work through each part
4. Provide the final answer
"""
```

### Dynamic Prompts

```python
from string import Template
template = Template("You are an expert in $domain.\nAnswer: $question")
prompt = template.substitute(domain="machine learning", question="What is backpropagation?")
```

## Teach-Back

Explain in your own words:
1. Why put instructions in the system message instead of the user message?
2. When would you use a dynamic template for the system prompt?
3. What is "chain of thought" and why does it help?
