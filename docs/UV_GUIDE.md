# Using uv for This Project

This project uses **uv** for fast, reliable Python package and project management.

## What is uv?

**uv** is a fast, modern Python package manager written in Rust that replaces pip, pip-tools, poetry, and other tools. Benefits:
- ⚡ **10-100x faster** than pip
- 🔒 **Reproducible builds** via `uv.lock`
- 📦 **Single tool** for all Python tasks
- 🔄 **Automatic venv management**
- 🌍 **Cross-platform** (Windows, macOS, Linux)

## Installation

```bash
# Install uv
pip install uv

# Verify installation
uv --version
```

## Key Commands

### First-Time Setup

```bash
# Clone and setup
git clone <repo-url>
cd langchain-exercise

# Sync all dependencies (creates .venv and uv.lock)
uv sync --all-groups
```

### Running Commands

```bash
# uv automatically manages the virtual environment!
uv run pytest tests/ -v           # Run tests
uv run black src/                 # Format code
uv run ruff check src/            # Check code style
uv run mypy src/                  # Type checking
```

**No need to activate venv manually** - uv handles it automatically!

### Managing Dependencies

```bash
# Add a new dependency
uv add requests

# Add a dev dependency
uv add --group dev pytest-cov

# Remove a dependency
uv remove requests

# Update all dependencies
uv sync --upgrade

# Update specific package
uv lock --upgrade-package requests
```

## Project Structure

```
.
├── .python-version      # Pinned Python version (e.g., "3.10")
├── .venv/               # Virtual environment (auto-created by uv)
├── pyproject.toml       # Project config & dependencies
├── uv.lock              # Exact versions for reproducibility
└── ...
```

### pyproject.toml

Defines:
- Project metadata (name, version, etc.)
- Dependencies in `[project]` section
- Optional groups: `providers`, `dev`, `test`
- Tool configurations: pytest, black, ruff, mypy

### uv.lock

- **Automatically generated** - don't edit manually
- **Commit to git** - ensures reproducible builds
- Lists exact versions for all dependencies
- Platform-independent

## Workflows

### Development Workflow

```bash
# 1. Setup
uv sync --all-groups

# 2. Make changes
# ... edit files ...

# 3. Test
uv run pytest tests/ -v

# 4. Format and lint
uv run black src/
uv run ruff check --fix src/

# 5. Type check
uv run mypy src/
```

### Adding Dependencies

```bash
# Add regular dependency (goes to pyproject.toml)
uv add langchain-anthropic

# Add dev dependency
uv add --group dev pytest-cov

# View dependencies
uv tree              # Tree view
uv pip list          # Pip-style list
```

### Running Exercises

```bash
# All tests
uv run pytest tests/ -v

# Specific exercise
uv run pytest tests/test_01_model_basics.py -v

# By difficulty level
uv run pytest tests/ -m beginner
uv run pytest tests/ -m intermediate
uv run pytest tests/ -m advanced

# Single test
uv run pytest tests/test_01_model_basics.py::TestModelBasics::test_invoke_model -v

# With print output
uv run pytest tests/ -v -s
```

## Advanced Usage

### Python Version Management

```bash
# Check .python-version
cat .python-version

# Pin a specific Python version
uv python pin 3.11

# Install multiple Python versions
uv python install 3.10 3.11 3.12

# Run with specific Python
uv run --python 3.11 pytest tests/
```

### Exporting Lockfile

```bash
# Export to requirements.txt (for compatibility)
uv export --output-file requirements.txt

# Export with specific extras
uv export --group dev --output-file requirements-dev.txt
```

### Workspaces

For monorepo projects (not used here):
```bash
# Define workspaces in pyproject.toml
[tool.uv.workspace]
members = ["packages/*"]
```

## Troubleshooting

### uv not found

```bash
# Install uv globally
pip install uv

# Or use curl (macOS/Linux)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or use PowerShell (Windows)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Virtual environment issues

```bash
# Recreate virtual environment
rm -rf .venv
uv sync

# Or force sync
uv sync --force
```

### Dependency conflicts

```bash
# Check dependency tree
uv tree

# Update specific package
uv lock --upgrade-package package_name

# Full dependency update
uv sync --upgrade
```

## Comparison with Other Tools

| Task | uv | pip | poetry | pip-tools |
|------|----|----|--------|-----------|
| Install deps | `uv sync` | `pip install` | `poetry install` | `pip-sync` |
| Add package | `uv add pkg` | `pip install pkg` | `poetry add pkg` | Manual |
| Lockfile | `uv.lock` | `requirements.txt` | `poetry.lock` | `requirements.txt` |
| Speed | ⚡⚡⚡ | ⚡ | ⚡⚡ | ⚡⚡ |
| Virtual env | Auto | Manual | Auto | Manual |

## Resources

- **Official Docs**: https://docs.astral.sh/uv/
- **GitHub**: https://github.com/astral-sh/uv
- **Why uv?**: https://astral.sh/blog/uv
- **Migration Guide**: https://docs.astral.sh/uv/guides/migration/

## Best Practices

✅ **Do:**
- Commit `uv.lock` to version control
- Use `uv sync --all-groups` for full setup
- Use `uv run` for all commands
- Pin Python version in `.python-version`
- Keep `pyproject.toml` organized

❌ **Don't:**
- Edit `uv.lock` manually
- Mix pip and uv commands
- Manually manage venv activation
- Commit `.venv/` to git
- Use old Python versions without reason
