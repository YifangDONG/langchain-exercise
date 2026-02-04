"""
Exercise 14: Text Chunking Strategies
======================================

LEVEL: Intermediate (RAG-focused)

GOAL: Learn to split documents into optimal chunks for retrieval.
      Good chunking is critical for RAG quality.

TODO:
1. Implement chunk_by_character() for simple fixed-size chunks
2. Implement chunk_by_separator() for structure-aware splitting
3. Implement recursive_chunk() for smart hierarchical splitting
4. Implement chunk_by_tokens() for LLM-aware chunking
5. Implement semantic_chunk() for meaning-based splitting
6. Implement evaluate_chunking_strategy() to compare approaches

CONCEPTS TO LEARN:
- Chunk size vs retrieval quality tradeoffs
- Overlap strategies for context preservation
- Token-aware chunking for LLM limits
- Semantic chunking for coherent units
- Metadata propagation through chunking

RESOURCES:
- LangChain docs: https://python.langchain.com/docs/modules/data_connection/document_transformers/
- Related exercises: 13_document_loading, 15_embeddings

HINTS:
- Too small chunks = missing context
- Too large chunks = noise in retrieval
- Overlap helps maintain context across boundaries
- Different content types need different strategies
"""

from typing import Any, Callable, Dict, List, Optional, Tuple
from dataclasses import dataclass, field


@dataclass
class Document:
    """Document with content and metadata."""
    page_content: str
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ChunkingConfig:
    """Configuration for text chunking."""
    chunk_size: int = 1000
    chunk_overlap: int = 200
    length_function: Callable[[str], int] = len
    separators: List[str] = field(
        default_factory=lambda: ["\n\n", "\n", ". ", " ", ""]
    )
    keep_separator: bool = True


def chunk_by_character(
    document: Document,
    chunk_size: int = 1000,
    chunk_overlap: int = 200
) -> List[Document]:
    """
    TODO: Split document into fixed-size character chunks.
    
    Requirements:
    - Split text into chunks of chunk_size characters
    - Apply chunk_overlap characters of overlap
    - Preserve and propagate document metadata
    - Add chunk index to metadata
    
    Args:
        document: Document to chunk
        chunk_size: Target size of each chunk in characters
        chunk_overlap: Number of overlapping characters
        
    Returns:
        List of Document chunks
        
    Example:
        >>> doc = Document(page_content="A" * 2500, metadata={"source": "test"})
        >>> chunks = chunk_by_character(doc, chunk_size=1000, chunk_overlap=200)
        >>> len(chunks)
        3
        >>> chunks[0].metadata
        {"source": "test", "chunk_index": 0, "total_chunks": 3}
    """
    pass


def chunk_by_separator(
    document: Document,
    separators: List[str] = None,
    chunk_size: int = 1000,
    chunk_overlap: int = 200
) -> List[Document]:
    """
    TODO: Split document at natural boundaries (paragraphs, sentences).
    
    Requirements:
    - Try separators in order (most to least preferred)
    - Keep chunks under chunk_size when possible
    - Apply overlap for context preservation
    - Don't break in the middle of sentences
    
    Args:
        document: Document to chunk
        separators: List of separators in preference order
        chunk_size: Maximum chunk size
        chunk_overlap: Overlap between chunks
        
    Returns:
        List of Document chunks
        
    Example:
        >>> doc = Document(page_content="Para 1.\\n\\nPara 2.\\n\\nPara 3.")
        >>> chunks = chunk_by_separator(doc, separators=["\\n\\n"])
        >>> [c.page_content for c in chunks]
        ["Para 1.", "Para 2.", "Para 3."]
    """
    pass


def recursive_chunk(
    document: Document,
    config: Optional[ChunkingConfig] = None
) -> List[Document]:
    """
    TODO: Recursively split using hierarchy of separators.
    
    This is the most commonly used strategy in RAG systems.
    
    Requirements:
    - Try to split by paragraphs first (\\n\\n)
    - If chunks too big, split by sentences (. )
    - If still too big, split by words ( )
    - Finally split by characters if needed
    - Maintain overlap between chunks
    
    Args:
        document: Document to chunk
        config: Chunking configuration
        
    Returns:
        List of Document chunks optimized for retrieval
        
    Example:
        >>> doc = Document(page_content=long_text)
        >>> chunks = recursive_chunk(doc)
        >>> all(len(c.page_content) <= config.chunk_size for c in chunks)
        True
    """
    pass


def chunk_by_tokens(
    document: Document,
    max_tokens: int = 500,
    overlap_tokens: int = 50,
    encoding_name: str = "cl100k_base"
) -> List[Document]:
    """
    TODO: Split document by token count (for LLM context limits).
    
    Requirements:
    - Use tiktoken to count tokens accurately
    - Ensure chunks fit in LLM context window
    - Maintain token-based overlap
    - Handle different tokenizer encodings
    
    Args:
        document: Document to chunk
        max_tokens: Maximum tokens per chunk
        overlap_tokens: Token overlap between chunks
        encoding_name: Tiktoken encoding name
        
    Returns:
        List of Document chunks with guaranteed token limits
        
    Example:
        >>> chunks = chunk_by_tokens(doc, max_tokens=500)
        >>> # Each chunk guaranteed to be <= 500 tokens
    """
    pass


def semantic_chunk(
    document: Document,
    embedding_model: Any = None,
    similarity_threshold: float = 0.5
) -> List[Document]:
    """
    TODO: Split document at semantic boundaries.
    
    This creates more coherent chunks by finding natural topic changes.
    
    Requirements:
    - Split into sentences first
    - Compute embeddings for each sentence
    - Find breakpoints where similarity drops
    - Group similar sentences into chunks
    - Respect maximum chunk size
    
    Args:
        document: Document to chunk
        embedding_model: Model to compute embeddings
        similarity_threshold: Threshold for grouping sentences
        
    Returns:
        List of semantically coherent Document chunks
        
    Example:
        >>> chunks = semantic_chunk(doc, model, threshold=0.5)
        >>> # Each chunk contains semantically related content
    """
    pass


def chunk_with_headers(
    document: Document,
    header_patterns: List[str] = None
) -> List[Document]:
    """
    TODO: Split document preserving header context.
    
    Requirements:
    - Identify headers in the document
    - Include relevant headers in each chunk
    - Maintain document hierarchy in metadata
    - Useful for structured documents
    
    Args:
        document: Document to chunk
        header_patterns: Regex patterns for headers
        
    Returns:
        List of Document chunks with header context
        
    Example:
        >>> doc = Document("# Main\\n## Sub\\nContent here")
        >>> chunks = chunk_with_headers(doc)
        >>> chunks[0].metadata["headers"]
        ["Main", "Sub"]
    """
    pass


def merge_small_chunks(
    chunks: List[Document],
    min_chunk_size: int = 100,
    max_chunk_size: int = 1000
) -> List[Document]:
    """
    TODO: Merge chunks that are too small.
    
    Requirements:
    - Combine adjacent chunks below min_chunk_size
    - Don't exceed max_chunk_size when merging
    - Update metadata appropriately
    
    Args:
        chunks: List of chunks to potentially merge
        min_chunk_size: Minimum acceptable chunk size
        max_chunk_size: Maximum size after merging
        
    Returns:
        List of chunks with small ones merged
    """
    pass


def add_chunk_context(
    chunks: List[Document],
    context_size: int = 1
) -> List[Document]:
    """
    TODO: Add context from neighboring chunks to each chunk.
    
    Requirements:
    - Add summary or beginning of adjacent chunks
    - Store context in metadata, not page_content
    - Helps with retrieval of boundary content
    
    Args:
        chunks: List of ordered chunks
        context_size: Number of neighboring chunks to include
        
    Returns:
        Chunks with added context in metadata
        
    Example:
        >>> enhanced = add_chunk_context(chunks, context_size=1)
        >>> enhanced[1].metadata["prev_context"]
        "End of previous chunk..."
        >>> enhanced[1].metadata["next_context"]
        "Start of next chunk..."
    """
    pass


def calculate_chunk_statistics(
    chunks: List[Document]
) -> Dict[str, Any]:
    """
    TODO: Calculate statistics about chunking results.
    
    Requirements:
    - Count total chunks
    - Calculate size distribution (min, max, avg, median)
    - Identify potential issues (very small/large chunks)
    - Measure overlap effectiveness
    
    Args:
        chunks: List of chunks to analyze
        
    Returns:
        Dictionary of statistics
        
    Example:
        >>> stats = calculate_chunk_statistics(chunks)
        >>> print(stats)
        {
            "count": 42,
            "avg_size": 856,
            "min_size": 234,
            "max_size": 1000,
            "size_std": 156
        }
    """
    pass


def evaluate_chunking_strategy(
    document: Document,
    strategies: List[Callable],
    test_queries: List[str] = None
) -> Dict[str, Any]:
    """
    TODO: Compare different chunking strategies.
    
    Requirements:
    - Apply each strategy to the document
    - Calculate statistics for each
    - Optionally test retrieval quality
    - Return comparison results
    
    Args:
        document: Document to chunk
        strategies: List of chunking functions to compare
        test_queries: Optional queries to test retrieval
        
    Returns:
        Comparison results for each strategy
        
    Example:
        >>> results = evaluate_chunking_strategy(
        ...     doc,
        ...     [chunk_by_character, recursive_chunk, semantic_chunk]
        ... )
        >>> results["recursive_chunk"]["avg_size"]
        856
    """
    pass


def create_parent_child_chunks(
    document: Document,
    parent_chunk_size: int = 2000,
    child_chunk_size: int = 500
) -> Tuple[List[Document], List[Document]]:
    """
    TODO: Create hierarchical parent-child chunks.
    
    This is an advanced RAG technique where:
    - Small chunks are used for precise retrieval
    - Parent chunks are returned for more context
    
    Requirements:
    - Create large parent chunks
    - Create smaller child chunks within parents
    - Link children to parents via metadata
    
    Args:
        document: Document to chunk
        parent_chunk_size: Size of parent chunks
        child_chunk_size: Size of child chunks
        
    Returns:
        Tuple of (parent_chunks, child_chunks)
        
    Example:
        >>> parents, children = create_parent_child_chunks(doc)
        >>> children[0].metadata["parent_id"]
        "parent_0"
    """
    pass
