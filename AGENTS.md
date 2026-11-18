# RowDelta contributor instructions

RowDelta is an open-source Python 3.12+ command-line utility for comparing, validating, and analyzing large CSV datasets. Keep the core engine independent from CLI and file I/O, favor simple typed interfaces, deterministic behavior, and graceful malformed-input handling. Do not claim performance properties without benchmarks. Synthetic, non-proprietary data only.

## Learning assignments

The user is building algorithmic skills and has about 30 minutes per day. When asked for a daily assignment:

1. Implement only the supporting infrastructure needed for the task.
2. Assign exactly one algorithmic function, with a descriptive name, complete typed signature, detailed docstring, examples, edge cases, acceptance criteria, automated tests, and a `NotImplementedError` placeholder.
3. Do not implement the assigned algorithm or reveal its solution, pseudocode, or a recommended algorithm unless the user explicitly asks for a hint.
4. Keep the task achievable in about 30 minutes and update `ROADMAP.md`.
5. After the user implements it, review correctness, readability, time and space complexity, and edge cases. Do not rewrite their algorithm without permission.

Do not build the entire algorithm roadmap in advance. Keep unfinished features clearly labeled. Do not add or run tests unless the user asks to test or verify implementation.

## Engineering workflow

- Keep dependencies minimal and use strong typing.
- Use pytest and Hypothesis for tests, Ruff for linting and formatting, and strict mypy for type checking.
- Preserve deterministic output and handle malformed CSV input with useful errors.
- Use synthetic data for fixtures and benchmarks.
