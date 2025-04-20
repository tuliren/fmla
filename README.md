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

### CLI Commands

FMLA provides several CLI commands to help navigate performance improvement plans:

```bash
# Show information about PIP
fmla info

# Show guide on dealing with PIP mentally
fmla guide

# Show information about FMLA and steps to take
fmla fmla
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
