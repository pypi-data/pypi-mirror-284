from syrius.commands.abstract import Command, AbstractCommand


class AzureTextToSpeechCommand(Command):
    """ """
    id: int = 43
    region: str | AbstractCommand
    api_key: str | AbstractCommand
    language_code: str | AbstractCommand
    output_format: str | AbstractCommand
    voice_name: str | AbstractCommand
    text: str | AbstractCommand
