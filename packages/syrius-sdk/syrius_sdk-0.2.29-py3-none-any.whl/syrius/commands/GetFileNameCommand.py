from syrius.commands.abstract import Command, AbstractCommand


class GetFileNameCommand(Command):
    """ """
    id: int = 46
    filename: str | AbstractCommand
    extension: str | AbstractCommand
