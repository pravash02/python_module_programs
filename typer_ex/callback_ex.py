import typer

# Define a Typer app
app = typer.Typer()


# Define a callback function to be executed before a command is invoked
@app.callback()
def before_command_callback():
    typer.echo("Before command")


# Define a Typer command
@app.command()
def greet(name: str):
    typer.echo(f"Hello, {name}!")


if __name__ == "__main__":
    app()  # Run the Typer app
