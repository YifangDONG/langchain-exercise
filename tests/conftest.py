"""
Shared pytest configuration and fixtures
"""
import pytest
from unittest.mock import Mock

# Import fixtures from utils
from src.utils.test_fixtures import (
    mock_llm,
    mock_async_llm,
    sample_messages,
    mock_tool,
    mock_tools,
    mock_agent,
    env_setup,
    reset_mocks,
    sample_pydantic_model,
    capture_logs,
)

# Re-export fixtures so they're available to all tests
__all__ = [
    "mock_llm",
    "mock_async_llm",
    "sample_messages",
    "mock_tool",
    "mock_tools",
    "mock_agent",
    "env_setup",
    "reset_mocks",
    "sample_pydantic_model",
    "capture_logs",
]
