import os


def get_schema() -> str:
    with open(os.path.join(os.getenv("TEMPLATES_PATH"), "schema.json")) as f:
        res = f.read()
    return res
