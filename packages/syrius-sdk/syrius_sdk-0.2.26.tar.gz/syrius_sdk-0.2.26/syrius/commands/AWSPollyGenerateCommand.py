from syrius.commands.abstract import Command, AbstractCommand


class AWSPollyGenerateCommand(Command):
    """ """
    id: int = 41
    engine: str | AbstractCommand
    access_key: str | AbstractCommand
    secret_key: str | AbstractCommand
    language_code: str | AbstractCommand
    output_format: str | AbstractCommand
    voice_name: str | AbstractCommand
    text: str | AbstractCommand
