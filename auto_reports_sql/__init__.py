import os
import sys
import json
from concurrent.futures import ThreadPoolExecutor
import click
import click_config_file

from . import utils
from .constants import parameter_choices


@click.group()
def main():
    pass


@main.command()
@click.option(
    "-t",
    "--threads",
    "threads",
    type=int,
    default=10,
    show_default=True,
    help="No. of threads used for computation",
)
@click.option(
    "-rt",
    "--report-title",
    "report_title",
    type=str,
    default="Report Title",
    show_default=True,
    help="Title of the generated report.",
)
@click.option(
    "-d",
    "--db",
    "db",
    type=click.Choice(parameter_choices.DB_OPTIONS),
    required=True,
    prompt="Which database you are using",
    help="The database which is used.",
)
@click.option(
    "-dp",
    "--db-path",
    "db_path",
    type=click.Path(exists=True),
    help="Sqlite database path. Only required if the database is set to 'sqlite'",
)
@click.option(
    "-h",
    "--host",
    "host",
    type=str,
    help="host of the database. Only required if the database is not set to 'sqlite'",
)
@click.option(
    "-u",
    "--username",
    "username",
    type=str,
    help="username to access the database. Only required if the database is not set to 'sqlite'",
)
@click.option(
    "-p",
    "--password",
    "password",
    type=str,
    help="password of the database. Only required if the database is not set to 'sqlite'",
)
@click.option(
    "-n",
    "--db-name",
    "db_name",
    type=str,
    help="name of the database. Only required if the database is not set to 'sqlite'",
)
@click.argument("queries", type=click.Path(exists=True), required=True)
@click_config_file.configuration_option()
def execute(**kwargs):
    os.environ = {**os.environ, **kwargs}
    queries: tuple[dict[str, str]] = kwargs.get("queries")
    threads: int = kwargs.get("threads")

    utils.validate_prams(**kwargs)
    utils.validate_packages()

    is_valid, res = utils.validate_schema(queries, type="execute")
    if not is_valid:
        click.secho(res, fg="red")
        sys.exit(1)

    result = []
    click.secho(f"Using {threads} Threads...", fg="yellow")

    with ThreadPoolExecutor(max_workers=threads) as exe:
        result = exe.map(lambda kwargs: utils.execute_sql(**kwargs), res)

    # click.echo(json.dumps(tuple(result), indent=2))
    utils.generate_report(result)

    """For testing performance"""
    # for query in queries:
    #     res.append(utils.execute_sql(max_workers=MAX_WORKERS, **query))


@main.command()
def generate():
    click.secho("Generating queries", bg="green")
