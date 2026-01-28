"""
Mock data and fixtures for testing
"""
from typing import List

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


# Sample conversations
SAMPLE_CONVERSATION = [
    SystemMessage(content="You are a helpful AI assistant."),
    HumanMessage(content="What is 2 + 2?"),
    AIMessage(content="2 + 2 equals 4."),
    HumanMessage(content="What about 3 + 5?"),
    AIMessage(content="3 + 5 equals 8."),
]

WEATHER_CONVERSATION = [
    SystemMessage(content="You are a weather assistant. Provide helpful weather information."),
    HumanMessage(content="What's the weather in New York?"),
    AIMessage(content="I need to check the weather data for New York."),
]

# Sample prompts
SIMPLE_PROMPTS = [
    "What is machine learning?",
    "Explain photosynthesis",
    "How do I learn Python?",
    "What is the capital of France?",
    "Tell me about climate change",
]

COMPLEX_PROMPTS = [
    "Compare machine learning and deep learning, highlighting key differences and use cases.",
    "Design a system for a weather forecasting application using microservices.",
    "Explain quantum computing and its potential impact on cryptography.",
]

# Tool definitions
TOOL_DEFINITIONS = {
    "calculator": {
        "name": "calculator",
        "description": "Perform basic mathematical operations",
        "parameters": {
            "type": "object",
            "properties": {
                "operation": {"type": "string", "description": "Math operation: add, subtract, multiply, divide"},
                "a": {"type": "number", "description": "First number"},
                "b": {"type": "number", "description": "Second number"},
            },
            "required": ["operation", "a", "b"],
        },
    },
    "get_weather": {
        "name": "get_weather",
        "description": "Get current weather for a location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "City name"},
            },
            "required": ["location"],
        },
    },
    "search_web": {
        "name": "search_web",
        "description": "Search the web for information",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Search query"},
                "num_results": {"type": "integer", "description": "Number of results to return", "default": 5},
            },
            "required": ["query"],
        },
    },
}

# Mock responses
MOCK_RESPONSES = {
    "default": "This is a mock response from the language model.",
    "weather": "The weather in New York is partly cloudy with a temperature of 72°F.",
    "calculation": "The result of the calculation is 42.",
    "search": "Found 5 relevant web pages for your search query.",
}

# Sample structured outputs
SAMPLE_STRUCTURED_OUTPUTS = {
    "person": {
        "name": "Alice Johnson",
        "age": 30,
        "email": "alice@example.com",
    },
    "task": {
        "title": "Implement exercise 1",
        "description": "Set up model initialization",
        "status": "in_progress",
        "priority": "high",
    },
    "weather": {
        "location": "New York",
        "temperature": 72,
        "condition": "Partly Cloudy",
        "humidity": 65,
    },
}
