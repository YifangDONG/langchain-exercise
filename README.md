# LangChain Learning Exercise Repository

Learn LangChain through **12 progressive, test-driven exercises**—from beginner model invocation to advanced multi-agent systems.

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

## 12 Exercises Overview

### 🟢 Beginner Level (Week 1)
| # | Exercise | Topics | Time |
|---|----------|--------|------|
| 1 | Model Basics | init, invoke, stream, batch | 1-2h |
| 2 | Messages | Message types, conversation history | 1-2h |
| 3 | Tool Definition | @tool decorator, schemas | 1-2h |
| 4 | Basic Agents | ReAct pattern, agent creation | 2-3h |

**Learn**: Initialize models, build conversations, create tools, invoke agents.

### 🟡 Intermediate Level (Week 2)
| # | Exercise | Topics | Time |
|---|----------|--------|------|
| 5 | Tool Execution | Execution loops, error handling | 2-3h |
| 6 | Advanced Tools | Runtime context, state, filtering | 2-3h |
| 7 | Structured Output | Pydantic, validation, parsing | 2-3h |
| 8 | System Prompts | Static/dynamic prompts, engineering | 2-3h |

**Learn**: Execute tools safely, manage state, validate outputs, engineer prompts.

### 🔴 Advanced Level (Week 3)
| # | Exercise | Topics | Time |
|---|----------|--------|------|
| 9 | Streaming | Real-time tokens, events | 2-3h |
| 10 | Memory & State | Persistence, retrieval, checkpoints | 3-4h |
| 11 | Middleware | Custom hooks, monitoring | 2-3h |
| 12 | Complex Workflows | Multi-agent, orchestration | 3-4h |

**Learn**: Stream responses, manage memory, customize behavior, build multi-agent systems.

## Learning Philosophy

✅ **Test-Driven**: Implement functions to pass comprehensive tests  
✅ **Progressive**: Build from basics to advanced patterns  
✅ **Practical**: Real-world scenarios and patterns  
✅ **Self-Paced**: Work through exercises at your own speed  
✅ **Comprehensive**: All major LangChain features covered  

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

### Basic Workflow

1. **Open Exercise File**
   ```bash
   code src/exercises/01_model_basics.py
   ```

2. **Read TODO Blocks**
   - Each exercise has clear TODO comments
   - Understand requirements and hints
   - Review the CONCEPTS section

3. **Implement Functions**
   - Fill in the `pass` statements
   - Follow docstring requirements
   - Keep tests in mind

4. **Run Tests**
   ```bash
   uv run pytest tests/test_01_model_basics.py -v
   ```

5. **Fix Failures & Iterate**
   - Read test error messages carefully
   - Adjust implementation
   - Rerun tests until all pass ✅

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
uv run pytest tests/ -m advanced      # Exercises 9-12
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
│   ├── exercises/        # 12 exercise files with TODOs
│   │   ├── 01_model_basics.py
│   │   ├── 02_messages.py
│   │   ├── ...
│   │   └── 12_advanced_workflows.py
│   ├── utils/            # Helper functions and fixtures
│   │   ├── helpers.py
│   │   ├── mock_data.py
│   │   └── test_fixtures.py
│   └── solutions/        # Reference solutions (optional)
├── tests/                # Test suite for each exercise
│   ├── CONCEPTS.md       # Core LangChain concepts with diagrams
│   └── UV_GUIDE.md       # Comprehensive uv package manager guide
├── .env.example          # Example environment configurations
├── examples/             # Real-world example applications
│   ├── weather_agent.py
│   ├── research_assistant.py
│   └── data_processor.py
├── docs/                 # Detailed documentation
│   ├── SETUP.md
│   ├── CONCEPTS.md
│   └── UV_GUIDE.md
├── pyproject.toml        # Project configuration
├── pytest.ini            # Pytest configuration
└── README.md             # This file
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

After completing all 12 exercises, you'll understand:

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

## Resources

- [LangChain Documentation](https://docs.langchain.com)
- [LangChain GitHub](https://github.com/langchain-ai/langchain)
- [Pydantic Documentation](https://docs.pydantic.dev)

## License

This project is open source and available under the MIT License.

## Key Features

🎯 **Test-Driven Learning** - Comprehensive test suites validate your work  
📚 **Progressive Difficulty** - Beginner → Intermediate → Advanced  
🔧 **Real-World Patterns** - Production-ready implementations, not toys  
💡 **Clear Documentation** - Each exercise explains concepts and requirements  
🚀 **Practical Skills** - Learn patterns used in real LangChain applications  
🤖 **Mock Support** - Test without API keys using intelligent mocks  
📊 **Comprehensive Coverage** - All major LangChain features included

---

**Happy learning! 🚀**

Start with Exercise 1: `src/exercises/01_model_basics.py`
