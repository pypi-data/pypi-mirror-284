from syrius.commands.abstract import Command, AbstractCommand


class AWSS3SaveObjectCommand(Command):
    """ """
    id: int = 39
    region: str | AbstractCommand
    access_key: str | AbstractCommand
    secret_key: str | AbstractCommand
    bucket: str | AbstractCommand
    filename: str | AbstractCommand
    file_content: str | AbstractCommand
