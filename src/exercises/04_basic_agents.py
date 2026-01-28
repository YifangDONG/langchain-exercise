"""
Exercise 04: Basic Agents & ReAct Pattern
==========================================

LEVEL: Beginner

GOAL: Create and invoke agents with ReAct (Reasoning + Acting) pattern.

TODO:
1. Implement create_basic_agent() to instantiate an agent
2. Implement invoke_agent() to run agent with messages
3. Implement extract_agent_steps() to get ReAct reasoning steps
4. Implement format_agent_response() to present results clearly

CONCEPTS TO LEARN:
- Agent creation and configuration
- ReAct pattern: Reasoning → Action → Observation
- Agent invocation and interaction
- Tool binding to agents
- Agent state and action selection
- Stopping conditions for agents

RESOURCES:
- LangChain docs: https://docs.langchain.com/oss/python/langchain/overview
- Related exercises: 01_model_basics, 03_tool_definition

HINTS:
- Use create_agent() from langchain
- Agents bind models with tools
- ReAct has distinct thinking and action phases
- Agent responses contain structured action information
- Tools are invoked based on agent decisions
"""

from typing import Any, Dict, List, Iterator, Tuple
from langchain_core.messages import BaseMessage, HumanMessage


def create_basic_agent(model: Any, tools: List[Any]) -> Any:
    """
    TODO: Create a basic agent with a model and tools.
    
    Requirements:
    - Use create_agent() from langchain
    - Bind tools to the agent
    - Configure for tool use
    - Return initialized agent
    
    Args:
        model: Language model for the agent
        tools: List of tools available to agent
        
    Returns:
        Configured agent object
    """
    pass


def invoke_agent(agent: Any, messages: List[BaseMessage], max_iterations: int = 10) -> Dict[str, Any]:
    """
    TODO: Invoke agent and run until completion or max iterations.
    
    Requirements:
    - Call agent.invoke() with messages
    - Implement iteration loop for ReAct
    - Track all reasoning and actions
    - Return final response and history
    
    Args:
        agent: Agent instance
        messages: Message input to agent
        max_iterations: Maximum iterations before stopping
        
    Returns:
        Dictionary with response, steps, and metadata
    """
    pass


def extract_agent_steps(agent_response: Dict[str, Any]) -> List[Dict[str, str]]:
    """
    TODO: Extract reasoning and action steps from agent response.
    
    Requirements:
    - Identify thinking/reasoning steps
    - Identify action/tool calls
    - Identify observation/results
    - Return chronological steps
    
    Args:
        agent_response: Response from agent.invoke()
        
    Returns:
        List of steps with type, content, and tool info
    """
    pass


def stream_agent_response(agent: Any, messages: List[BaseMessage]) -> Iterator[str]:
    """
    TODO: Stream agent thinking and responses.
    
    Requirements:
    - Use agent.stream() method if available
    - Yield intermediate steps and thinking
    - Show real-time reasoning process
    
    Args:
        agent: Agent instance
        messages: Input messages
        
    Yields:
        Text chunks of agent reasoning
    """
    pass


def format_agent_response(response: Dict[str, Any]) -> str:
    """
    TODO: Format agent response for readable display.
    
    Requirements:
    - Show reasoning steps
    - Show action/tool calls
    - Show observations/results
    - Show final answer
    
    Args:
        response: Agent response dictionary
        
    Returns:
        Formatted string representation
    """
    pass


def count_agent_iterations(response: Dict[str, Any]) -> int:
    """
    TODO: Count how many reasoning/action steps agent took.
    
    Requirements:
    - Count reasoning steps
    - Count action invocations
    - Return total iterations
    
    Args:
        response: Agent response dictionary
        
    Returns:
        Number of iteration steps
    """
    pass


def verify_agent_answer(response: Dict[str, Any]) -> bool:
    """
    TODO: Check if agent reached valid answer.
    
    Requirements:
    - Verify response contains final answer
    - Check all actions completed
    - Return True if agent finished successfully
    
    Args:
        response: Agent response dictionary
        
    Returns:
        True if agent has valid answer
    """
    pass
