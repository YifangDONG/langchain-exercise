# Concept Guide: Tool Definition

## Key Concepts

1. **Tools are callable functions** - Agents use them to interact with external systems
2. **Docstrings become schemas** - Args and Returns describe parameters for the LLM
3. **Type hints matter** - LangChain uses them for validation and schema generation
4. **Tools are registered** - Pass a list of tools to agents

## Visual: From Function to Tool

```
┌─────────────────────────────────────────────────────────────┐
│                  TOOL DEFINITION FLOW                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   @tool                          LLM sees:                  │
│   def get_weather(location: str):  • name: get_weather       │
│       """Get weather..."""    ──▶  • description: from doc   │
│       Args:                        • parameters: from        │
│         location: City name          type hints + docstring   │
│       Returns:                                               │
│         Weather description                                  │
│                                                              │
│   Schema is auto-generated → Agent can reason about when    │
│   and how to call the tool                                   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Code Example

```python
from langchain_core.tools import tool

@tool
def get_weather(location: str) -> str:
    """Get the current weather for a location.

    Args:
        location: City name

    Returns:
        Weather description
    """
    return f"The weather in {location} is sunny and 72°F"

@tool
def calculate(expression: str) -> float:
    """Evaluate a mathematical expression."""
    return eval(expression)

# Create a registry of tools
tools = [get_weather, calculate]

# Make them available to agents
agent = create_agent(model, tools)
```

## Tool Organization

- One tool = one focused capability
- Clear docstrings improve agent tool choice
- Type hints enable automatic schema generation

## Teach-Back

Explain in your own words:
1. Why is the docstring important for a tool?
2. What would happen if you used `location: str` but didn't document it?
3. How does the agent know which tool to call?
