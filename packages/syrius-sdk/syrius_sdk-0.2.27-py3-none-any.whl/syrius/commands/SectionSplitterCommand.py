from typing import Any

from syrius.commands.abstract import Command, AbstractCommand


class SectionSplitterCommand(Command):
    """ """
    id: int = 20
    words: list[dict[str, Any]] | AbstractCommand
    text: str | AbstractCommand
