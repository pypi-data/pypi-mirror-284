import typer

from source.interface_adapters import controller

cli = typer.Typer()


@cli.callback()
def callback(): ...


@cli.command()
def init():
    controller.init()
