import click
import click_config_file


@click.group()
def main():
    pass


@main.command()
def execute():
    click.secho("Executing queries", bg="red")


@main.command()
def generate():
    click.secho("Generating queries", bg="green")
