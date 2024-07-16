from syrius.commands.abstract import Command, AbstractCommand


class TokenCounterCommand(Command):
    """ """
    id: int = 10
    text: str | AbstractCommand
