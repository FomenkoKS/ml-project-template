import pathlib

req_path = pathlib.Path(__file__).parent.parent.resolve() / "requirements.txt"
venv_path = pathlib.Path(__file__).parent.resolve() / "venv.yaml"

with open(venv_path, "w") as venv_file:
    venv_file.write('python: "3.10"\n\nbuild_dependencies:\n\ndependencies:\n')
    with open(req_path, "r") as req_file:
        for line in req_file:
            if not line.startswith("#"):
                venv_file.write(f"  - {line}")
