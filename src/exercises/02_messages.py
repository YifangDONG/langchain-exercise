"""
Exercise 02: Messages & Conversation
====================================

LEVEL: Beginner

GOAL: Understand message types and build conversation history properly.

TODO:
1. Implement create_system_message() and create_user_message()
2. Implement build_conversation() to create a message sequence
3. Implement format_conversation() to format messages for display
4. Implement manage_conversation_history() to add messages and maintain context

CONCEPTS TO LEARN:
- Message types: SystemMessage, HumanMessage, AIMessage, ToolMessage
- Message content and properties
- Conversation history as list of messages
- Message formatting and serialization
- Context management in conversations

RESOURCES:
- LangChain docs: https://docs.langchain.com/oss/python/langchain/overview
- Related exercises: 01_model_basics, 04_basic_agents

HINTS:
- Import message types from langchain_core.messages
- Conversations are just lists of message objects
- Each message has a content property
- Message types determine role in conversation
"""

from typing import Any, List, Dict
from langchain_core.messages import BaseMessage, SystemMessage, HumanMessage, AIMessage


def create_system_message(content: str) -> SystemMessage:
    """
    TODO: Create a system message.
    
    Requirements:
    - Return a SystemMessage with the given content
    - System messages define the assistant's behavior/role
    
    Args:
        content: System prompt content
        
    Returns:
        SystemMessage object
    """
    pass


def create_user_message(content: str) -> HumanMessage:
    """
    TODO: Create a user/human message.
    
    Requirements:
    - Return a HumanMessage with the given content
    - Human messages represent user input
    
    Args:
        content: User message content
        
    Returns:
        HumanMessage object
    """
    pass


def create_assistant_message(content: str) -> AIMessage:
    """
    TODO: Create an assistant/AI message.
    
    Requirements:
    - Return an AIMessage with the given content
    - AI messages represent assistant responses
    
    Args:
        content: Assistant message content
        
    Returns:
        AIMessage object
    """
    pass


def build_conversation(
    system_prompt: str,
    user_messages: List[str],
    assistant_responses: List[str]
) -> List[BaseMessage]:
    """
    TODO: Build a complete conversation message sequence.
    
    Requirements:
    - Start with system message
    - Alternate user and assistant messages
    - Maintain proper order
    - Return list of messages
    
    Args:
        system_prompt: System message content
        user_messages: List of user messages
        assistant_responses: List of assistant responses (same length as user_messages)
        
    Returns:
        List of message objects in conversation order
    """
    pass


def format_conversation(messages: List[BaseMessage]) -> str:
    """
    TODO: Format conversation for display.
    
    Requirements:
    - Format each message with role prefix (USER:, ASSISTANT:, SYSTEM:)
    - Join messages with newlines
    - Make conversation readable
    
    Args:
        messages: List of message objects
        
    Returns:
        Formatted conversation string
    """
    pass


def add_to_conversation(
    messages: List[BaseMessage],
    user_message: str,
    assistant_response: str
) -> List[BaseMessage]:
    """
    TODO: Add a user-assistant exchange to conversation history.
    
    Requirements:
    - Append user message
    - Append assistant response
    - Return updated conversation
    - Don't modify original list
    
    Args:
        messages: Current conversation history
        user_message: New user message
        assistant_response: New assistant response
        
    Returns:
        Updated conversation list
    """
    pass


def get_conversation_context(messages: List[BaseMessage], max_messages: int = 10) -> List[BaseMessage]:
    """
    TODO: Get recent conversation context.
    
    Requirements:
    - Keep system message if present
    - Get last N messages
    - Maintain chronological order
    
    Args:
        messages: Full conversation history
        max_messages: Maximum messages to return (excluding system)
        
    Returns:
        Recent conversation context
    """
    pass
