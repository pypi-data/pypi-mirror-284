import json
from dataclasses import asdict
from pathlib import Path
from typing import Any

from source.entities import devcontainer_json, enums, settings_json

CURRENT_PATH = Path()
DEVCONTAINER_DIR_PATH = CURRENT_PATH / ".devcontainer"
DEVCONTAINER_JSON_PATH = DEVCONTAINER_DIR_PATH / "devcontainer.json"
VSCODE_DIR_PATH = CURRENT_PATH / ".vscode"
VSCODE_SETTINGS_JSON_PATH = VSCODE_DIR_PATH / "settings.json"


def check_json_files_existence():
    assert (
        not DEVCONTAINER_JSON_PATH.exists()
    ), f"{DEVCONTAINER_JSON_PATH} already exists!"
    check_vscode_settings_json_existance()


def check_vscode_settings_json_existance():
    assert (
        not VSCODE_SETTINGS_JSON_PATH.exists()
    ), f"{VSCODE_SETTINGS_JSON_PATH} already exists!"


def init(
    language: str,
):
    settings_json_schema = get_settings_json_schema(language)
    VSCODE_DIR_PATH.mkdir(
        exist_ok=True,
    )
    VSCODE_SETTINGS_JSON_PATH.write_text(
        data=json.dumps(
            obj=settings_json_schema,
            indent=4,
        )
    )

    if devcontainer_json_schema := get_devcontainer_json_schema(
        language,
        name=CURRENT_PATH.absolute().name,
    ):
        DEVCONTAINER_DIR_PATH.mkdir(
            exist_ok=True,
        )
        DEVCONTAINER_JSON_PATH.write_text(
            data=json.dumps(
                obj=asdict(devcontainer_json_schema),
                indent=4,
            )
        )


def get_settings_json_schema(
    language: str,
):
    match language:
        case enums.Language.PYTHON:
            settings_json_schema = settings_json.PYTHON_SCHEMA
        case enums.Language.DART:
            settings_json_schema = settings_json.DART_SCHEMA
        case _:
            settings_json_schema = {}
    return settings_json_schema


def get_devcontainer_json_schema(
    language: str,
    name: str,
):
    match language:
        case enums.Language.PYTHON:
            devcontainer_json_schema = devcontainer_json.PythonSchema(name)
        case enums.Language.JAVASCRIPT:
            devcontainer_json_schema = devcontainer_json.JavascriptSchema(name)
        case _:
            devcontainer_json_schema = None
    return devcontainer_json_schema


def update_settings_json():
    settings_json_schema: dict[str, Any] = json.loads(
        VSCODE_SETTINGS_JSON_PATH.read_text()
    )
    language = next(
        k.replace("[", "").replace("]", "")
        for k in settings_json_schema.keys()
        if k.startswith("[")
    )
    settings_json_schema = get_settings_json_schema(language)
    VSCODE_SETTINGS_JSON_PATH.write_text(
        data=json.dumps(
            obj=settings_json_schema,
            indent=4,
        )
    )
