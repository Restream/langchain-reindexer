"""Setup script for local development and testing."""

from setuptools import find_packages, setup

setup(
    name="langchain-community-reindexer",
    version="0.1.0",
    description="Reindexer vector store integration for LangChain",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Parviz Mirzoev",
    author_email="parviz.mirzoev@restream.ru",
    packages=find_packages(),
    install_requires=[
        "langchain-core>=0.1.0",
        "pyreindexer>=0.5.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
            "ruff>=0.1.0",
            "mypy>=1.0.0",
        ],
    },
    python_requires=">=3.8",
)