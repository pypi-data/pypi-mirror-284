from syrius.commands.abstract import Command, AbstractCommand


class GoogleTextToSpeechCommand(Command):
    """ """
    id: int = 42
    credentials: str | AbstractCommand
    speed_rate: float | int | AbstractCommand
    language_code: str | AbstractCommand
    output_format: str | AbstractCommand
    voice_name: str | AbstractCommand
    text: str | AbstractCommand
