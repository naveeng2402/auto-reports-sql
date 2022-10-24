import json
import jsonschema
from typing import Iterable

import utils


def validate_json(filename: str) -> tuple[bool, str | Iterable]:
    schema = json.loads(utils.get_schema())

    with open(filename) as f:
        try:
            res = json.load(f)
        except:
            return False, "ERR: Invalid JSON string"

        try:
            jsonschema.validate(instance=res, schema=schema)
        except:
            return (
                False,
                f"ERR: The JSON should conform to the following schema:\n{schema}",
            )

    return True, tuple(res)
