# Modern Python Development with UV: A Practical Guide

## Introduction

UV is a blazingly fast Python package installer and resolver written in Rust. In this tutorial, we'll explore how to use UV to manage Python projects efficiently, from initial setup to dependency management and daily development workflows.

## Prerequisites

- Basic familiarity with Python and command line
- UV installed on your system (installation instructions vary by platform)

## Part 1: Project Setup

Let's create a web application project to demonstrate UV's capabilities. We'll build a simple Flask API with proper testing and development tools.

```bash
# Create a new project directory
mkdir awesome-api
cd awesome-api

# Initialize a new Python project
uv init

# Create a virtual environment
uv venv

# Activate the virtual environment
# On Unix/MacOS:
source .venv/bin/activate
# On Windows:
# .venv\Scripts\activate
```

After activating the virtual environment, your prompt should change to indicate that you're working within the virtual environment. For example:
```
(.venv) user@computer:~/awesome-api$
```

> **Note**: Remember to always activate your virtual environment when working on your project. This ensures you're using the project-specific Python interpreter and packages.

After running these commands, UV creates a `pyproject.toml` file for your project configuration. This is where your project metadata and dependencies will be stored.

## Part 2: Managing Dependencies

Let's add the dependencies we'll need for our project:

```bash
# Add production dependencies
uv add flask sqlalchemy python-dotenv

# Add development dependencies
uv add --dev pytest pytest-cov black mypy isort

# Create a lock file to pin exact versions
uv lock

# Sync the environment with locked dependencies
uv sync
```

### Understanding the Commands
- `uv add`: Adds packages to your project
- `uv add --dev`: Adds development-only dependencies
- `uv lock`: Creates/updates the lock file with exact versions
- `uv sync`: Ensures your environment matches the lock file

## Part 3: Project Structure

Let's create a basic project structure:

```bash
# Create project directories
mkdir awesome_api
mkdir tests

# Create main application file
cat > awesome_api/__init__.py << EOL
from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return {"message": "Welcome to Awesome API!"}

    return app
EOL

# Create a test file
cat > tests/test_app.py << EOL
import pytest
from awesome_api import create_app

@pytest.fixture
def app():
    return create_app()

@pytest.fixture
def client(app):
    return app.test_client()

def test_hello_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["message"] == "Welcome to Awesome API!"
EOL
```

## Part 4: Development Workflow

Now let's see how UV helps in daily development tasks:

### Running Tests
```bash
# Run tests with pytest
uv run pytest

# Run tests with coverage
uv run pytest --cov=awesome_api
```

### Code Formatting and Type Checking
```bash
# Format code with black
uv run black awesome_api tests

# Run type checking
uv run mypy awesome_api

# Sort imports
uv run isort .
```

### Dependency Management

```bash
# View dependency tree
uv tree

# Check for dependency conflicts
uv pip check

# Add new dependencies as needed
uv add pydantic
uv lock  # Update lock file
uv sync  # Sync environment
```

## Part 5: Advanced Features

### Using UV's Cache
```bash
# View cache location
uv cache dir

# Clean cache if needed
uv cache clean
```

### Package Information
```bash
# View detailed package info
uv pip show flask

# List all installed packages
uv pip list
```

### Python Version Management
```bash
# List available Python versions
uv python list

# Install a specific Python version
uv python install 3.11
```

## Best Practices

1. **Always Use Lock Files**: Commit your lock file to version control to ensure reproducible builds.
   ```bash
   uv lock
   git add pyproject.toml uv.lock
   ```

2. **Regular Environment Sync**: After pulling changes or updating dependencies:
   ```bash
   git pull
   uv sync
   ```

3. **Clean Environment**: If you suspect environment issues:
   ```bash
   uv pip uninstall --all
   uv sync
   ```

4. **Development Tools**: Use UV's run command for development tools:
   ```bash
   uv run black .
   uv run pytest
   ```

## Troubleshooting

### Common Issues and Solutions

1. **Virtual Environment Issues**
   ```bash
   # If virtual environment seems corrupted
   deactivate  # First deactivate if it's active
   rm -rf .venv  # Remove the old environment
   uv venv  # Create a new environment
   source .venv/bin/activate  # Activate it
   uv sync  # Reinstall all dependencies
   ```

2. **Lock File Conflicts**
   ```bash
   uv lock --refresh  # Regenerate lock file from scratch
   ```

2. **Missing Dependencies**
   ```bash
   uv pip check  # Check for missing dependencies
   uv sync  # Resync environment
   ```

3. **Cache Issues**
   ```bash
   uv cache clean  # Clean the cache
   uv sync  # Resync environment
   ```

## Conclusion

UV provides a modern, fast, and efficient way to manage Python projects. Its integration of project management, dependency resolution, and development tools makes it a powerful choice for Python development.

Key benefits:
- Fast dependency resolution
- Reliable environment management
- Integrated development tools
- Modern project structure

Remember to regularly update UV itself:
```bash
uv self update
```

This tutorial covered the basics of using UV for Python development. As you continue working with UV, you'll discover more features and workflows that can enhance your development process.

## Additional Resources

- UV Documentation
- Python Packaging Guide
- Modern Python Development Best Practices

Happy coding with UV! 🚀
