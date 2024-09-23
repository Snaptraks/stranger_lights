from random import choice

default_messages: list[str] = [
    "he is coming",
    "he is here",
    "help me",
    "i am hungry",
    "i am not alone",
    "i am trapped",
    "i cant escape",
    "i have hope",
    "it is so lonely",
    "it stinks",
    "please come",
    "right here",
    "so cold",
    "so scared",
]


def get_message() -> str:
    return choice(default_messages)
