# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A personal self-study log: a .NET backend/fullstack developer learning Python from scratch on the way to AI engineering. [README.md](README.md) is the source of truth for the curriculum — a week-by-week, day-by-day plan (Week 0 setup + 17 weeks, 3 h/day Mon–Fri) with checkboxes and a progress table. When asked "what's next" or to work on a given day, read the matching `Week N` / `D1`–`D5` entry there. The README also has a .NET → Python cheat sheet; use those mappings (FastAPI for ASP.NET Core, pytest for xUnit, `Protocol` for interfaces, etc.) when explaining concepts.

## Layout

- One top-level folder per week/phase (`00-setup/` … `15-typescript-ui/`, `capstone/`). Each has a `NOTES.md` with `Learned` / `Broke` / `Revisit` sections that the user fills in.
- Inside a week, work is split by day: `01-python-fundamentals/d1/` … `d5/`.
- Early days (d1–d4) are loose standalone scripts with no project file. Scripts in the same day folder import each other by bare module name (e.g. `d3/main.py` does `from text_utils import ...`), so run them from inside that folder.
- From D5 onward, exercises become `uv` projects (`uv init --package` style: `pyproject.toml`, `src/<name>/__init__.py`, `uv_build` backend, `requires-python >=3.13`, a `[project.scripts]` entry point pointing at `<name>:main`). Examples: `00-setup/hello/`, `01-python-fundamentals/d5/todo/`.
- `HELLWORLD/` is a stray scratch file outside the week structure.

## Commands

There is no root-level project, test suite, or CI. Commands are run per folder.

```sh
# Standalone scripts (d1–d4)
cd 01-python-fundamentals/d3 && python main.py

# uv projects (d5 onward)
cd 01-python-fundamentals/d5/todo
uv sync
uv run todo            # runs the [project.scripts] entry point
uv add <pkg>           # add a dependency

# Lint / type-check (ruff and mypy are not installed globally; use uvx or add as dev deps)
uvx ruff check .
uvx ruff format .
uvx mypy .
```

Once pytest is introduced (Week 2 D3): `uv run pytest`, single test with `uv run pytest path/to/test_file.py::test_name`.

## Code conventions already in use

The Friday review checklist in the README defines the bar: type hints everywhere, ruff and mypy clean, tests on main paths, no silently swallowed errors, logging where it matters, no god files. Existing code also follows:

- `from __future__ import annotations` at the top of modules with classes.
- Full type hints including `-> None`, and one-line docstrings on public functions/classes.
- Scripts expose a `main()` guarded by `if __name__ == "__main__":`.
- `Decimal` (not `float`) for money; immutable value objects as `@dataclass(frozen=True)`.
- Domain errors as a small exception hierarchy with a common base class (see `01-python-fundamentals/d4/bank.py`).
