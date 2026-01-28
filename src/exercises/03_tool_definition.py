"""
Exercise 03: Tool Definition & Schemas
======================================

LEVEL: Beginner

GOAL: Create tools with decorators and understand tool schemas.

TODO:
1. Implement @tool decorated functions for basic operations
2. Implement generate_tool_schema() to create tool schemas
3. Implement validate_tool_input() to check tool parameters
4. Implement compose_tool_registry() to organize multiple tools

CONCEPTS TO LEARN:
- @tool decorator for tool definition
- Tool descriptions and documentation
- Parameter type hints and validation
- Tool schema generation from Python functions
- Tool naming and organization

RESOURCES:
- LangChain docs: https://docs.langchain.com/oss/python/langchain/overview
- Related exercises: 01_model_basics, 04_basic_agents

HINTS:
- Use @tool decorator from langchain_core.tools
- Tool description comes from docstring
- Type hints define parameter schema
- Return type defines output schema
- Tools should have clear, specific purposes
"""

from typing import Any, Dict, List, Optional, Callable
from langchain_core.tools import tool


# TODO: Create your first tool using @tool decorator
# Example structure:
# @tool
# def my_tool(param: str) -> str:
#     \"\"\"Tool description explaining what it does.\"\"\"
#     return f"Result: {param}"


def create_calculator_tool() -> Callable:
    """
    TODO: Create a calculator tool using @tool decorator.
    
    Requirements:
    - Define @tool function for calculator
    - Support add, subtract, multiply, divide operations
    - Handle division by zero
    - Clear docstring describing functionality
    
    Returns:
        Calculator tool function
    """
    @tool
    def calculator(operation: str, a: float, b: float) -> float:
        """
        TODO: Implement calculator tool.
        
        Performs basic mathematical operations on two numbers.
        
        Args:
            operation: One of 'add', 'subtract', 'multiply', 'divide'
            a: First number
            b: Second number
            
        Returns:
            Result of the operation
        """
        pass
    
    return calculator


def create_weather_tool() -> Callable:
    """
    TODO: Create a weather lookup tool using @tool decorator.
    
    Requirements:
    - Accept location as parameter
    - Return simulated weather data
    - Clear documentation
    
    Returns:
        Weather tool function
    """
    pass


def create_search_tool() -> Callable:
    """
    TODO: Create a web search tool using @tool decorator.
    
    Requirements:
    - Accept query and optional num_results parameter
    - Return simulated search results
    - Document all parameters
    
    Returns:
        Search tool function
    """
    pass


def generate_tool_schema(tool_func: Callable) -> Dict[str, Any]:
    """
    TODO: Generate JSON schema from a tool function.
    
    Requirements:
    - Extract tool metadata (name, description)
    - Generate parameter schema from type hints
    - Include required and optional parameters
    
    Args:
        tool_func: Tool function with @tool decorator
        
    Returns:
        JSON schema representation of tool
    """
    pass


def validate_tool_input(tool_func: Callable, input_data: Dict[str, Any]) -> bool:
    """
    TODO: Validate input against tool schema.
    
    Requirements:
    - Check all required parameters present
    - Validate parameter types
    - Return True if valid, False otherwise
    
    Args:
        tool_func: Tool function to validate against
        input_data: Input parameters to validate
        
    Returns:
        True if input is valid for tool
    """
    pass


def get_tool_description(tool_func: Callable) -> str:
    """
    TODO: Extract tool description from docstring.
    
    Requirements:
    - Get docstring from tool function
    - Extract first line as summary
    - Include full description if available
    
    Args:
        tool_func: Tool function
        
    Returns:
        Tool description string
    """
    pass


def compose_tool_registry(tools: List[Callable]) -> Dict[str, Callable]:
    """
    TODO: Create a registry of tools indexed by name.
    
    Requirements:
    - Map tool names to tool functions
    - Enable easy lookup by name
    - Return organized registry
    
    Args:
        tools: List of tool functions
        
    Returns:
        Dictionary mapping tool names to functions
    """
    pass
