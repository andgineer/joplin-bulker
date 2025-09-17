# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Joplin Bulker is a Python automation tool for legacy Joplin files (Export RAW format only - does not support modern SQLite versions). The project provides bulk operations on Joplin notes, primarily tag removal and Goodreads CSV import functionality.

**Important**: This project is archived/unmaintained as the author migrated to Obsidian and no longer uses Joplin.

## Architecture

- **Entry point**: Console script `joplin-bulker` defined in setup.py, mapped to `joplin_bulker.main:cli`
- **Main CLI**: `src/joplin_bulker/main.py` - Rich Click-based CLI with two main commands:
  - `tag --rm=<tag_name>` - Bulk tag removal (implemented in `src/joplin_bulker/tag.py`)
  - `import-goodreads <file>` - Import Goodreads CSV (implemented in `src/joplin_bulker/import_goodreads.py`)
- **Configuration**: `config.yaml` specifies Joplin folder path (defaults to `~/Downloads/Joplin`)
- **Dependencies**: Uses Joppy library for Joplin API communication, Rich Click for CLI

## Development Setup

### Environment Setup
```bash
. ./activate.sh
```
This script creates/activates a Python 3.12 virtual environment using Astral's UV and installs all dependencies.

### Available Commands

#### Testing
```bash
python -m pytest tests/
```

#### Linting and Formatting
```bash
ruff check --fix .        # Linting with auto-fix
ruff format .             # Code formatting
mypy src/                 # Type checking
pylint src/               # Additional linting
```

#### Pre-commit (runs ruff, mypy, pylint)
```bash
pre-commit run --all-files
```

#### Version Management
```bash
make version              # Show current version
make ver-bug             # Bump bug version
make ver-feature         # Bump feature version
make ver-release         # Bump release version
```

#### Dependency Management
```bash
make reqs                # Update all requirements and pre-commit hooks
```

## Key Implementation Details

- Python 3.9+ required (setup.py), but development uses Python 3.12
- Package structure follows src layout: `src/joplin_bulker/`
- Version managed in `src/joplin_bulker/version.py`
- Uses setuptools with requirements from `requirements.in`
- Pre-commit configured with ruff (linter/formatter), mypy (type checking), and pylint
- Tests located in `tests/` directory with pytest framework