"""Allow cookiecutter to be executable through `python -m awesome-cookiecutter`."""

from beautiful_cookiecutter.cli import main

if __name__ == "__main__":
    main(prog_name="beautiful_cookiecutter")