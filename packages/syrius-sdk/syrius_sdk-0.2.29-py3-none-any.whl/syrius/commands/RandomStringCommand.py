from syrius.commands.abstract import Command, AbstractCommand


class RandomStringCommand(Command):
    """ """
    id: int = 45
    max_chars: int | AbstractCommand
