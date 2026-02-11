"""
Exercise 01: Model Initialization & Basic Invocation
=====================================================

LEVEL: Beginner

GOAL: Initialize chat models from various providers and perform basic 
      invoke/stream/batch operations.

TODO:
1. Implement initialize_model() to initialize a chat model
2. Implement invoke_model() to invoke the model with a prompt
3. Implement stream_model() to stream tokens from the model
4. Implement batch_model() to process multiple prompts in batch

CONCEPTS TO LEARN:
- Model initialization with init_chat_model()
- invoke() method for single prompt execution
- stream() method for token-by-token output
- batch() method for multiple inputs
- Model parameters (temperature, max_tokens)

RESOURCES:
- LangChain docs: https://docs.langchain.com/oss/python/langchain/overview
- Related exercises: 02_messages, 04_basic_agents

HINTS:
- Look at langchain.chat_models.init_chat_model()
- Model can be specified by string like "openai/gpt-4"
- stream() yields chunks that can be concatenated
- batch() returns a list of responses
"""

from typing import Any, Iterator, List


def initialize_model(model_name: str = "openai/gpt-4-turbo") -> Any:
    """
    TODO: Initialize and return a chat model.
    
    Requirements:
    - Use init_chat_model() from langchain
    - Support multiple providers (openai, anthropic, google, etc.)
    - Handle API key configuration from environment
    - Return the initialized model
    
    Args:
        model_name: Model identifier (e.g., "openai/gpt-4-turbo")
        
    Returns:
        Initialized chat model object
    """
    from langchain import init_chat_model
    model = init_chat_model(model_name)
    return model


def invoke_model(model: Any, prompt: str) -> str:
    """
    TODO: Invoke the model with a prompt and return text response.
    
    Requirements:
    - Use the invoke() method
    - Extract and return the response content as string
    - Handle different response types
    
    Args:
        model: Initialized chat model
        prompt: Input prompt text
        
    Returns:
        Model response as string
    """
    for chunk in model.stream(prompt):
        yield chunk.content


def stream_model(model: Any, prompt: str) -> Iterator[str]:
    """
    TODO: Stream tokens from the model one at a time.
    
    Requirements:
    - Use the stream() method
    - Yield individual token chunks
    - Handle streaming response properly
    
    Args:
        model: Initialized chat model
        prompt: Input prompt text
        
    Yields:
        Individual token chunks from the model
    """
    pass


def batch_model(model: Any, prompts: List[str]) -> List[str]:
    """
    TODO: Process multiple prompts in batch.
    
    Requirements:
    - Use the batch() method
    - Process all prompts efficiently
    - Return list of responses in same order as input
    
    Args:
        model: Initialized chat model
        prompts: List of input prompts
        
    Returns:
        List of response strings
    """
    pass


def compare_model_parameters(
    model: Any, 
    prompt: str, 
    temperatures: List[float] = [0.0, 0.7, 1.0]
) -> List[str]:
    """
    TODO: Compare model outputs with different temperatures.
    
    Requirements:
    - Test multiple temperature values
    - Use invoke() for each configuration
    - Return list of responses for comparison
    
    Args:
        model: Initialized chat model
        prompt: Input prompt
        temperatures: List of temperature values to test
        
    Returns:
        List of responses for each temperature
    """
    pass
