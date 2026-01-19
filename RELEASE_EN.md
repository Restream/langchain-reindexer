# Release Cycle and Publishing Instructions

## Release Cycle

1. Update the version number in `pyproject.toml`
2. Update the version number in `setup.py` (if used)
3. Update `CHANGELOG.md` with information about the new release
4. Create and push a git tag with the new version
5. Publish the package to PyPI

## Preparing for Publication

1. Make sure all tests pass:
   ```
   python -m pytest tests/
   ```

2. Check code formatting:
   ```
   ruff format .
   ```

3. Check code for errors:
   ```
   ruff check .
   ```

4. Check typing:
   ```
   mypy langchain_reindexer/
   ```

## Publishing to PyPI

1. Install the necessary tools:
   ```
   pip install build twine
   ```

2. Build the distribution:
   ```
   python -m build
   ```

3. Check the distribution:
   ```
   twine check dist/*
   ```

4. Publish to TestPyPI (for testing):
   ```
   twine upload --repository testpypi dist/*
   ```

5. Check installation from TestPyPI:
   ```
   pip install --index-url https://test.pypi.org/simple/ langchain-reindexer
   ```

6. If everything works correctly, publish to PyPI:
   ```
   twine upload dist/*
   ```

## After Publication

1. Create a release on GitHub with the version tag
2. Update documentation if necessary
3. Notify the community about the new release