from string import ascii_uppercase

from colors import ColorType, blink_to_message, color_wave
from coords import CoordsType, load_coords
from letter_to_light_map import lights_index
from matplotlib import animation
from matplotlib import pyplot as plt
from matplotlib.collections import PathCollection


def norm_color(color: ColorType) -> ColorType:
    """Return a value between 0 and 1 for color, as required by matplotlib."""
    return tuple(c / 255 for c in color)  # type: ignore


def update_plot(colors: list[ColorType], sc: PathCollection) -> tuple[PathCollection]:
    sc.set_facecolor([norm_color(c) for c in colors])  # type: ignore
    return (sc,)


def animate(coords: CoordsType, message: str):
    message = message.upper()
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_aspect("equal", "box")
    ax.set_axis_off()
    fig.set_facecolor("k")

    sc = ax.scatter(
        *coords,
        facecolor="0",  # black
        edgecolor="0.1",  # white
        s=100,
    )
    # letter labels
    for x, letter in enumerate(ascii_uppercase):
        ax.text(
            coords[0, lights_index[x]],
            coords[1, lights_index[x]] + 0.06,
            letter,
            ha="center",
            color="1",
        )

    anim = animation.FuncAnimation(  # noqa
        fig,
        update_plot,
        frames=blink_to_message(coords, message),  # type: ignore
        # frames=color_wave(coords),  # type: ignore
        fargs=(sc,),
        interval=500,
        cache_frame_data=False,
    )

    plt.show()


def main() -> None:
    # coords = load_coords("coords_line.csv")
    coords = load_coords("stranger_things_lights_coords.csv")

    animate(coords, message="hello world")


if __name__ == "__main__":
    main()
