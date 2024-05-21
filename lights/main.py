import time
from pathlib import Path

import board
import neopixel
from colors import ColorType, blink_to_message, color_wave
from coords import CoordsType, load_coords
from default_messages import get_message

ROOT_PATH = Path(__file__).parent.resolve()
MESSAGE_FILE = ROOT_PATH / "messages/messages.txt"

N_PIXELS: int = 50
pixels = neopixel.NeoPixel(
    board.D21,  # type: ignore
    n=N_PIXELS,
    brightness=0.4,
    pixel_order=neopixel.RGB,
    auto_write=False,
)


def clear_pixels():
    pixels.fill((0, 0, 0))
    pixels.show()


def make_color_int(color: ColorType) -> ColorType:
    return tuple(int(c) for c in color)


def run_message(coords: CoordsType, message: str) -> None:
    color_gen = blink_to_message(coords, message)
    for colors in color_gen:
        for p, c in enumerate(colors):
            pixels[p] = make_color_int(c)

        pixels.show()
        time.sleep(0.5)


def run_color_wave(coords: CoordsType) -> None:
    color_gen = color_wave(coords)
    for colors in color_gen:
        for p, c in enumerate(colors):
            pixels[p] = make_color_int(c)

        pixels.show()
        time.sleep(1 / 60)


def pop_message_from_file() -> str | None:
    first_message = None

    try:
        with open(MESSAGE_FILE, "r") as f:
            messages = f.readlines()
            if messages:
                first_message = messages.pop(0).strip()

        with open(MESSAGE_FILE, "w") as f:
            f.writelines(messages)

    except FileNotFoundError:
        pass

    return first_message


def main() -> None:
    coords = load_coords(ROOT_PATH / "coords_line.csv")

    while True:
        message = pop_message_from_file()
        if message:
            print("from file:", message)
            run_message(coords, message)

        else:
            message = get_message()
            print(f"preset: {message}")
            run_message(coords, message)

        run_color_wave(coords)
        clear_pixels()

        time.sleep(2)


if __name__ == "__main__":
    main()
