"""
Exercise 13: Document Loading and Processing
=============================================

LEVEL: Intermediate (RAG-focused)

GOAL: Load documents from various sources (PDF, web, CSV, etc.) and prepare
      them for RAG pipeline processing.

TODO:
1. Implement load_pdf_document() to extract text from PDFs
2. Implement load_web_page() to scrape and clean web content
3. Implement load_csv_documents() to convert CSV rows to documents
4. Implement load_directory() to batch load multiple files
5. Implement extract_metadata() to get document properties
6. Implement create_document_pipeline() for chained processing

CONCEPTS TO LEARN:
- Document loaders for different file types
- Text extraction and cleaning
- Metadata extraction and management
- Document transformation pipelines
- Handling various encodings and formats

RESOURCES:
- LangChain docs: https://python.langchain.com/docs/modules/data_connection/document_loaders/
- Related exercises: 14_text_chunking, 15_embeddings

HINTS:
- Use langchain_community.document_loaders for standard loaders
- Documents have 'page_content' and 'metadata' attributes
- Clean extracted text (remove extra whitespace, fix encoding)
- Preserve source information in metadata
"""

from typing import Any, Dict, List, Optional
from dataclasses import dataclass, field


@dataclass
class Document:
    """
    Represents a document with content and metadata.
    
    This is compatible with LangChain's Document class.
    """
    page_content: str
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class LoaderConfig:
    """Configuration for document loaders."""
    encoding: str = "utf-8"
    clean_whitespace: bool = True
    extract_images: bool = False
    max_file_size_mb: int = 50
    supported_extensions: List[str] = field(
        default_factory=lambda: [".pdf", ".txt", ".md", ".csv", ".html"]
    )


def load_pdf_document(
    file_path: str,
    config: Optional[LoaderConfig] = None
) -> List[Document]:
    """
    TODO: Load a PDF file and extract text content.
    
    Requirements:
    - Extract text from all pages
    - Preserve page numbers in metadata
    - Handle multi-column layouts
    - Clean extracted text (remove artifacts)
    - Include source file path in metadata
    
    Args:
        file_path: Path to the PDF file
        config: Optional loader configuration
        
    Returns:
        List of Document objects (one per page or section)
        
    Example:
        >>> docs = load_pdf_document("report.pdf")
        >>> print(docs[0].page_content[:100])
        "Executive Summary: This report covers..."
        >>> print(docs[0].metadata)
        {"source": "report.pdf", "page": 1, "total_pages": 10}
    """
    pass


def load_web_page(
    url: str,
    config: Optional[LoaderConfig] = None
) -> Document:
    """
    TODO: Load content from a web page.
    
    Requirements:
    - Fetch HTML content from URL
    - Extract main content (remove nav, footer, ads)
    - Convert HTML to clean text
    - Preserve important formatting (headers, lists)
    - Extract title, description from meta tags
    - Store URL and fetch timestamp in metadata
    
    Args:
        url: The web page URL to fetch
        config: Optional loader configuration
        
    Returns:
        Document with page content and metadata
        
    Example:
        >>> doc = load_web_page("https://example.com/article")
        >>> print(doc.metadata)
        {"source": "https://example.com/article", "title": "...", "fetched_at": "..."}
    """
    pass


def load_csv_documents(
    file_path: str,
    content_columns: List[str],
    metadata_columns: Optional[List[str]] = None,
    config: Optional[LoaderConfig] = None
) -> List[Document]:
    """
    TODO: Load CSV file and convert rows to documents.
    
    Requirements:
    - Read CSV with proper encoding handling
    - Combine specified columns into page_content
    - Use other columns as metadata
    - Handle missing values gracefully
    - Support custom column separators
    
    Args:
        file_path: Path to CSV file
        content_columns: Columns to combine for page_content
        metadata_columns: Columns to include in metadata
        config: Optional loader configuration
        
    Returns:
        List of Document objects (one per row)
        
    Example:
        >>> docs = load_csv_documents(
        ...     "products.csv",
        ...     content_columns=["name", "description"],
        ...     metadata_columns=["category", "price"]
        ... )
        >>> print(docs[0].page_content)
        "Widget Pro: A professional-grade widget..."
        >>> print(docs[0].metadata)
        {"category": "tools", "price": "29.99", "row": 0}
    """
    pass


def load_text_file(
    file_path: str,
    config: Optional[LoaderConfig] = None
) -> Document:
    """
    TODO: Load a plain text or markdown file.
    
    Requirements:
    - Read file with proper encoding
    - Detect and handle different line endings
    - Optionally preserve markdown formatting
    - Include file stats in metadata
    
    Args:
        file_path: Path to text file
        config: Optional loader configuration
        
    Returns:
        Document with file content
        
    Example:
        >>> doc = load_text_file("readme.md")
        >>> print(doc.metadata)
        {"source": "readme.md", "size_bytes": 1234, "encoding": "utf-8"}
    """
    pass


def load_directory(
    directory_path: str,
    glob_pattern: str = "**/*",
    config: Optional[LoaderConfig] = None
) -> List[Document]:
    """
    TODO: Load all supported documents from a directory.
    
    Requirements:
    - Recursively find files matching pattern
    - Use appropriate loader for each file type
    - Skip unsupported file types
    - Handle errors gracefully (don't fail on one bad file)
    - Track loading statistics
    
    Args:
        directory_path: Path to directory
        glob_pattern: Pattern to match files
        config: Optional loader configuration
        
    Returns:
        List of all loaded documents
        
    Example:
        >>> docs = load_directory("./documents", "**/*.pdf")
        >>> print(f"Loaded {len(docs)} documents")
    """
    pass


def extract_metadata(
    document: Document,
    extract_entities: bool = False,
    extract_keywords: bool = False
) -> Dict[str, Any]:
    """
    TODO: Extract or enhance metadata from a document.
    
    Requirements:
    - Calculate content statistics (word count, char count)
    - Detect language
    - Optionally extract named entities
    - Optionally extract keywords/key phrases
    - Preserve existing metadata
    
    Args:
        document: Document to analyze
        extract_entities: Whether to extract named entities
        extract_keywords: Whether to extract keywords
        
    Returns:
        Enhanced metadata dictionary
        
    Example:
        >>> metadata = extract_metadata(doc, extract_keywords=True)
        >>> print(metadata)
        {"word_count": 500, "language": "en", "keywords": ["AI", "machine learning"]}
    """
    pass


def clean_document_text(
    document: Document,
    remove_extra_whitespace: bool = True,
    remove_special_chars: bool = False,
    lowercase: bool = False
) -> Document:
    """
    TODO: Clean and normalize document text.
    
    Requirements:
    - Remove extra whitespace and newlines
    - Fix common encoding issues
    - Optionally remove special characters
    - Optionally convert to lowercase
    - Return new document (don't modify original)
    
    Args:
        document: Document to clean
        remove_extra_whitespace: Collapse multiple spaces/newlines
        remove_special_chars: Remove non-alphanumeric chars
        lowercase: Convert to lowercase
        
    Returns:
        New Document with cleaned content
    """
    pass


def create_document_pipeline(
    loaders: List[str],
    transformations: List[str]
) -> Any:
    """
    TODO: Create a reusable document processing pipeline.
    
    Requirements:
    - Chain multiple loaders for different file types
    - Apply transformations in sequence
    - Support lazy loading for large document sets
    - Provide progress tracking
    
    Args:
        loaders: List of loader types to use
        transformations: List of transformations to apply
        
    Returns:
        Pipeline object that can process documents
        
    Example:
        >>> pipeline = create_document_pipeline(
        ...     loaders=["pdf", "web", "csv"],
        ...     transformations=["clean", "extract_metadata"]
        ... )
        >>> docs = pipeline.process("./documents")
    """
    pass


def validate_document(document: Document) -> Dict[str, Any]:
    """
    TODO: Validate a document for RAG processing.
    
    Requirements:
    - Check content is not empty
    - Verify required metadata fields exist
    - Check content length is within bounds
    - Detect potential issues (encoding, formatting)
    
    Args:
        document: Document to validate
        
    Returns:
        Validation result with is_valid, issues list
        
    Example:
        >>> result = validate_document(doc)
        >>> print(result)
        {"is_valid": True, "issues": [], "warnings": ["Content is very short"]}
    """
    pass


def merge_documents(
    documents: List[Document],
    separator: str = "\n\n"
) -> Document:
    """
    TODO: Merge multiple documents into one.
    
    Requirements:
    - Combine page_content with separator
    - Merge metadata appropriately
    - Track source documents in metadata
    
    Args:
        documents: Documents to merge
        separator: Text between documents
        
    Returns:
        Single merged document
    """
    pass
