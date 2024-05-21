from random import choice

default_messages: list[str] = [
    "help me",
    "right here",
    "so cold",
    "it stinks",
    "he is here",
]


def get_message() -> str:
    return choice(default_messages)
