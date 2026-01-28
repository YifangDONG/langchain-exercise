"""
Tests for Exercise 04: Basic Agents & ReAct Pattern
==================================================
"""
import pytest
from langchain_core.messages import HumanMessage


class TestBasicAgents:
    """Test Exercise 04: Basic Agents & ReAct Pattern"""
    
    @pytest.mark.beginner
    @pytest.mark.unit
    def test_create_basic_agent(self, mock_llm, mock_tools):
        """Test creating basic agent with model and tools."""
        # TODO: Import create_basic_agent
        # TODO: Call create_basic_agent with mock_llm and mock_tools
        # TODO: Assert returns agent object
        # TODO: Assert agent has invoke method
        pass
    
    @pytest.mark.beginner
    @pytest.mark.unit
    def test_invoke_agent_with_messages(self, mock_llm, mock_tools):
        """Test invoking agent with messages."""
        # TODO: Import create_basic_agent and invoke_agent
        # TODO: Create agent
        # TODO: Invoke with simple messages
        # TODO: Assert returns dict with response
        pass
    
    @pytest.mark.beginner
    @pytest.mark.unit
    def test_invoke_agent_respects_max_iterations(self, mock_llm, mock_tools):
        """Test that invoke_agent stops after max iterations."""
        # TODO: Import invoke_agent
        # TODO: Create agent
        # TODO: Call with max_iterations=3
        # TODO: Assert execution stops at or before limit
        pass
    
    @pytest.mark.beginner
    @pytest.mark.unit
    def test_extract_agent_steps(self, mock_llm, mock_tools):
        """Test extracting reasoning and action steps."""
        # TODO: Import create_basic_agent, invoke_agent, extract_agent_steps
        # TODO: Create and invoke agent
        # TODO: Call extract_agent_steps on response
        # TODO: Assert returns list of steps
        # TODO: Assert steps have type, content fields
        pass
    
    @pytest.mark.beginner
    @pytest.mark.unit
    def test_stream_agent_response(self, mock_llm, mock_tools):
        """Test streaming agent response."""
        # TODO: Import stream_agent_response
        # TODO: Create agent
        # TODO: Call stream_agent_response
        # TODO: Assert returns iterator
        # TODO: Assert can iterate over streamed content
        pass
    
    @pytest.mark.beginner
    @pytest.mark.unit
    def test_format_agent_response(self, mock_llm, mock_tools):
        """Test formatting agent response for display."""
        # TODO: Import create_basic_agent, invoke_agent, format_agent_response
        # TODO: Create and invoke agent
        # TODO: Call format_agent_response
        # TODO: Assert returns string
        # TODO: Assert formatted response is readable
        pass
    
    @pytest.mark.beginner
    @pytest.mark.unit
    def test_count_agent_iterations(self, mock_llm, mock_tools):
        """Test counting agent iterations."""
        # TODO: Import count_agent_iterations
        # TODO: Get agent response
        # TODO: Call count_agent_iterations
        # TODO: Assert returns integer >= 0
        pass
    
    @pytest.mark.beginner
    @pytest.mark.unit
    def test_verify_agent_answer(self, mock_llm, mock_tools):
        """Test verifying agent reached answer."""
        # TODO: Import verify_agent_answer
        # TODO: Get successful agent response
        # TODO: Call verify_agent_answer
        # TODO: Assert returns True for valid answer
        pass
    
    @pytest.mark.beginner
    @pytest.mark.integration
    def test_complete_agent_workflow(self, mock_llm, mock_tools):
        """Test complete agent workflow from creation to result."""
        # TODO: Create agent
        # TODO: Invoke with task
        # TODO: Extract steps
        # TODO: Format response
        # TODO: Verify completion
        # TODO: Assert workflow is consistent
        pass
