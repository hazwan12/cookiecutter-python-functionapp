import os

if "{{ cookiecutter.open_source_license }}" == "Proprietary":
    os.remove("LICENSE") if os.path.exists("LICENSE") else None
