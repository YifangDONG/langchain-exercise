"""
Tests for Exercise 14: Text Chunking Strategies
================================================

Run with: pytest tests/test_14_text_chunking.py -v
"""

import pytest
from src.exercises.text_chunking_14 import (
    Document,
    ChunkingConfig,
    chunk_by_character,
    chunk_by_separator,
    recursive_chunk,
    chunk_by_tokens,
    semantic_chunk,
    chunk_with_headers,
    merge_small_chunks,
    add_chunk_context,
    calculate_chunk_statistics,
    create_parent_child_chunks,
)


@pytest.mark.intermediate
class TestChunkingStrategies:
    """Test different chunking strategies."""
    
    @pytest.mark.unit
    def test_chunk_by_character(self):
        """
        TODO: Test character-based chunking.
        
        Steps:
        1. Create document with known length
        2. Chunk with specific size and overlap
        3. Verify chunk count correct
        4. Verify overlap applied
        5. Verify metadata propagated
        """
        pass
    
    @pytest.mark.unit
    def test_chunk_by_separator(self):
        """
        TODO: Test separator-based chunking.
        
        Steps:
        1. Create document with paragraphs
        2. Chunk by paragraph separator
        3. Verify splits at separators
        4. Verify respects size limits
        """
        pass
    
    @pytest.mark.unit
    def test_recursive_chunk(self):
        """
        TODO: Test recursive chunking.
        
        Steps:
        1. Create document with mixed content
        2. Apply recursive chunking
        3. Verify all chunks under size limit
        4. Verify natural breaks preserved
        """
        pass
    
    @pytest.mark.unit
    def test_chunk_by_tokens(self, mock_tokenizer):
        """
        TODO: Test token-based chunking.
        
        Steps:
        1. Create document
        2. Chunk with token limits
        3. Verify token count per chunk
        """
        pass
    
    @pytest.mark.unit
    def test_chunk_with_headers(self):
        """
        TODO: Test header-preserving chunking.
        
        Steps:
        1. Create markdown document with headers
        2. Chunk preserving headers
        3. Verify headers in metadata
        """
        pass


@pytest.mark.intermediate
class TestChunkPostProcessing:
    """Test chunk post-processing functions."""
    
    @pytest.mark.unit
    def test_merge_small_chunks(self):
        """
        TODO: Test merging small chunks.
        
        Steps:
        1. Create chunks of varying sizes
        2. Merge small ones
        3. Verify no chunks below minimum
        4. Verify no chunks above maximum
        """
        pass
    
    @pytest.mark.unit
    def test_add_chunk_context(self):
        """
        TODO: Test adding neighbor context.
        
        Steps:
        1. Create ordered chunks
        2. Add context from neighbors
        3. Verify prev/next context in metadata
        """
        pass
    
    @pytest.mark.unit
    def test_calculate_chunk_statistics(self):
        """
        TODO: Test statistics calculation.
        
        Steps:
        1. Create chunks
        2. Calculate statistics
        3. Verify count, avg, min, max correct
        """
        pass
    
    @pytest.mark.unit
    def test_create_parent_child_chunks(self):
        """
        TODO: Test parent-child hierarchy.
        
        Steps:
        1. Create document
        2. Generate parent and child chunks
        3. Verify children reference parents
        4. Verify size relationships
        """
        pass
