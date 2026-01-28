"""
Tests for Exercise 02: Messages & Conversation
==============================================
"""
import pytest
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, BaseMessage


class TestMessages:
    """Test Exercise 02: Messages & Conversation"""
    
    @pytest.mark.beginner
    @pytest.mark.unit
    def test_create_system_message(self):
        """Test creating system message."""
        # TODO: Import create_system_message from src.exercises.02_messages
        # TODO: Call create_system_message with content
        # TODO: Assert returns SystemMessage
        # TODO: Assert content is preserved
        pass
    
    @pytest.mark.beginner
    @pytest.mark.unit
    def test_create_user_message(self):
        """Test creating user/human message."""
        # TODO: Import create_user_message
        # TODO: Call with content
        # TODO: Assert returns HumanMessage
        # TODO: Assert content is correct
        pass
    
    @pytest.mark.beginner
    @pytest.mark.unit
    def test_create_assistant_message(self):
        """Test creating assistant/AI message."""
        # TODO: Import create_assistant_message
        # TODO: Call with content
        # TODO: Assert returns AIMessage
        # TODO: Assert content is correct
        pass
    
    @pytest.mark.beginner
    @pytest.mark.unit
    def test_build_conversation(self):
        """Test building conversation message sequence."""
        # TODO: Import build_conversation
        # TODO: Call with system prompt and alternating messages
        # TODO: Assert returns list of messages
        # TODO: Assert correct order (system, user, assistant, user, assistant)
        # TODO: Assert all message types are correct
        pass
    
    @pytest.mark.beginner
    @pytest.mark.unit
    def test_build_conversation_with_empty_messages(self):
        """Test building conversation with no user messages."""
        # TODO: Call build_conversation with empty lists
        # TODO: Assert returns list with just system message
        pass
    
    @pytest.mark.beginner
    @pytest.mark.unit
    def test_format_conversation(self):
        """Test formatting conversation for display."""
        # TODO: Import format_conversation
        # TODO: Create conversation messages
        # TODO: Call format_conversation
        # TODO: Assert returns string
        # TODO: Assert includes role prefixes (USER:, ASSISTANT:, SYSTEM:)
        pass
    
    @pytest.mark.beginner
    @pytest.mark.unit
    def test_add_to_conversation(self):
        """Test adding user-assistant exchange to history."""
        # TODO: Import add_to_conversation
        # TODO: Create initial conversation
        # TODO: Add new exchange
        # TODO: Assert original not modified
        # TODO: Assert returned list has new messages
        pass
    
    @pytest.mark.beginner
    @pytest.mark.unit
    def test_get_conversation_context(self):
        """Test getting recent conversation context."""
        # TODO: Import get_conversation_context
        # TODO: Create long conversation
        # TODO: Call with max_messages=5
        # TODO: Assert returns recent messages
        # TODO: Assert system message preserved
        # TODO: Assert respects max_messages limit
        pass
    
    @pytest.mark.beginner
    @pytest.mark.integration
    def test_conversation_workflow(self):
        """Test complete conversation workflow."""
        # TODO: Create system message
        # TODO: Build conversation with exchanges
        # TODO: Add more exchanges
        # TODO: Format for display
        # TODO: Get recent context
        # TODO: Verify workflow consistency
        pass
