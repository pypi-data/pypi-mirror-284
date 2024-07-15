from syrius.commands.abstract import Command, AbstractCommand


class JoinAudioCommand(Command):
    """ """
    id: int = 38
    audio: list[str] | AbstractCommand
    format: str
