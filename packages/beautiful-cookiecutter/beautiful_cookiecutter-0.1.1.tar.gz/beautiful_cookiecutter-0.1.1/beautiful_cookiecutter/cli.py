"""Main `awecome_cookiecutter` CLI."""

from __future__ import annotations

import json
import os
from pprint import pprint
import sys
from collections import OrderedDict
from typing import Any, TYPE_CHECKING

# from awecome_cookiecutter import __version__
import click
import cookiecutter
import inquirer

if TYPE_CHECKING:
    from collections.abc import Iterable

    from click import Context, Parameter
    from typing_extensions import Literal

__version__ = '0.1.0'
def version_msg() -> str:
    """Return the Cookiecutter version, location and Python powering it."""
    python_version = sys.version
    location = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return f"Cookiecutter {__version__} from {location} (Python {python_version})"


def validate_extra_context(
    _ctx: Context, _param: Parameter, value: Iterable[str]
) -> OrderedDict[str, str] | None:
    """Validate extra context."""
    for string in value:
        if '=' not in string:
            msg = (
                f"EXTRA_CONTEXT should contain items of the form key=value; "
                f"'{string}' doesn't match that form"
            )
            raise click.BadParameter(msg)

    # Convert tuple -- e.g.: ('program_name=foobar', 'startsecs=66')
    # to dict -- e.g.: {'program_name': 'foobar', 'startsecs': '66'}
    return OrderedDict(s.split('=', 1) for s in value) or None

@click.command(context_settings={"help_option_names": ['-h', '--help']})
@click.version_option(__version__, '-V', '--version', message=version_msg())
@click.argument('template', required=False)
@click.argument('extra_context', nargs=-1, callback=validate_extra_context)
@click.option(
    '--no-input',
    is_flag=True,
    help='Do not prompt for parameters and only use cookiecutter.json file content. '
    'Defaults to deleting any cached resources and redownloading them. '
    'Cannot be combined with the --replay flag.',
)
@click.option(
    '-c',
    '--checkout',
    help='branch, tag or commit to checkout after git clone',
)
@click.option(
    '--directory',
    help='Directory within repo that holds cookiecutter.json file '
    'for advanced repositories with multi templates in it',
)
@click.option(
    '-v', '--verbose', is_flag=True, help='Print debug information', default=False
)
@click.option(
    '--replay',
    is_flag=True,
    help='Do not prompt for parameters and only use information entered previously. '
    'Cannot be combined with the --no-input flag or with extra configuration passed.',
)
@click.option(
    '--replay-file',
    type=click.Path(),
    default=None,
    help='Use this file for replay instead of the default.',
)
@click.option(
    '-f',
    '--overwrite-if-exists',
    is_flag=True,
    help='Overwrite the contents of the output directory if it already exists',
)
@click.option(
    '-s',
    '--skip-if-file-exists',
    is_flag=True,
    help='Skip the files in the corresponding directories if they already exist',
    default=False,
)
@click.option(
    '-o',
    '--output-dir',
    default='.',
    type=click.Path(),
    help='Where to output the generated project dir into',
)
@click.option(
    '--config-file', type=click.Path(), default=None, help='User configuration file'
)
@click.option(
    '--default-config',
    is_flag=True,
    help='Do not load a config file. Use the defaults instead',
)
@click.option(
    '--debug-file',
    type=click.Path(),
    default=None,
    help='File to be used as a stream for DEBUG logging',
)
@click.option(
    '--accept-hooks',
    type=click.Choice(['yes', 'ask', 'no']),
    default='yes',
    help='Accept pre/post hooks',
)
@click.option(
    '-l', '--list-installed', is_flag=True, help='List currently installed templates.'
)
@click.option(
    '--keep-project-on-failure',
    is_flag=True,
    help='Do not delete project folder on failure',
)
def main(
    template: str,
    extra_context: dict[str, Any],
    no_input: bool,
    checkout: str,
    verbose: bool,
    replay: bool | str,
    overwrite_if_exists: bool,
    output_dir: str,
    config_file: str | None,
    default_config: bool,
    debug_file: str | None,
    directory: str,
    skip_if_file_exists: bool,
    accept_hooks: Literal['yes', 'ask', 'no'],
    replay_file: str | None,
    list_installed: bool,
    keep_project_on_failure: bool,
) -> None:
    """Create a project from a Cookiecutter project template (TEMPLATE).

    Cookiecutter is free and open source software, developed and managed by
    volunteers. If you would like to help out or fund the project, please get
    in touch at https://github.com/cookiecutter/cookiecutter.
    """
    with open(f"{template}/cookiecutter.json") as cookiecutter_file:
        parsed_json = json.load(cookiecutter_file)

    # pprint(parsed_json)

    questions = []
    for key, value in parsed_json.items():
        if type(value) == str:
            if value.lower() in ["true", "yes", "y", "on", "false", "no", "n"]:
                questions.append(
                    inquirer.Confirm(key, message=key, default=(value.lower() == "y")),
                )
            else:
                questions.append(
                    inquirer.Text(key, key, default=value)
                )
        elif type(value) == list:
            questions.append(
                inquirer.List(key,
                              message=key,
                              choices=value,
                              ),
            )


    answer = inquirer.prompt(questions)
    pprint(answer)

    correct_answer = {}
    for key, value in answer.items():
        if value =="True":
            correct_answer[key] = 'y'
        elif value == "False":
            correct_answer[key] = 'n'
        else:
            correct_answer[key] = value

    pprint(correct_answer)

    extra_context = [f"{k}={v}" for k, v in correct_answer.items()]

    import subprocess
    print(["cookiecutter", template, *extra_context])
    print(subprocess.run(["cookiecutter", template, *extra_context]))

    # from cookiecutter.cli import main as cookiecutter_main
    # cookiecutter_main(
    #     template=template,
    #     extra_context=correct_answer,
    #     no_input=no_input,
    #     checkout=checkout,
    #     verbose=verbose,
    #     replay=replay,
    #     overwrite_if_exists=overwrite_if_exists,
    #     output_dir=output_dir,
    #     config_file=config_file,
    #     default_config=default_config,
    #     debug_file=debug_file,
    #     directory=directory,
    #     skip_if_file_exists=skip_if_file_exists,
    #     accept_hooks=accept_hooks,
    #     replay_file=replay_file,
    #     list_installed=list_installed,
    #     keep_project_on_failure=keep_project_on_failure,
    # )

if __name__ == "__main__":
    main()
