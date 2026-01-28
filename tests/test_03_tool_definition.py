"""
Tests for Exercise 03: Tool Definition & Schemas
===============================================
"""
import pytest
from typing import Callable


class TestToolDefinition:
    """Test Exercise 03: Tool Definition & Schemas"""
    
    @pytest.mark.beginner
    @pytest.mark.unit
    def test_create_calculator_tool(self):
        """Test creating calculator tool with @tool decorator."""
        # TODO: Import create_calculator_tool
        # TODO: Call create_calculator_tool()
        # TODO: Assert returns callable
        # TODO: Assert tool has name attribute
        # TODO: Assert tool has description
        pass
    
    @pytest.mark.beginner
    @pytest.mark.unit
    def test_calculator_tool_add_operation(self):
        """Test calculator tool add operation."""
        # TODO: Get calculator tool
        # TODO: Call tool with operation='add', a=2, b=3
        # TODO: Assert returns 5
        pass
    
    @pytest.mark.beginner
    @pytest.mark.unit
    def test_calculator_tool_divide_by_zero(self):
        """Test calculator tool handles division by zero."""
        # TODO: Get calculator tool
        # TODO: Call with operation='divide', a=1, b=0
        # TODO: Assert handles error gracefully
        pass
    
    @pytest.mark.beginner
    @pytest.mark.unit
    def test_create_weather_tool(self):
        """Test creating weather lookup tool."""
        # TODO: Import create_weather_tool
        # TODO: Call create_weather_tool()
        # TODO: Assert returns callable
        # TODO: Assert tool has proper description
        pass
    
    @pytest.mark.beginner
    @pytest.mark.unit
    def test_create_search_tool(self):
        """Test creating web search tool."""
        # TODO: Import create_search_tool
        # TODO: Call create_search_tool()
        # TODO: Assert returns callable
        # TODO: Assert supports optional num_results parameter
        pass
    
    @pytest.mark.beginner
    @pytest.mark.unit
    def test_generate_tool_schema(self):
        """Test generating JSON schema from tool."""
        # TODO: Import generate_tool_schema and create_calculator_tool
        # TODO: Get calculator tool
        # TODO: Call generate_tool_schema
        # TODO: Assert returns dict
        # TODO: Assert has name, description, parameters
        # TODO: Assert parameters includes operation, a, b
        pass
    
    @pytest.mark.beginner
    @pytest.mark.unit
    def test_validate_tool_input(self):
        """Test validating input against tool schema."""
        # TODO: Import validate_tool_input and create_calculator_tool
        # TODO: Get calculator tool
        # TODO: Call validate_tool_input with valid inputs
        # TODO: Assert returns True
        # TODO: Call with invalid inputs (missing field)
        # TODO: Assert returns False
        pass
    
    @pytest.mark.beginner
    @pytest.mark.unit
    def test_get_tool_description(self):
        """Test extracting tool description."""
        # TODO: Import get_tool_description and create_calculator_tool
        # TODO: Get calculator tool
        # TODO: Call get_tool_description
        # TODO: Assert returns string description
        # TODO: Assert description is not empty
        pass
    
    @pytest.mark.beginner
    @pytest.mark.unit
    def test_compose_tool_registry(self):
        """Test creating registry of tools."""
        # TODO: Import compose_tool_registry and create multiple tools
        # TODO: Get list of tools
        # TODO: Call compose_tool_registry
        # TODO: Assert returns dict
        # TODO: Assert can lookup tools by name
        # TODO: Assert all tools present in registry
        pass
