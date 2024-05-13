import time
from pathlib import Path

MESSAGE_FILE = Path(__file__).parent / "messages/messages.txt"


def pop_message_from_file() -> str | None:
    first_message = None

    with open(MESSAGE_FILE, "r") as f:
        messages = f.readlines()
        if messages:
            first_message = messages.pop(0).strip()

    with open(MESSAGE_FILE, "w") as f:
        f.writelines(messages)

    return first_message


def main() -> None:
    while True:
        message = pop_message_from_file()
        if message:
            print("from file:", message)

        else:
            print("random preset message")

        time.sleep(2)


if __name__ == "__main__":
    main()
