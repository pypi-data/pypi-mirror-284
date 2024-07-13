from dataclasses import dataclass, field
from typing import Any


@dataclass
class PythonSchema:
    name: str
    containerEnv: dict[str, str] = field(
        init=False,
        default_factory=lambda: {
            "POETRY_VIRTUALENVS_IN_PROJECT": "true",
        },
    )
    customizations: dict[str, Any] = field(
        init=False,
        default_factory=lambda: {
            "vscode": {
                "extensions": [
                    "ms-python.python",
                    "charliermarsh.ruff",
                    "christian-kohler.path-intellisense",
                    "tamasfe.even-better-toml",
                    "redhat.vscode-yaml",
                ]
            }
        },
    )
    image: str = field(
        init=False,
        default="mcr.microsoft.com/devcontainers/python:3.10",
    )
    runArgs: list[str] = field(
        init=False,
        default_factory=list,
    )
    onCreateCommand: str = field(
        init=False,
        default="curl -sSL https://install.python-poetry.org | python3 -",
    )
    postCreateCommand: str = field(
        init=False,
        default="poetry install",
    )

    def __post_init__(self):
        self.name = self.name.strip()
        self.runArgs.append(
            f'--name={self.name.lower().replace(" ", "-")}-devcontainer'
        )


@dataclass
class JavascriptSchema:
    name: str
    customizations: dict[str, Any] = field(
        init=False,
        default_factory=lambda: {
            "vscode": {
                "extensions": [
                    "christian-kohler.path-intellisense",
                    "VisualStudioExptTeam.vscodeintellicode",
                ]
            }
        },
    )
    image: str = field(
        init=False,
        default="mcr.microsoft.com/devcontainers/javascript-node:20",
    )
    runArgs: list[str] = field(
        init=False,
        default_factory=list,
    )

    def __post_init__(self):
        self.name = self.name.strip()
        self.runArgs.append(
            f'--name={self.name.lower().replace(" ", "-")}-devcontainer'
        )
