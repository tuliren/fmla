# FMLA

A Python package that displays a welcome message when imported.

## Installation

```bash
pip install fmla
```

## Usage

```python
import fmla
```

## Development

This project uses Poetry for dependency management.

```bash
# Install dependencies
poetry install

# Run tests
poetry run pytest

# Run linting
poetry run flake8 fmla
poetry run black fmla
poetry run isort fmla
poetry run mypy fmla
```
