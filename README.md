# PIP FMLA

A sarcastic Python package with CLI tools to help navigate Performance Improvement Plans (PIP) and Family Medical Leave Act (FMLA) situations. It displays a welcome message when imported and provides helpful commands for those facing workplace challenges.

## Installation

```bash
pip install fmla
```

## Usage

### Under commandline

FMLA provides CLI commands to help navigate performance improvement plans:

```bash
# Show information about PIP
fmla info

# Show guide on dealing with PIP mentally and FMLA information
fmla guide
```

### Programmatically

```python
import fmla
```

This package currently does not provide any programmatic functionality.

## Development

This project uses Poetry for dependency management.

```bash
# Install dependencies
poetry install

# Run commands locally
poetry run fmla info

# Run tests
poetry run pytest

# Run linting
poetry run flake8 fmla
poetry run black fmla
poetry run isort fmla
poetry run mypy fmla
```
