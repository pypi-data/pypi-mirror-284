from typing import Any

from syrius.commands.abstract import Command, AbstractCommand


class ArrayOfKeyValueToArrayCommand(Command):
    """ """
    id: int = 28
    array: list[Any] | AbstractCommand
    filtered_by: str | AbstractCommand
