# LangChain Learning Exercise Repository

Learn LangChain through **18 progressive, test-driven exercises**—from beginner model invocation to production-ready RAG systems.

**Now featuring TBR (Training from the Back of the Room) methodology:**
- **CONNECTIONS** - Warm-up activities linking to prior knowledge
- **CONCEPTS** - Focused mini-guides with visual diagrams
- **CONCRETE PRACTICE** - Hands-on coding exercises with tests
- **CONCLUSIONS** - Reflection prompts and skill checklists

## Installation

### Prerequisites

- **Python 3.10+** - [Download](https://www.python.org)
- **uv** - Fast Python package installer ([Install Guide](https://docs.astral.sh/uv/getting-started/installation/))
- **Git** - Optional, for cloning

### Step 1: Get the Repository

```bash
git clone https://github.com/YifangDONG/langchain-exercise.git
cd langchain-exercise
```

### Step 2: Install Dependencies

```bash
# Install uv (if not already installed)
pip install uv

# Sync all dependencies (automatically creates .venv and lockfile)
uv sync --all-groups

# Or sync specific dependency groups
uv sync --group dev --group providers
```

**What `uv sync` does:**
- Creates `.venv/` virtual environment (no manual activation needed!)
- Creates/updates `uv.lock` for reproducible builds
- Installs all dependencies from pyproject.toml

### Step 3: Verify Setup

```bash
# Check pytest is available
uv run pytest --version

# Run a quick test
uv run pytest tests/test_01_model_basics.py::TestModelBasics::test_initialize_model -v

# Run all exercises
uv run pytest tests/ -v
```

## Environment Configuration

### API Keys (Optional)

Create a `.env` file for API keys (copy from [.env.example](.env.example)):

```bash
# .env
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
GOOGLE_API_KEY=...
LANGCHAIN_MOCK_MODE=false  # Set to true to use mocks
```

**Note**: Exercises use mocks by default. API keys only needed for testing with real models.

## What You'll Learn

This repository teaches LangChain through a **test-driven learning approach**. Each exercise contains:

- **TODO blocks** describing what to implement
- **Comprehensive test suite** validating your implementation
- **Progressive difficulty** building from basics to advanced patterns
- **Real-world concepts** from production LangChain applications

## 18 Exercises Overview

### 🟢 Beginner Level - LangChain Foundations (Week 1)
| # | Exercise | Topics | Time |
|---|----------|--------|------|
| 1 | Model Basics | init, invoke, stream, batch | 1-2h |
| 2 | Messages | Message types, conversation history | 1-2h |
| 3 | Tool Definition | @tool decorator, schemas | 1-2h |
| 4 | Basic Agents | ReAct pattern, agent creation | 2-3h |

**Learn**: Initialize models, build conversations, create tools, invoke agents.

### 🟡 Intermediate Level - Production Patterns (Week 2)
| # | Exercise | Topics | Time |
|---|----------|--------|------|
| 5 | Tool Execution | Execution loops, error handling | 2-3h |
| 6 | Advanced Tools | Runtime context, state, filtering | 2-3h |
| 7 | Structured Output | Pydantic, validation, parsing | 2-3h |
| 8 | System Prompts | Static/dynamic prompts, engineering | 2-3h |

**Learn**: Execute tools safely, manage state, validate outputs, engineer prompts.

### 🔴 Advanced Level - Complex Systems (Week 3)
| # | Exercise | Topics | Time |
|---|----------|--------|------|
| 9 | Streaming | Real-time tokens, events | 2-3h |
| 10 | Memory & State | Persistence, retrieval, checkpoints | 3-4h |
| 11 | Middleware | Custom hooks, monitoring | 2-3h |
| 12 | Complex Workflows | Multi-agent, orchestration | 3-4h |

**Learn**: Stream responses, manage memory, customize behavior, build multi-agent systems.

### 🚀 RAG Deep Dive - Build Production RAG (Week 4)
| # | Exercise | Topics | Time |
|---|----------|--------|------|
| 13 | Document Loading | PDF, web, CSV loaders | 2-3h |
| 14 | Text Chunking | Splitters, overlap, tokens | 2-3h |
| 15 | Embeddings & Vectors | FAISS, Chroma, similarity | 2-3h |
| 16 | Retrieval Chains | Basic RAG, multi-query | 3-4h |
| 17 | Advanced RAG | Reranking, hybrid, HyDE | 3-4h |
| 18 | RAG Evaluation | Metrics, RAGAS, A/B testing | 3-4h |

**Learn**: Build production-quality RAG systems from document loading to evaluation.

## Learning Philosophy (TBR Methodology)

This repository uses **Training from the Back of the Room** (TBR) methodology:

### The 4 C's Framework

```
┌────────────────────────────────────────────────────────────────────┐
│  1. CONNECTIONS (5 min)  │  Connect to what you already know       │
│     📖 Read: XX_CONNECTIONS.md before starting                     │
├────────────────────────────────────────────────────────────────────┤
│  2. CONCEPTS (15 min)    │  Learn new concepts with visuals        │
│     📖 Read: docs/concepts/XX_*.md                                 │
├────────────────────────────────────────────────────────────────────┤
│  3. CONCRETE PRACTICE    │  Hands-on coding with tests             │
│     💻 Code: src/exercises/XX_*.py                                 │
│     🧪 Test: pytest tests/test_XX_*.py                             │
├────────────────────────────────────────────────────────────────────┤
│  4. CONCLUSIONS (5 min)  │  Reflect and celebrate learning         │
│     📖 Read: XX_CONCLUSIONS.md after completing                    │
└────────────────────────────────────────────────────────────────────┘
```

### Core Principles

✅ **Test-Driven**: Implement functions to pass comprehensive tests  
✅ **Progressive**: Build from basics to production RAG systems  
✅ **Visual**: Diagrams and analogies for every concept  
✅ **Practical**: Real-world scenarios and patterns  
✅ **Self-Paced**: Work through exercises at your own speed  
✅ **Hints Available**: Get unstuck with progressive hints  

## IDE Setup (Optional)

### Visual Studio Code

1. **Install Python Extension**
   - Extensions → Search "Python" → Install by Microsoft

2. **Select Python Interpreter**
   - Ctrl+Shift+P → "Python: Select Interpreter"
   - Choose `./.venv/bin/python`

3. **Configure Pytest**
   - Settings → Search "pytest"
   - Set Python Testing to "pytest"

4. **Recommended Extensions**
   - Pylance (type checking)
   - Black Formatter (code formatting)

### PyCharm

1. **Open Project Settings**
   - File → Settings → Project → Python Interpreter

2. **Add Interpreter**
   - Click gear → Add...
   - Select "Existing Environment" → Choose `.venv/bin/python`

3. **Enable Pytest**
   - File → Settings → Tools → Python Integrated Tools
   - Set Default Test Runner to "pytest"

### Command Line (Vim/Nano/etc)

```bash
# Just use uv run with pytest
uv run pytest tests/ -v
```

## How to Use This Repository

### TBR Learning Workflow

1. **CONNECTIONS - Warm Up (5 min)**
   ```bash
   # Read the connections file first
   cat src/exercises/01_CONNECTIONS.md
   ```
   - Reflect on prior knowledge
   - Understand the real-world analogy
   - Check prerequisites

2. **CONCEPTS - Learn (15 min)**
   ```bash
   # Read the focused concept guide
   cat docs/concepts/01_model_basics.md
   ```
   - Study the visual diagrams
   - Review code examples
   - Understand key takeaways

3. **CONCRETE PRACTICE - Code (30-60 min)**
   ```bash
   # Open and implement the exercise
   code src/exercises/01_model_basics.py
   
   # Run tests as you go
   uv run pytest tests/test_01_model_basics.py -v
   ```
   - Fill in the `pass` statements
   - Use hints if stuck (see below)
   - Iterate until tests pass ✅

4. **CONCLUSIONS - Reflect (5 min)**
   ```bash
   # Read the conclusions file
   cat src/exercises/01_CONCLUSIONS.md
   ```
   - Check off skills learned
   - Answer reflection questions
   - Review mini-project challenge

### Using the Hints System

If you get stuck, use the progressive hints:

```python
# In Python REPL or Jupyter
from src.utils.hints import hint, HintHelper

# Get a hint for any function
hint("initialize_model")       # First hint
hint("initialize_model", 2)    # Second hint

# Or use interactive helper
helper = HintHelper("basic_rag_chain")
helper.next()    # Get hints one at a time
helper.next()
helper.approach() # See solution approach
```

### Exercise Structure
```python
"""
Exercise NN: Topic Name
=======================
LEVEL: [Beginner/Intermediate/Advanced]

GOAL: Clear learning objective

TODO:
1. Task description
2. Task description
3. Implementation task

CONCEPTS TO LEARN:
- Concept 1: Description
- Concept 2: Description
"""

def function_to_implement():
    """
    TODO: Brief description of what to do
    
    Requirements:
    - Requirement 1
    - Requirement 2
    """
    pass
```

### Debug Tips

```bash
# See detailed output with print statements
uv run pytest tests/test_01_model_basics.py -vv -s

# Stop on first failure
uv run pytest tests/test_01_model_basics.py -x

# Show local variables on failure
uv run pytest tests/test_01_model_basics.py -l

# Run with pdb debugger
uv run pytest tests/test_01_model_basics.py --pdb

# Run specific test function
uv run pytest tests/test_01_model_basics.py::TestModelBasics::test_invoke_model
```

## Running Tests

### All Tests
```bash
uv run pytest tests/ -v
```

### By Difficulty
```bash
uv run pytest tests/ -m beginner      # Exercises 1-4
uv run pytest tests/ -m intermediate  # Exercises 5-8  
uv run pytest tests/ -m advanced      # Exercises 9-18 (includes RAG)
```

### RAG Exercises Only
```bash
uv run pytest tests/test_13*.py tests/test_14*.py tests/test_15*.py tests/test_16*.py tests/test_17*.py tests/test_18*.py -v
```

### Specific Exercise
```bash
uv run pytest tests/test_01_model_basics.py -v
```

### Specific Test
```bash
uv run pytest tests/test_01_model_basics.py::TestModelBasics::test_invoke_model -v
```

### With Coverage
```bash
uv run pytest tests/ --cov=src --cov-report=html
# Open htmlcov/index.html
```

## Project Structure

```
langchain-exercise/
├── src/
│   ├── exercises/           # 18 exercise files with TODOs
│   │   ├── 01_model_basics.py
│   │   ├── 01_CONNECTIONS.md   # TBR: Prior knowledge warm-up
│   │   ├── 01_CONCLUSIONS.md   # TBR: Reflection & celebration
│   │   ├── ...
│   │   ├── 12_advanced_workflows.py
│   │   ├── 13_document_loading.py     # RAG: Document ingestion
│   │   ├── 14_text_chunking.py        # RAG: Chunking strategies
│   │   ├── 15_embeddings_vectorstores.py  # RAG: Vector search
│   │   ├── 16_retrieval_chains.py     # RAG: RAG patterns
│   │   ├── 17_advanced_rag.py         # RAG: Reranking, HyDE
│   │   └── 18_rag_evaluation.py       # RAG: Metrics & testing
│   └── utils/               # Helper functions and fixtures
│       ├── helpers.py
│       ├── mock_data.py
│       ├── test_fixtures.py
│       └── hints.py         # Progressive hints system
├── tests/                   # Test suite for each exercise
│   ├── test_01_model_basics.py
│   ├── ...
│   └── test_18_evaluation.py
├── docs/
│   ├── CONCEPTS.md          # Master concepts document
│   ├── UV_GUIDE.md          # Package manager guide
│   └── concepts/            # Per-exercise concept guides
│       ├── 01_model_basics.md
│       ├── 13_document_loading.md
│       ├── 15_embeddings.md
│       └── ...
├── examples/                # Real-world example applications
│   ├── weather_agent.py
│   ├── research_assistant.py
│   └── data_processor.py
├── pyproject.toml           # Project configuration
├── pytest.ini               # Pytest configuration
└── README.md                # This file
```

## Using Mock Data

Exercises use mocks by default (no API calls needed):

```python
# tests/conftest.py provides mock_llm fixture
@pytest.fixture
def mock_llm():
    mock = Mock(spec=BaseChatModel)
    mock.invoke.return_value = AIMessage(content="Mock response")
    return mock
```

### Testing with Real APIs

After setting up `.env` with API keys:

```bash
# Use real API calls
LANGCHAIN_MOCK_MODE=false uv run pytest tests/test_01_model_basics.py -v
```

## Advanced Usage

### Update Dependencies

```bash
# Update all to latest versions
uv sync --upgrade

# Update specific package
uv lock --upgrade-package langchain

# View dependency tree
uv tree
```

For comprehensive uv documentation, see [docs/UV_GUIDE.md](docs/UV_GUIDE.md).

### Python Version Management

```bash
# Install pyenv
curl https://pyenv.run | bash

# Install and use Python 3.10
pyenv install 3.10.0
pyenv local 3.10.0
```

## Troubleshooting

### Import Errors
```bash
# Resync dependencies
uv sync --all-groups
```

### Mock vs Real API
```bash
# Use mocks (default, no API keys needed)
LANGCHAIN_MOCK_MODE=true uv run pytest tests/

# Use real API (set keys in .env)
LANGCHAIN_MOCK_MODE=false uv run pytest tests/
```

## Examples

After completing exercises, explore real-world applications:

```bash
# Weather agent with multiple tools
uv run python examples/weather_agent.py

# Research assistant with complex workflow
uv run python examples/research_assistant.py

# Batch data processor
uv run python examples/data_processor.py
```

## Documentation

- **[CONCEPTS.md](docs/CONCEPTS.md)** - Core LangChain concepts with Mermaid diagrams
- **[UV_GUIDE.md](docs/UV_GUIDE.md)** - Comprehensive uv package manager guide

## Learning Outcomes

After completing all 18 exercises, you'll understand:

### LangChain Foundations (Exercises 1-12)
- ✅ How to initialize and use LangChain models
- ✅ Message types and conversation management
- ✅ Creating and using tools effectively
- ✅ Building agents with ReAct pattern
- ✅ Tool execution and error handling
- ✅ Dynamic tool selection and state management
- ✅ Structured outputs with Pydantic
- ✅ System prompt engineering
- ✅ Real-time streaming responses
- ✅ Memory and state persistence
- ✅ Custom middleware and monitoring
- ✅ Multi-agent systems and orchestration

### RAG Mastery (Exercises 13-18)
- ✅ Loading documents from PDF, web, CSV, and more
- ✅ Text chunking strategies for optimal retrieval
- ✅ Creating embeddings and managing vector stores
- ✅ Building RAG chains (basic, conversational, multi-query)
- ✅ Advanced techniques (reranking, hybrid search, HyDE)
- ✅ Evaluating and optimizing RAG systems

**Goal Achieved**: Build production-quality RAG systems! 🎉

## Resources

- [LangChain Documentation](https://docs.langchain.com)
- [LangChain GitHub](https://github.com/langchain-ai/langchain)
- [Pydantic Documentation](https://docs.pydantic.dev)

## License

This project is open source and available under the MIT License.

## Key Features

🎯 **Test-Driven Learning** - Comprehensive test suites validate your work  
📚 **Progressive Difficulty** - Beginner → Intermediate → Advanced → RAG  
🔧 **Real-World Patterns** - Production-ready implementations, not toys  
💡 **TBR Methodology** - CONNECTIONS, CONCEPTS, PRACTICE, CONCLUSIONS  
🚀 **Complete RAG Curriculum** - From document loading to evaluation  
🤖 **Mock Support** - Test without API keys using intelligent mocks  
💬 **Progressive Hints** - Get unstuck without spoiling solutions  
📊 **Visual Learning** - Diagrams and analogies for every concept

---

## RAG Learning Path

If your goal is to build RAG systems, follow this optimized path:

```
Week 1: Foundations        Week 2: RAG Core           Week 3: Production RAG
┌──────────────────┐      ┌──────────────────┐      ┌──────────────────┐
│ Ex 1: Models     │      │ Ex 13: Loading   │      │ Ex 17: Advanced  │
│ Ex 2: Messages   │ ───▶ │ Ex 14: Chunking  │ ───▶ │ Ex 18: Evaluation│
│ Ex 7: Structured │      │ Ex 15: Vectors   │      │                  │
│ Ex 8: Prompts    │      │ Ex 16: RAG Chain │      │ Final Project!   │
└──────────────────┘      └──────────────────┘      └──────────────────┘
```

---

**Happy learning! 🚀**

Start with Exercise 1: `src/exercises/01_model_basics.py`

Or jump to RAG: `src/exercises/13_document_loading.py`
