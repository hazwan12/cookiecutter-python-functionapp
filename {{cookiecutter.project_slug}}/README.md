# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Structure

- `{{ cookiecutter.package_name }}/` — function app source
- `tests/` — unit tests (pytest)
- `azure-pipelines.yml` — Build, SCA (pip-audit), SAST (bandit), Test stages

## Local development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
cp local.settings.json.example local.settings.json
```

## Run tests

```bash
pytest --cov={{ cookiecutter.package_name }}
```
