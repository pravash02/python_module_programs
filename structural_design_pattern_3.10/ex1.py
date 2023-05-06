from dataclasses import dataclass
import shlex
from typing import List


def execute_command(command_arg) -> None:
    match command_arg:
        case "1":
            print("One")
        case "2":
            print("Two")
        case "3":
            print("Three")
        case _:
            print("Other")

def execute_command_v2(command_arg) -> None:
    match command_arg.split():
        case ["load", filename]:
            print(f"Loading file: {filename}.")
        case ["save", filename]:
            print(f"Saving to file: {filename}.")
        case ["quit" | "exit" | "bye", *other] if "--force" in other or "-f" in other:
            print("Forcefully quitting the program.")
        case ["quit" | "exit" | "bye", *other]:
            print("Quitting the program.")
        case _:
            print(f"Unknown command: {command_arg!r}.")

@dataclass
class CommandArg():
    command: str
    argument: list[str]


def execute_command_v3(command_arg):
    match command_arg:
        case CommandArg(command="load", argument=filename):
            print(f"Loading file: {filename}.")
        case CommandArg(command="save", argument=filename):
            print(f"Saving to file: {filename}.")
        case CommandArg(command="quit" | "exit" | "bye", argument=["--force" | "-f", *other]):
            print("Forcefully quitting the program.")
        case CommandArg(command="quit" | "exit" | "bye"):
            print("Quitting the program.")
        case _:
            print(f"Unknown command: {command_arg!r}.")


def main() -> None:
    while True:
        # command_arg = input()
        # execute_command_v2(command_arg)
        command, *arguments = shlex.split(input("$ "))
        command_arg = CommandArg(command, arguments)
        execute_command_v3(command_arg)



if __name__ == '__main__':
    main()
