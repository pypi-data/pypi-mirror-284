PYTHON_SCHEMA = {
    "[python]": {
        "editor.defaultFormatter": "charliermarsh.ruff",
        "editor.codeActionsOnSave": {
            "source.fixAll.ruff": "always",
            "source.organizeImports.ruff": "always",
            "source.unusedImports": "always",
        },
    },
    "python.analysis.typeCheckingMode": "standard",
    "python.analysis.autoImportCompletions": True,
}

DART_SCHEMA = {
    "[dart]": {
        "editor.rulers": [80],
        "editor.selectionHighlight": True,
        "editor.suggestSelection": "first",
        "editor.tabCompletion": "onlySnippets",
        "editor.wordBasedSuggestions": "off",
    }
}
