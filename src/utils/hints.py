"""
Hints System for LangChain Exercises
=====================================

This module provides a progressive hint system for learners who get stuck.
Hints are revealed one at a time to encourage independent problem-solving.

Usage:
    from src.utils.hints import get_hint, show_all_hints
    
    # Get next hint for a function
    get_hint("initialize_model")
    
    # Get specific hint level
    get_hint("initialize_model", level=2)
    
    # Show all hints (spoiler!)
    show_all_hints("initialize_model")
"""

from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class HintSet:
    """Collection of progressive hints for a function."""
    function_name: str
    exercise: str
    hints: List[str]
    solution_approach: str


# Hint database organized by exercise
HINTS_DATABASE: Dict[str, HintSet] = {
    # Exercise 01: Model Basics
    "initialize_model": HintSet(
        function_name="initialize_model",
        exercise="01_model_basics",
        hints=[
            "Look for init_chat_model() in langchain module",
            "The model_name format is 'provider/model' like 'openai/gpt-4-turbo'",
            "Check that you're importing from the right module: from langchain import init_chat_model",
            "The function should simply call init_chat_model(model_name) and return the result",
        ],
        solution_approach="Use init_chat_model() from langchain package with the model_name parameter"
    ),
    "invoke_model": HintSet(
        function_name="invoke_model",
        exercise="01_model_basics",
        hints=[
            "The model object has an .invoke() method",
            "invoke() takes a string prompt and returns a response object",
            "The response has a .content attribute with the text",
            "Return response.content to get just the string",
        ],
        solution_approach="Call model.invoke(prompt) and return response.content"
    ),
    "stream_model": HintSet(
        function_name="stream_model",
        exercise="01_model_basics",
        hints=[
            "Use model.stream() instead of model.invoke()",
            "stream() returns an iterator that yields chunks",
            "Each chunk has a .content attribute",
            "Use 'yield chunk.content' in a for loop",
        ],
        solution_approach="for chunk in model.stream(prompt): yield chunk.content"
    ),
    "batch_model": HintSet(
        function_name="batch_model",
        exercise="01_model_basics",
        hints=[
            "Use model.batch() with a list of prompts",
            "batch() returns a list of response objects",
            "Extract .content from each response",
            "Use list comprehension: [r.content for r in responses]",
        ],
        solution_approach="Call model.batch(prompts) and extract .content from each response"
    ),
    
    # Exercise 02: Messages
    "create_system_message": HintSet(
        function_name="create_system_message",
        exercise="02_messages",
        hints=[
            "Import SystemMessage from langchain_core.messages",
            "SystemMessage takes content as argument",
            "Return SystemMessage(content)",
        ],
        solution_approach="from langchain_core.messages import SystemMessage; return SystemMessage(content)"
    ),
    "build_conversation": HintSet(
        function_name="build_conversation",
        exercise="02_messages",
        hints=[
            "A conversation is just a list of messages",
            "Start with SystemMessage for system prompt",
            "Alternate HumanMessage and AIMessage",
            "Return the list of message objects",
        ],
        solution_approach="Build a list starting with SystemMessage, then alternating Human/AI messages"
    ),
    
    # Exercise 03: Tools
    "create_calculator_tool": HintSet(
        function_name="create_calculator_tool",
        exercise="03_tool_definition",
        hints=[
            "Import the @tool decorator from langchain_core.tools",
            "Define a function with proper type hints",
            "Write a clear docstring - this becomes the tool description",
            "The decorator auto-generates the schema from your function",
        ],
        solution_approach="@tool decorator + function with type hints + docstring"
    ),
    
    # Exercise 04: Agents
    "create_basic_agent": HintSet(
        function_name="create_basic_agent",
        exercise="04_basic_agents",
        hints=[
            "Look for create_agent() in langchain",
            "You need to pass both model and tools",
            "The agent wraps the model with tool-use capability",
            "Return the created agent object",
        ],
        solution_approach="Use create_agent(model, tools) from langchain"
    ),
    
    # Exercise 13: Document Loading
    "load_pdf_document": HintSet(
        function_name="load_pdf_document",
        exercise="13_document_loading",
        hints=[
            "You can use PyPDF2, pdfplumber, or langchain document loaders",
            "Each page should become a separate Document",
            "Store page number and source in metadata",
            "Handle encoding issues with proper error handling",
        ],
        solution_approach="Use a PDF library to extract text page by page, create Document objects"
    ),
    "load_web_page": HintSet(
        function_name="load_web_page",
        exercise="13_document_loading",
        hints=[
            "Use requests to fetch HTML content",
            "Use BeautifulSoup to parse and clean HTML",
            "Extract main content, remove nav/footer/ads",
            "Store URL and title in metadata",
        ],
        solution_approach="requests.get() + BeautifulSoup for parsing + clean text extraction"
    ),
    
    # Exercise 15: Embeddings
    "create_embeddings": HintSet(
        function_name="create_embeddings",
        exercise="15_embeddings_vectorstores",
        hints=[
            "Use the embedding model's embed_documents() method",
            "Pass a list of texts, get a list of vectors back",
            "Handle batching for large document sets",
            "Each vector is a list of floats",
        ],
        solution_approach="model.embed_documents(texts) returns list of embedding vectors"
    ),
    "similarity_search": HintSet(
        function_name="similarity_search",
        exercise="15_embeddings_vectorstores",
        hints=[
            "First embed the query using the same model",
            "Use the vector store's search method",
            "Results are ordered by similarity score",
            "Return top k results with scores",
        ],
        solution_approach="Embed query, then store.similarity_search(query_embedding, k=k)"
    ),
    
    # Exercise 16: Retrieval Chains
    "basic_rag_chain": HintSet(
        function_name="basic_rag_chain",
        exercise="16_retrieval_chains",
        hints=[
            "Step 1: Retrieve documents using the retriever",
            "Step 2: Format documents into context string",
            "Step 3: Create prompt with query + context",
            "Step 4: Generate answer using LLM",
            "Step 5: Return answer with sources",
        ],
        solution_approach="Retrieve → Format Context → Prompt → Generate → Return with sources"
    ),
    
    # Exercise 17: Advanced RAG
    "rerank_results": HintSet(
        function_name="rerank_results",
        exercise="17_advanced_rag",
        hints=[
            "Cross-encoders score (query, doc) pairs together",
            "Create pairs of (query, doc.page_content) for each doc",
            "Use reranker.predict(pairs) to get scores",
            "Sort by score descending and take top_k",
        ],
        solution_approach="pairs = [(query, doc) for doc in docs]; scores = reranker.predict(pairs); sort and return top_k"
    ),
    "hybrid_search": HintSet(
        function_name="hybrid_search",
        exercise="17_advanced_rag",
        hints=[
            "Run both vector search and BM25 search",
            "Normalize scores from each method",
            "Combine with alpha weighting: alpha*vector + (1-alpha)*bm25",
            "Use reciprocal rank fusion for combining result lists",
        ],
        solution_approach="Run both searches, normalize scores, combine with RRF"
    ),
    
    # Exercise 18: Evaluation
    "recall_at_k": HintSet(
        function_name="recall_at_k",
        exercise="18_rag_evaluation",
        hints=[
            "Recall = (relevant docs found) / (total relevant docs)",
            "Only consider the top k retrieved results",
            "Convert lists to sets for intersection",
            "Handle edge case where no relevant docs exist",
        ],
        solution_approach="len(set(retrieved[:k]) & set(relevant)) / len(relevant)"
    ),
    "evaluate_faithfulness": HintSet(
        function_name="evaluate_faithfulness",
        exercise="18_rag_evaluation",
        hints=[
            "Extract claims/statements from the answer",
            "Check each claim against the context",
            "Use LLM to determine if claim is supported",
            "Return ratio of supported claims",
        ],
        solution_approach="Extract claims, verify each against context using LLM, return support ratio"
    ),
}


def get_hint(function_name: str, level: int = None) -> str:
    """
    Get a hint for a specific function.
    
    Args:
        function_name: Name of the function to get hint for
        level: Specific hint level (1-indexed). If None, returns next unrevealed hint.
        
    Returns:
        Hint string
        
    Example:
        >>> get_hint("initialize_model")
        "Hint 1/4: Look for init_chat_model() in langchain module"
        >>> get_hint("initialize_model", level=2)
        "Hint 2/4: The model_name format is 'provider/model' like 'openai/gpt-4-turbo'"
    """
    if function_name not in HINTS_DATABASE:
        return f"No hints available for '{function_name}'. Check the function name."
    
    hint_set = HINTS_DATABASE[function_name]
    total_hints = len(hint_set.hints)
    
    if level is None:
        level = 1  # Default to first hint
    
    if level < 1 or level > total_hints:
        return f"Invalid hint level. Available levels: 1-{total_hints}"
    
    hint_text = hint_set.hints[level - 1]
    return f"Hint {level}/{total_hints}: {hint_text}"


def show_all_hints(function_name: str) -> str:
    """
    Show all hints for a function (spoiler warning!).
    
    Args:
        function_name: Name of the function
        
    Returns:
        All hints formatted as a string
    """
    if function_name not in HINTS_DATABASE:
        return f"No hints available for '{function_name}'."
    
    hint_set = HINTS_DATABASE[function_name]
    
    lines = [
        f"All hints for {function_name} ({hint_set.exercise}):",
        "-" * 50,
    ]
    
    for i, hint in enumerate(hint_set.hints, 1):
        lines.append(f"{i}. {hint}")
    
    lines.extend([
        "-" * 50,
        f"Approach: {hint_set.solution_approach}",
    ])
    
    return "\n".join(lines)


def get_solution_approach(function_name: str) -> str:
    """
    Get the general solution approach for a function.
    
    Args:
        function_name: Name of the function
        
    Returns:
        Solution approach string
    """
    if function_name not in HINTS_DATABASE:
        return f"No solution approach available for '{function_name}'."
    
    return HINTS_DATABASE[function_name].solution_approach


def list_available_hints() -> List[str]:
    """
    List all functions that have hints available.
    
    Returns:
        List of function names with hints
    """
    return sorted(HINTS_DATABASE.keys())


def get_hints_for_exercise(exercise: str) -> Dict[str, HintSet]:
    """
    Get all hints for a specific exercise.
    
    Args:
        exercise: Exercise identifier (e.g., "01_model_basics")
        
    Returns:
        Dictionary of function_name -> HintSet
    """
    return {
        name: hints 
        for name, hints in HINTS_DATABASE.items() 
        if hints.exercise == exercise
    }


# Interactive hint helper
class HintHelper:
    """
    Interactive hint helper for Jupyter notebooks or REPL.
    
    Usage:
        helper = HintHelper("initialize_model")
        helper.next()  # Get first hint
        helper.next()  # Get second hint
        helper.reveal()  # Show all hints
    """
    
    def __init__(self, function_name: str):
        self.function_name = function_name
        self.current_level = 0
        
        if function_name not in HINTS_DATABASE:
            print(f"No hints available for '{function_name}'.")
            self.max_level = 0
        else:
            self.max_level = len(HINTS_DATABASE[function_name].hints)
    
    def next(self) -> str:
        """Get the next hint."""
        if self.current_level >= self.max_level:
            return "No more hints! Try show_solution_approach() or reveal()."
        
        self.current_level += 1
        hint = get_hint(self.function_name, self.current_level)
        print(hint)
        return hint
    
    def reset(self):
        """Reset to first hint."""
        self.current_level = 0
        print("Hints reset. Call next() to start over.")
    
    def reveal(self) -> str:
        """Show all hints (spoiler!)."""
        result = show_all_hints(self.function_name)
        print(result)
        return result
    
    def approach(self) -> str:
        """Show the solution approach."""
        result = get_solution_approach(self.function_name)
        print(f"Solution approach: {result}")
        return result


# Convenience function for quick access
def hint(function_name: str, level: int = None):
    """
    Quick hint access function.
    
    Examples:
        >>> hint("initialize_model")
        >>> hint("basic_rag_chain", 3)
    """
    print(get_hint(function_name, level))
