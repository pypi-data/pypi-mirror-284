from syrius.commands.abstract import Command, AbstractCommand


class OpenAITextToSpeechCommand(Command):
    """ """
    id: int = 37
    api_key: str | AbstractCommand
    model: str | AbstractCommand
    speed: str | AbstractCommand
    message: str | AbstractCommand
    voice: str | AbstractCommand
    output_format: str | AbstractCommand
