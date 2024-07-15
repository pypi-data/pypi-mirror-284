from syrius.commands.abstract import Command, AbstractCommand


class AWSSESSendEmailCommand(Command):
    """ """
    id: int = 40
    region: str | AbstractCommand
    access_key: str | AbstractCommand
    secret_key: str | AbstractCommand
    subject: str | AbstractCommand
    from_email: str | AbstractCommand
    recipient: str | AbstractCommand
    text_email: str | AbstractCommand
    html_email: str | AbstractCommand
