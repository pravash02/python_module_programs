# my_list = ["foo", "bar"]
# from rich import inspect
# inspect(my_list, methods=True)
#
from rich.console import Console
from rich.table import Table

table = Table(title="Star Wars Movies")

table.add_column("Released", justify="right", style="cyan", no_wrap=True)
table.add_column("Title", style="magenta")
table.add_column("Box Office", justify="right", style="green")

table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

console = Console()
console.print(table)

# from time import sleep
# from rich.console import Console
#
# console = Console()
# tasks = [f"task {n}" for n in range(1, 11)]
#
# with console.status("Working on tasks...") as status:
#     while tasks:
#         task = tasks.pop(0)
#         sleep(1)
#         console.log(f"{task} complete")


from rich.console import Console
from rich.traceback import install
install(show_locals=True)

console = Console()

try:
    # do_something()
    pass
except Exception:
    console.print_exception(show_locals=True)
