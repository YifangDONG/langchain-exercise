# Concept Guide: Document Loading

## Key Concepts

1. **Different sources need different loaders** - PDF, web, CSV all handled differently
2. **Metadata is crucial** - Source, page, date enables filtering and citations
3. **Clean text improves retrieval** - Remove artifacts, normalize whitespace
4. **Documents are the RAG foundation** - Everything builds on good loading

## Visual: Document Loading Pipeline

```
┌─────────────────────────────────────────────────────────────┐
│                  DOCUMENT LOADING PIPELINE                   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   Raw Sources                 Loaders              Documents │
│                                                              │
│   📄 PDF ──────────────▶ PDFLoader ──────┐                  │
│                                           │                  │
│   🌐 Web ──────────────▶ WebLoader ──────┼──▶ [Document]    │
│                                           │     page_content │
│   📊 CSV ──────────────▶ CSVLoader ──────┤     metadata     │
│                                           │                  │
│   📝 Text ─────────────▶ TextLoader ─────┘                  │
│                                                              │
│   Each loader:                                               │
│   • Extracts text content                                    │
│   • Captures metadata (source, page, date)                  │
│   • Handles encoding issues                                  │
│   • Returns standardized Document objects                   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Code Example

```python
from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class Document:
    page_content: str
    metadata: Dict[str, Any]

# PDF Loading
docs = load_pdf("manual.pdf")
# Returns: [
#   Document(page_content="Chapter 1...", metadata={"source": "manual.pdf", "page": 1}),
#   Document(page_content="Chapter 2...", metadata={"source": "manual.pdf", "page": 2}),
# ]

# Web Loading
doc = load_web("https://example.com/article")
# Returns: Document(
#   page_content="Article text...",
#   metadata={"source": "https://...", "title": "...", "fetched_at": "..."}
# )

# CSV Loading
docs = load_csv("products.csv", content_cols=["name", "description"])
# Returns one Document per row
```

## Metadata Importance

```
WITHOUT METADATA:
Query: "What's the warranty?"
Result: "The warranty is 2 years"
User: "Where did this come from?" 🤷

WITH METADATA:
Query: "What's the warranty?"
Result: "The warranty is 2 years"
        Source: warranty_policy.pdf, Page 5, Updated: 2024-01-15
User: "I can verify this!" ✓
```

## Teach-Back

Explain in your own words:
1. Why can't we use the same code to load PDFs and websites?
2. What metadata would you capture for a support ticket database?
3. How does good document loading affect RAG quality?
