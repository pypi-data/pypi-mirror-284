from syrius.commands.LoopInputCommand import loopType
from syrius.commands.abstract import Command, AbstractCommand


class GoogleTextToSpeechCommand(Command):
    """ """
    id: int = 42
    credentials: str | AbstractCommand | loopType
    speed_rate: float | int | AbstractCommand | loopType
    language_code: str | AbstractCommand | loopType
    output_format: str | AbstractCommand | loopType
    voice_name: str | AbstractCommand | loopType
    text: str | AbstractCommand | loopType
