from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_required_project_directories_exist() -> None:
    """Project should contain the main professional directories."""

    required_directories = [
        "app",
        "data",
        "data/sample_documents",
        "data/evaluation_set",
        "docs",
        "tests",
    ]

    for directory in required_directories:
        assert (PROJECT_ROOT / directory).is_dir(), f"Missing directory: {directory}"


def test_required_project_files_exist() -> None:
    """Project should contain the main setup and documentation files."""

    required_files = [
        "README.md",
        "pyproject.toml",
        ".env.example",
        ".gitignore",
        "LICENSE",
        "docs/architecture.md",
        "app/__init__.py",
    ]

    for file_path in required_files:
        assert (PROJECT_ROOT / file_path).is_file(), f"Missing file: {file_path}"