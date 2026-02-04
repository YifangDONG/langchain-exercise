# Concept Guide: Messages

## Key Concepts

1. **Messages are the fundamental data structure** - Conversations are lists of messages
2. **Four core types** - SystemMessage, HumanMessage, AIMessage, ToolMessage
3. **System sets behavior** - Defines assistant personality and constraints
4. **History enables context** - Pass previous messages for multi-turn conversation

## Visual: Message Roles

```
┌─────────────────────────────────────────────────────────────┐
│                    CONVERSATION AS MESSAGES                  │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   SystemMessage   "You are a helpful assistant."             │
│        │          (sets tone, rules, personality)            │
│        ▼                                                      │
│   HumanMessage    "What is the capital of France?"           │
│        │          (user input)                               │
│        ▼                                                      │
│   AIMessage       "The capital of France is Paris."          │
│        │          (model response)                           │
│        ▼                                                      │
│   HumanMessage    "What about 3 + 3?"                        │
│        │                                                      │
│   AIMessage       "3 + 3 equals 6."                         │
│        │                                                      │
│   ToolMessage     "Weather in Paris: 72°F"  (tool result)   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Code Example

```python
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage,
    ToolMessage,
)

# System message sets the tone
system = SystemMessage("You are a helpful assistant.")

# Human message is user input
user = HumanMessage("What is the capital of France?")

# AI message is model response
assistant = AIMessage("The capital of France is Paris.")

# Tool message is tool execution result
tool_result = ToolMessage("Weather in Paris: 72°F")

# Conversation = list of messages
conversation = [
    system,
    HumanMessage("What is 2 + 2?"),
    AIMessage("2 + 2 equals 4."),
    HumanMessage("What about 3 + 3?"),
]

# Pass to model for continuation
response = model.invoke(conversation + [HumanMessage("And 4 + 4?")])
```

## Message Roles Summary

| Type   | Purpose                          |
|--------|----------------------------------|
| System | Defines assistant personality    |
| Human  | User queries and instructions    |
| AI     | Model responses and reasoning   |
| Tool   | Tool execution results           |

## Teach-Back

Explain in your own words:
1. Why do we pass conversation history when calling the model?
2. When would you use a ToolMessage?
3. What happens if you omit the SystemMessage?
