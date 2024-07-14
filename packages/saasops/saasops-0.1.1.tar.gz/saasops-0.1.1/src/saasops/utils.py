from saasops.classes import MessageStyle
from rich.console import Console

# Utility functions


def print_status(console: Console, message: str, style: MessageStyle) -> None:
    """Print a status message with the specified style."""
    console.print(message, markup=True, style=style.value)
