import typer
import shutil

app = typer.Typer()
files_app = typer.Typer(name="files", help="Manage files")

# Add the 'files' sub-app to the main app
app.add_typer(files_app, name="files", help="File management commands")


# Define a sub-command 'move' under 'files' sub-app
def move_files(src_path: str, dest_path: str):
    """
    Move files from source path to destination path.
    """
    # shutil.move(src_path, dest_path)
    typer.echo(f"Moved files from '{src_path}' to '{dest_path}'")

# Add the 'move' sub-command to 'files' sub-app
files_app.command(name="move", help="Move files")(move_files)


# Define a sub-command 'delete' under 'files' sub-app
def delete_files(file_path: str):
    """
    Delete files at the specified path.
    """
    # shutil.rmtree(file_path)
    typer.echo(f"Deleted files at '{file_path}'")

# Add the 'delete' sub-command to 'files' sub-app
files_app.command(name="delete", help="Delete files")(delete_files)


@app.command()
def main_app():
    print("This is main app")


if __name__ == "__main__":
    app()
