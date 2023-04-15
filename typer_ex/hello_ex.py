import typer

app = typer.Typer()


@app.command()
def hello_world():
    print("hello world")


@app.command()
def greet(name: str):
    typer.echo(f"Hello, {name}!")


@app.command()
def greet2(name: str = typer.Argument("world", help="The name to greet", show_default=True)):
    typer.echo(f"Hello, {name}!")


@app.command()
def backup(database: str, output_dir: str, force: bool = False):
    if force:
        typer.echo("Forced backup requested!")
    else:
        typer.echo("Regular backup requested.")
    typer.echo(f"Database: {database}")
    typer.echo(f"Output directory: {output_dir}")


if __name__ == "__main__":
    app()
