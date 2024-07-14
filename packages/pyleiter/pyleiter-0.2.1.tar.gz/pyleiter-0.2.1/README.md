# Pyleiter
Simple task manager for a Python project.

## Installation
Use your favorite virtualenv and python package manager. For instance, using pip:

```bash
pip install pyleiter
```

## Configuration and usage

Make sure your project has a 'pyproject.toml' file and add a section like the one below:

```toml
[tool.pyleiter.commands]
format = { command = "ruff format src", help = "Applies ruff format to project"}
lint = { command = "ruff check src", help = "Runs project formatter and linter" }
```

Where each line corresponds to a command you want to register for your program.

After that, you can use pyleiter with the registered commands:

```bash
pyleiter format
```

## Why use it?

Simply because every project requires simple maintenance scripts, and it is often done without a standardized way for Python projects.
By using a tool that leverages `pyproject.toml`, we can keep the configuration centralized.

## Similar (and better) projects

- https://github.com/nat-n/poethepoet
- https://github.com/omnilib/thx
