"""
Utility helpers for LangChain exercises
"""
from typing import Any, List

from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, SystemMessage


def format_messages(messages: List[BaseMessage]) -> str:
    """
    Format a list of messages for display.
    
    Args:
        messages: List of LangChain messages
        
    Returns:
        Formatted string representation of messages
    """
    formatted = []
    for msg in messages:
        if isinstance(msg, SystemMessage):
            formatted.append(f"[SYSTEM]: {msg.content}")
        elif isinstance(msg, HumanMessage):
            formatted.append(f"[USER]: {msg.content}")
        elif isinstance(msg, AIMessage):
            formatted.append(f"[ASSISTANT]: {msg.content}")
        else:
            formatted.append(f"[{msg.__class__.__name__.upper()}]: {msg.content}")
    return "\n".join(formatted)


def truncate_text(text: str, max_length: int = 100) -> str:
    """
    Truncate text to max length with ellipsis.
    
    Args:
        text: Text to truncate
        max_length: Maximum length before truncation
        
    Returns:
        Truncated text
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."


def safe_get(data: dict, key: str, default: Any = None) -> Any:
    """
    Safely get value from dictionary with default.
    
    Args:
        data: Dictionary to query
        key: Key to retrieve
        default: Default value if key not found
        
    Returns:
        Value from dictionary or default
    """
    return data.get(key, default)


def parse_tool_calls(response: Any) -> List[dict]:
    """
    Parse tool calls from model response.
    
    Args:
        response: Model response object
        
    Returns:
        List of parsed tool calls
    """
    tool_calls = []
    if hasattr(response, "tool_calls"):
        tool_calls = response.tool_calls
    return tool_calls
