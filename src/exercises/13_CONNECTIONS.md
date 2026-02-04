# Exercise 13: Document Loading - CONNECTIONS

## Before You Start (5 minutes)

### What Do You Already Know?

Take a moment to reflect on these questions:

1. **Have you ever opened different file types in Python?**
   - PDFs, CSVs, text files - each needs different handling.

2. **Do you know about web scraping?**
   - Fetching and extracting content from web pages.

3. **Have you dealt with file encodings?**
   - UTF-8, Latin-1, and why "special characters" sometimes break.

### Real-World Analogy

Think of Document Loading like a **Library Intake System**:

```
┌─────────────────────────────────────────────────────────────┐
│                THE LIBRARY INTAKE ANALOGY                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Different materials arrive at the library:                  │
│                                                              │
│  📄 PDF Reports → Special scanner for digital docs          │
│  🌐 Web Articles → Print from website, file properly        │
│  📊 CSV Data → Convert spreadsheet to readable format       │
│  📝 Text Files → Simple, just catalog and shelve            │
│                                                              │
│  Each type needs:                                            │
│  1. Different intake process (loader)                        │
│  2. Proper cataloging (metadata)                             │
│  3. Consistent format for readers (Document)                 │
│                                                              │
│  RAG Document Loading = Library intake + cataloging          │
│  Turn any source into searchable, retrievable documents      │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Why Document Loading Matters for RAG

```
RAG Pipeline:
                        ┌─────────────────────┐
Raw Sources ──────────▶│  Document Loading   │────────▶ Structured Documents
                        └─────────────────────┘
  • PDFs                    (This exercise!)           • Clean text
  • Websites                                           • Metadata  
  • Databases                                          • Source info
  • Emails                                             • Ready for chunking
```

### Prerequisite Checklist

Before starting this exercise, make sure you:

- [ ] Completed Exercises 01-12 (LangChain foundations)
- [ ] Understand file I/O in Python
- [ ] Know about different file encodings
- [ ] Have basic understanding of HTML structure

### Connect to Your Goal

**Building the Best RAG System**: Document loading is the first step!

```
Your knowledge base might include:
┌─────────────────────────────────────────────────────────────┐
│  • Product manuals (PDF) - Technical specifications          │
│  • Support articles (Web) - Troubleshooting guides          │
│  • Customer data (CSV) - Purchase history, preferences      │
│  • Internal docs (MD/TXT) - Policies, procedures            │
│  • Emails (various) - Customer communications               │
└─────────────────────────────────────────────────────────────┘

All must be converted to Documents with:
  • page_content: The searchable text
  • metadata: Source, date, category, etc.
```

### Warm-Up Activity

Before coding, think about your RAG knowledge base:

1. **What document types do you need to support?**
   - _____________________
   - _____________________
   - _____________________

2. **What metadata is important for each type?**
   - PDFs: page number, title, author
   - Web: URL, fetch date, title
   - CSV: row number, column headers
   - Your additions: _____________________

3. **What quality issues might you encounter?**
   - _____________________

---

**Ready?** Now proceed to `13_document_loading.py` and implement the functions!
