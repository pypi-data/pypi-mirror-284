from typing import Any

from syrius.commands.abstract import Command, AbstractCommand


class ArraysGetKeyCommand(Command):
    """ """
    id: int = 44
    array: dict[str, Any] | AbstractCommand
    key: str | AbstractCommand
