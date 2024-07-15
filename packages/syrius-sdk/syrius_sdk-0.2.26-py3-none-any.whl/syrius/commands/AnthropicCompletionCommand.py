from typing import Any

from syrius.commands.abstract import Command, AbstractCommand


class AnthropicCompletionCommand(Command):
    """ """
    id: int = 36
    messages: list[dict[str, Any]] | AbstractCommand
    api_key: str | AbstractCommand
    model: str | AbstractCommand
    max_tokens: int | AbstractCommand
    temperature: float | AbstractCommand
    tools: dict[str, Any] | AbstractCommand
    extract: str | AbstractCommand
