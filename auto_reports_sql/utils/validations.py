import pkgutil
import os
import pkg_resources
import json
import jsonschema
import click
from typing import Iterable

from ..constants import parameter_choices


def check_installed_package(package: str):
    try:
        pkg_resources.get_distribution(package)
        return True
    except:
        return False


def validate_packages():
    db = os.getenv("db")
    click.echo(db)
    if db == "mysql":
        if not check_installed_package("mysql-connector-python"):
            raise click.ClickException(
                "'mysql-connector-python' is not installed.\npip install mysql-connector-python"
            )
    if db == "postgres":
        if not check_installed_package("psycopg2-binary"):
            raise click.ClickException(
                "'psycopg2-binary' is not installed.\npip install psycopg2-binary"
            )


def validate_prams(**kwargs):
    if kwargs.get("db", "") == "sqlite":
        if not kwargs.get("db_path"):
            raise click.ClickException(
                "--db-path is required when --db is set to 'sqlite'"
            )
    else:
        if not (
            kwargs.get("host")
            and kwargs.get("username")
            and kwargs.get("password")
            and kwargs.get("db_name")
        ):
            raise click.ClickException(
                "--host --username --password --db-name are required when --db is set to 'mysql' or 'postgres'"
            )


def get_schema(type: parameter_choices.JSON_SCHEMA) -> str:
    return pkgutil.get_data(__name__, f"../schema/{type}.schema.json").decode()


def validate_schema(
    filename: str, type: parameter_choices.JSON_SCHEMA
) -> tuple[bool, str | Iterable]:
    schema_str = get_schema(type)
    schema = json.loads(schema_str)

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
                f"ERR: The JSON should conform to the following schema:\n{schema_str}",
            )

    return True, tuple(res)
