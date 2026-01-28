"""
Exercise 08: System Prompts & Prompt Engineering
================================================

LEVEL: Intermediate

GOAL: Use static and dynamic system prompts to guide model behavior.

TODO:
1. Implement create_system_prompt() for static prompts
2. Implement dynamic_system_prompt() for context-aware prompts
3. Implement prompt_template() for variable substitution
4. Implement measure_prompt_effectiveness() to compare prompts

CONCEPTS TO LEARN:
- System message purpose and structure
- Prompt engineering best practices
- Variable substitution in prompts
- Dynamic prompt generation
- Role definition and context setting
- Prompt templates and formatting

RESOURCES:
- LangChain docs: https://docs.langchain.com/oss/python/langchain/overview
- Related exercises: 01_model_basics, 02_messages

HINTS:
- System prompts set behavior and role
- Good prompts are clear and specific
- Variables use {variable_name} syntax
- Context can be injected into prompts
- Test different prompts and compare results
- Chain of thought prompts improve reasoning
"""

from typing import Any, Dict, List, Optional, Tuple
from string import Template


def create_system_prompt(role: str, instructions: str, context: str = "") -> str:
    """
    TODO: Create a system prompt with role and instructions.
    
    Requirements:
    - Define assistant role clearly
    - Include specific instructions
    - Add any relevant context
    - Return complete system prompt
    
    Args:
        role: The role/identity of the assistant
        instructions: Detailed instructions for behavior
        context: Optional additional context
        
    Returns:
        System prompt string
    """
    pass


def create_helpful_assistant_prompt() -> str:
    """
    TODO: Create a helpful assistant system prompt.
    
    Requirements:
    - Define as helpful assistant
    - Include key principles
    - Set tone and style
    - Include safety guidelines
    
    Returns:
        System prompt for helpful assistant
    """
    pass


def create_expert_prompt(expertise: str) -> str:
    """
    TODO: Create system prompt for expert role.
    
    Requirements:
    - Position as expert in domain
    - Include relevant knowledge
    - Set appropriate tone
    - Include expertise-specific guidelines
    
    Args:
        expertise: Area of expertise
        
    Returns:
        Expert system prompt
    """
    pass


def create_dynamic_system_prompt(
    base_prompt: str,
    variables: Dict[str, str]
) -> str:
    """
    TODO: Create dynamic prompt with variable substitution.
    
    Requirements:
    - Replace {variable_name} with values
    - Support multiple variables
    - Validate all variables replaced
    - Return complete prompt
    
    Args:
        base_prompt: Template prompt with {variables}
        variables: Dictionary of variable values
        
    Returns:
        Filled prompt string
    """
    pass


def create_prompt_template(template_string: str) -> Template:
    """
    TODO: Create reusable prompt template.
    
    Requirements:
    - Convert string to Template
    - Support variable substitution
    - Return template for reuse
    
    Args:
        template_string: Template with $variable placeholders
        
    Returns:
        Template object
    """
    pass


def inject_context_into_prompt(
    prompt: str,
    context_info: Dict[str, Any],
    context_format: str = "Context: {context}"
) -> str:
    """
    TODO: Inject contextual information into prompt.
    
    Requirements:
    - Add context information
    - Format it clearly
    - Preserve original prompt
    - Return enhanced prompt
    
    Args:
        prompt: Original prompt
        context_info: Contextual information
        context_format: Format string for context
        
    Returns:
        Prompt with injected context
    """
    pass


def create_chain_of_thought_prompt(task: str) -> str:
    """
    TODO: Create prompt encouraging step-by-step reasoning.
    
    Requirements:
    - Include think step by step instruction
    - Guide reasoning process
    - Ask for explicit reasoning
    - Format for clarity
    
    Args:
        task: The task description
        
    Returns:
        Chain of thought prompt
    """
    pass


def compare_prompts(
    model: Any,
    test_input: str,
    prompts: Dict[str, str]
) -> Dict[str, Dict[str, Any]]:
    """
    TODO: Compare effectiveness of different prompts.
    
    Requirements:
    - Run model with each prompt
    - Collect responses
    - Compare quality metrics
    - Return comparison results
    
    Args:
        model: Language model to test
        test_input: Test input for prompts
        prompts: Dictionary of prompt name -> prompt text
        
    Returns:
        Comparison results with responses and metrics
    """
    pass


def measure_prompt_quality(
    response: str,
    criteria: Dict[str, float]
) -> float:
    """
    TODO: Measure quality of response from prompt.
    
    Requirements:
    - Evaluate against criteria
    - Calculate quality score
    - Support multiple criteria
    - Return 0-1 score
    
    Args:
        response: Model response to evaluate
        criteria: Criteria weights
        
    Returns:
        Quality score between 0 and 1
    """
    pass
