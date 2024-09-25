from random import choice

default_messages: list[str] = [
    # Stranget Things theme
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
    # Halloween theme
    "happy halloween",
    "joyeuse halloween",
    "boo",
]


def get_message() -> str:
    return choice(default_messages)
