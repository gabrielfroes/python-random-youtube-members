from pathlib import Path
from shutil import rmtree

from invoke import task


def _remove_dirs(dirs):
    for a_dir in dirs:
        dir_path = Path(a_dir)
        if dir_path.exists() and dir_path.is_dir():
            print(f"Removing {a_dir}...")
            rmtree(a_dir, ignore_errors=False)


def _remove_globs(globs):
    for a_glob in globs:
        for a_file in Path(".").glob(a_glob):
            if str(a_file).startswith("venv"):
                continue
            print(f"Removing {a_file}...")
            file_path = Path(a_file)
            if file_path.exists() and file_path.is_file():
                a_file.unlink()
            elif file_path.exists() and file_path.is_dir():
                rmtree(a_file, ignore_errors=False)


@task
def tests(c):
    """
    Run unit tests.
    """
    c.run("python -m pytest tests -vv "
          "--cov=tests "
          "--cov=core "
          "--cov=main "
          "--cov-report term-missing:skip-covered "
          "-W ignore::DeprecationWarning")
    lint(c)


@task
def lint(c):
    """
    Run linting.
    """
    print("Linting...")
    c.run("flake8 "
          "core/ "
          "./main.py "
          "--max-complexity=5")
    c.run("flake8 tests --ignore=S101,S311,F811")
    print("\033[32mAll right!\033[0m")


@task
def clean_pyc(_c):
    """
    Remove Python file artifacts.
    """
    globs_to_remove = [
        "**/*.pyc",
        "**/*.pyo",
        "**/*~",
        "**/__pycache__",
    ]
    _remove_globs(globs_to_remove)


@task
def clean_test(_c):
    """
    Remove test and coverage artifacts.
    """
    remove_dirs = [
        ".tox",
        "htmlcov",
    ]
    remove_globs = [
        ".coverage",
        ".pytest_cache",
    ]
    _remove_dirs(remove_dirs)
    _remove_globs(remove_globs)


@task(clean_pyc, clean_test)
def clean(_c):
    """
    Remove all build, test, coverage and Python artifacts.
    """
    pass


@task(clean)
def install(c):
    """
    Install dependencies.
    """
    c.run("pip install -r requirements.txt")


@task(install)
def install_dev(c):
    """
    Install dependencies for development.
    """
    c.run("pip install -r requirements_dev.txt")


@task
def run(c):
    """
    Run the project.
    """
    c.run("python main.py")
