# Concept Guide: Tool Execution

## Key Concepts

1. **Agents invoke tools** - The runtime passes tool name + arguments and runs the tool
2. **Errors must be handled** - Invalid input or failures should return clear messages, not crash
3. **Tool results become ToolMessages** - So the agent can reason over what happened
4. **Retries help with flaky APIs** - Use backoff for transient failures

## Visual: Execution Flow

```
┌─────────────────────────────────────────────────────────────┐
│                  TOOL EXECUTION FLOW                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   Agent decides: get_weather(location="Paris")               │
│        │                                                     │
│        ▼                                                     │
│   Runtime looks up tool by name, validates args              │
│        │                                                     │
│        ▼                                                     │
│   execute_tool_safely(tool, input_data)                      │
│        │                                                     │
│        ├── Success → ToolMessage(content="72°F, sunny")      │
│        │                                                     │
│        └── Error   → ToolMessage(content="Error: ...")       │
│                      (agent can retry or explain to user)    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Code Example

```python
def execute_tool_safely(tool, input_data):
    try:
        return tool.invoke(input_data)
    except ValueError as e:
        return f"Invalid input: {e}"
    except Exception as e:
        return f"Tool error: {e}"

# Retry with backoff for flaky tools
def retry_with_backoff(func, max_retries=3):
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            wait_time = 2 ** attempt  # Exponential backoff
            if attempt < max_retries - 1:
                time.sleep(wait_time)
            else:
                raise
```

## Teach-Back

Explain in your own words:
1. Why return an error string instead of raising in the tool?
2. When is exponential backoff useful?
3. What should the agent do when it receives a ToolMessage with an error?
