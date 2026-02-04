"""
Tests for Exercise 13: Document Loading and Processing
======================================================

Run with: pytest tests/test_13_document_loading.py -v
"""

import pytest
from src.exercises.document_loading_13 import (
    Document,
    LoaderConfig,
    load_pdf_document,
    load_web_page,
    load_csv_documents,
    load_text_file,
    load_directory,
    extract_metadata,
    clean_document_text,
    validate_document,
    merge_documents,
)


@pytest.mark.intermediate
class TestDocumentLoading:
    """Test document loading functions."""
    
    @pytest.mark.unit
    def test_load_pdf_document(self, tmp_path):
        """
        TODO: Test PDF loading.
        
        Steps:
        1. Create or use a sample PDF
        2. Load with load_pdf_document()
        3. Verify content extracted
        4. Verify metadata includes source and page info
        """
        pass
    
    @pytest.mark.unit
    def test_load_web_page(self, mock_requests):
        """
        TODO: Test web page loading.
        
        Steps:
        1. Mock HTTP response
        2. Load with load_web_page()
        3. Verify HTML cleaned to text
        4. Verify metadata includes URL
        """
        pass
    
    @pytest.mark.unit
    def test_load_csv_documents(self, tmp_path):
        """
        TODO: Test CSV loading.
        
        Steps:
        1. Create sample CSV file
        2. Load with load_csv_documents()
        3. Verify one document per row
        4. Verify content columns combined
        5. Verify metadata columns preserved
        """
        pass
    
    @pytest.mark.unit
    def test_load_text_file(self, tmp_path):
        """
        TODO: Test text file loading.
        
        Steps:
        1. Create sample text file
        2. Load with load_text_file()
        3. Verify content matches file
        4. Verify metadata includes file info
        """
        pass
    
    @pytest.mark.integration
    def test_load_directory(self, tmp_path):
        """
        TODO: Test directory loading.
        
        Steps:
        1. Create directory with multiple file types
        2. Load with load_directory()
        3. Verify all supported files loaded
        4. Verify unsupported files skipped
        """
        pass


@pytest.mark.intermediate
class TestDocumentProcessing:
    """Test document processing functions."""
    
    @pytest.mark.unit
    def test_extract_metadata(self):
        """
        TODO: Test metadata extraction.
        
        Steps:
        1. Create document with content
        2. Extract metadata
        3. Verify word count, language detection
        """
        pass
    
    @pytest.mark.unit
    def test_clean_document_text(self):
        """
        TODO: Test text cleaning.
        
        Steps:
        1. Create document with messy text
        2. Clean with various options
        3. Verify whitespace normalized
        4. Verify original not modified
        """
        pass
    
    @pytest.mark.unit
    def test_validate_document(self):
        """
        TODO: Test document validation.
        
        Steps:
        1. Create valid and invalid documents
        2. Validate each
        3. Verify correct validation results
        """
        pass
    
    @pytest.mark.unit
    def test_merge_documents(self):
        """
        TODO: Test document merging.
        
        Steps:
        1. Create multiple documents
        2. Merge with separator
        3. Verify combined content
        4. Verify metadata merged
        """
        pass
