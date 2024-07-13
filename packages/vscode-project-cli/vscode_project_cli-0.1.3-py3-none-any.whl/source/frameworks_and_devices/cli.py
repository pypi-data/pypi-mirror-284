import typer
from rich import print
from rich.prompt import Prompt

from source.entities import enums
from source.interface_adapters import controller

cli = typer.Typer()


@cli.command()
def init():
    try:
        controller.check_json_files_existence()
    except AssertionError as exc:
        print(exc)
        raise typer.Abort()

    controller.init(
        language=Prompt.ask(
            prompt="Language",
            choices=list(enums.Language),
        ),
    )


@cli.command()
def update_settings_json():
    try:
        controller.check_vscode_settings_json_existance()
        print(".vscode/settings.json doesn't exist!")
        raise typer.Abort()
    except AssertionError:
        controller.update_settings_json()
