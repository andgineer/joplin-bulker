# Repository Guidelines

## Project Structure & Module Organization
- `src/joplin_bulker/`: Python package and CLI entrypoints (e.g., `main.py`, `tag.py`).
- `tests/`: Pytest suites (`test_*.py`) and fixtures.
- `scripts/`: Maintenance utilities (e.g., version bump, requirements compile).
- Root files: `activate.sh` (dev env), `config.yaml` (app config), `Makefile` (helpers), `README.md`.

## Build, Test, and Development Commands
- Setup env: `. ./activate.sh` — creates/activates `.venv` via `uv`, installs deps, installs package in editable mode.
- CLI help: `joplin-bulker --help` — lists commands (`tag`, `import_goodreads`).
- Run locally: `joplin-bulker tag --rm=school` — removes tag “school” (requires `config.yaml` with `folder:` path).
- Tests: `pytest -q` — run unit tests; add `-k name` to filter.
- Lint/format: `pre-commit run -a` — runs Ruff (lint/format), MyPy, and Pylint using repo config.
- Coverage: `coverage run -m pytest && coverage html` — results in `htmlcov/`.
- Make helpers: `make help` to list; common: `make version`, `make reqs`.

## Coding Style & Naming Conventions
- Language: Python 3.12 (see `activate.sh`).
- Formatting: Ruff formatter; max line length 99 (`.ruff.toml`, `.pylintrc`).
- Indentation: 4 spaces; snake_case for modules/functions; CapWords for classes.
- Type hints: MyPy enabled with strict flags; prefer explicit types for public funcs.
- Linting: Pylint tuned via `.pylintrc`; use `pre-commit` before pushing.

## Testing Guidelines
- Framework: Pytest; place tests under `tests/` as `test_*.py`.
- Naming: test functions `test_<behavior>()`; fixtures in `tests/conftest.py`.
- Scope: cover parsing (`tag.parse_joplin`), CLI paths, and edge cases.
- Run selectively: `pytest -k parse` to focus; ensure green with coverage where practical.

## Commit & Pull Request Guidelines
- Commits: short, imperative subject (“upgrade requests”), reference issues when relevant (`#3`).
- Branches: concise, kebab-case (`fix-bad-parse`, `feature-goodreads-cleanup`).
- PRs: clear description, steps to reproduce, expected result; link issues; include screenshots/logs if UX-visible.
- Quality gates: CI should pass; run `pre-commit run -a` and `pytest` locally before requesting review.

## Security & Configuration Tips
- `config.yaml`: set `folder:` to your Joplin export dir before running destructive commands.
- Web Clipper: enable in Joplin Desktop for API-based features (see `README.md`).
