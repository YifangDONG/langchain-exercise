"""
Test fixtures and utilities for pytest
"""
import os
from typing import Generator, Any
from unittest.mock import Mock, AsyncMock, MagicMock

import pytest
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.outputs import Generation, LLMResult


@pytest.fixture
def mock_llm() -> Mock:
    """
    Create a mock LLM for testing.
    
    Returns:
        Mock LLM object with common methods
    """
    mock = Mock(spec=BaseChatModel)
    
    # Set up invoke method
    mock.invoke.return_value = AIMessage(content="Mock response from LLM")
    
    # Set up stream method
    def mock_stream(messages, **kwargs):
        yield AIMessage(content="Mock ")
        yield AIMessage(content="streamed ")
        yield AIMessage(content="response")
    
    mock.stream.side_effect = mock_stream
    
    # Set up batch method
    mock.batch.return_value = [
        AIMessage(content=f"Response to prompt {i+1}") for i in range(3)
    ]
    
    return mock


@pytest.fixture
def mock_async_llm() -> AsyncMock:
    """
    Create a mock async LLM for testing.
    
    Returns:
        AsyncMock LLM object
    """
    mock = AsyncMock(spec=BaseLLM)
    mock.ainvoke.return_value = AIMessage(content="Mock async response")
    return mock


@pytest.fixture
def sample_messages():
    """
    Provide sample message sequences for testing.
    
    Returns:
        Dictionary of message lists
    """
    return {
        "simple": [
            HumanMessage(content="Hello"),
        ],
        "with_system": [
            SystemMessage(content="You are a helpful assistant."),
            HumanMessage(content="Hello"),
        ],
        "conversation": [
            SystemMessage(content="You are a helpful assistant."),
            HumanMessage(content="What is 2+2?"),
            AIMessage(content="2+2 equals 4"),
            HumanMessage(content="What about 3+3?"),
            AIMessage(content="3+3 equals 6"),
        ],
    }


@pytest.fixture
def mock_tool():
    """
    Create a mock tool for agent testing.
    
    Returns:
        Mock tool object
    """
    tool = Mock()
    tool.name = "mock_tool"
    tool.description = "A mock tool for testing"
    tool.invoke.return_value = "Mock tool result"
    return tool


@pytest.fixture
def mock_tools():
    """
    Create multiple mock tools for agent testing.
    
    Returns:
        List of mock tools
    """
    calculator = Mock()
    calculator.name = "calculator"
    calculator.description = "Perform mathematical calculations"
    calculator.invoke.return_value = "42"
    
    weather = Mock()
    weather.name = "get_weather"
    weather.description = "Get weather information"
    weather.invoke.return_value = "Sunny, 72°F"
    
    search = Mock()
    search.name = "search"
    search.description = "Search for information"
    search.invoke.return_value = "Found 3 results"
    
    return [calculator, weather, search]


@pytest.fixture
def mock_agent():
    """
    Create a mock agent for testing.
    
    Returns:
        Mock agent object
    """
    agent = Mock()
    agent.invoke.return_value = AIMessage(content="Agent response")
    agent.stream.return_value = [
        {"type": "ai", "content": "Thinking..."},
        {"type": "tool", "name": "calculator", "input": "2+2"},
        {"type": "tool_result", "output": "4"},
    ]
    return agent


@pytest.fixture
def env_setup(monkeypatch):
    """
    Set up environment variables for testing.
    
    Args:
        monkeypatch: pytest's monkeypatch fixture
    """
    monkeypatch.setenv("LANGCHAIN_MOCK_MODE", "true")
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test-mock-key")
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-test-mock-key")


@pytest.fixture(autouse=True)
def reset_mocks():
    """Auto-reset all mocks between tests."""
    yield
    # Cleanup happens after each test


@pytest.fixture
def sample_pydantic_model():
    """
    Create a sample Pydantic model for structured output testing.
    
    Returns:
        Pydantic model class
    """
    from pydantic import BaseModel, Field
    
    class Person(BaseModel):
        name: str = Field(description="Person's name")
        age: int = Field(description="Person's age", ge=0, le=150)
        email: str = Field(description="Person's email address")
    
    return Person


@pytest.fixture
def capture_logs(caplog):
    """
    Fixture to capture and verify logs during testing.
    
    Args:
        caplog: pytest's caplog fixture
        
    Returns:
        Log capture object
    """
    return caplog
