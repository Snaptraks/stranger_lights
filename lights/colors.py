import colorsys
import random
from string import ascii_uppercase
from typing import Iterator

import numpy as np
from coords import CoordsType
from letter_to_light_map import lights_index

ColorType = tuple[float, ...]


def colors_fade_rgb(
    color_0: ColorType, color_1: ColorType, steps: int = 50
) -> Iterator[ColorType]:
    slope = [(color_1[i] - color_0[i]) / steps for i in range(3)]

    new_color = color_0[:]
    for t in range(steps + 1):
        new_color = tuple(int(color_0[i] + t * slope[i]) for i in range(3))
        yield new_color


def random_rgb() -> ColorType:
    rgb = tuple(int(c * 255) for c in colorsys.hsv_to_rgb(random.random(), 1, 1))
    return rgb


def random_lights_color(n_lights: int) -> list[ColorType]:
    return [random_rgb() for _ in range(n_lights)]


def blink_to_message(coords: CoordsType, message: str) -> Iterator[list[ColorType]]:
    base_colors = random_lights_color(coords.shape[1])
    message = message.upper()
    all_off: list[ColorType] = [(0, 0, 0) for _ in range(len(base_colors))]
    for letter in message:
        led_colors = all_off.copy()
        if letter in ascii_uppercase:
            letter_index = lights_index[ascii_uppercase.index(letter)]
            led_colors[letter_index] = base_colors[letter_index]

        yield led_colors
        yield all_off

    yield all_off  # to finish the message with an all_off


def color_wave(coords: CoordsType) -> Iterator[list[ColorType]]:
    base_colors = random_lights_color(coords.shape[1])

    def func(x, y, t) -> ColorType:
        # return np.exp(-((x - t) ** 2))
        return 0.5 * (np.sin(4 * (x - t)) + 1)

    t = 0
    dt = 0.4

    while True:
        masks = func(coords[0], coords[1], t)
        yield [
            tuple(c * mask for c in color) for color, mask in zip(base_colors, masks)
        ]
        t += dt
