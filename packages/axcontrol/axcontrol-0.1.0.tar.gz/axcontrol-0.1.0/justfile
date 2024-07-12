# use PowerShell instead of sh:
set windows-shell := ["powershell.exe", "-c"]

update-deps:
    uv pip compile pyproject.toml -o requirements/requirements.pip
    uv pip compile pyproject.toml --extra=dev -o requirements/dev-requirements.pip

deps:
    just update-deps
    uv pip sync requirements/dev-requirements.pip
