# Contributing to Reindexer Vector Store for LangChain

First off, thank you for considering contributing to this project! It's people like you that make this integration possible.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

This section guides you through submitting a bug report. Following these guidelines helps maintainers and the community understand your report, reproduce the behavior, and find related reports.

Before creating bug reports, please check the issue tracker as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* Use a clear and descriptive title for the issue to identify the problem.
* Describe the exact steps which reproduce the problem in as many details as possible.
* Provide specific examples to demonstrate the steps.

### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion, including completely new features and minor improvements to existing functionality.

* Use a clear and descriptive title for the issue to identify the suggestion.
* Provide a step-by-step description of the suggested enhancement in as many details as possible.
* Provide specific examples to demonstrate the steps.

### Pull Requests

The process described here has several goals:

* Maintain the project's quality
* Fix problems that are important to users
* Engage the community in working toward the best possible integration
* Enable a sustainable system for the project's maintainers to review contributions

Please follow these steps to have your contribution considered by the maintainers:

1. Follow all instructions in the template
2. After you submit your pull request, verify that all status checks are passing

While the prerequisites above must be satisfied prior to having your pull request reviewed, the reviewer(s) may ask you to complete additional design work, tests, or other changes before your pull request can be ultimately accepted.

## Development Setup

1. Fork the repository
2. Clone your fork: `git clone https://github.com/your-username/reindexer-langchain-community.git`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
5. Install the package in development mode: `pip install -e .[dev]`
6. Run tests: `python -m pytest tests/`

## Style Guide

This project uses ruff for code formatting and linting. Please ensure your code follows these guidelines:

* Use 88 characters as the line length limit
* Follow PEP 8 style guide for Python code
* Write docstrings for all public methods and classes
* Use type hints where possible

To format your code, run: `ruff format .`

To check for linting issues: `ruff check .`

## Testing

All contributions must include tests. The project uses pytest for testing.

* Write tests for any new functionality
* Ensure all existing tests pass: `python -m pytest tests/`
* Aim for high test coverage

## Documentation

All public APIs should be documented with docstrings following the Google Python Style Guide.

## License

By contributing, you agree that your contributions will be licensed under the GPL-3.0 License.