from enum import Enum, auto

import pygame


class RelativePosition(Enum):
    """An enum for positions on the screen."""
    TOP_LEFT = auto()
    TOP_RIGHT = auto()
    BOTTOM_LEFT = auto()
    BOTTOM_RIGHT = auto()
    CENTER = auto()
    TOP_CENTER = auto()
    BOTTOM_CENTER = auto()
    LEFT_CENTER = auto()
    RIGHT_CENTER = auto()


class PygameDisplayUninitialized(Exception):
    """The Pygame Display was not initialized using set_mode()."""


def position_relative_to(rect: pygame.Rect, pos: RelativePosition) -> pygame.Rect:
    """
    Returns a rect that has its original coordinates placed relative to a specific position on the screen.

    The Pygame display must be initialized before calling this function.
    """
    screen = pygame.display.get_surface()
    if screen is None:
        raise PygameDisplayUninitialized(
            "The root function cannot be called \
                                          unless the display is initialized"
        )
    screen_width, screen_height = screen.get_size()
    center_pos = int(screen_width / 2), int(screen_height / 2)

    x, y = 0, 0
    match pos:
        case RelativePosition.CENTER:
            x = center_pos[0] - int(rect.width / 2)
            y = center_pos[1] - int(rect.height / 2)
        case RelativePosition.LEFT_CENTER:
            x = 0
            y = center_pos[1] - int(rect.height / 2)
        case RelativePosition.RIGHT_CENTER:
            x = screen_width - rect.width
            y = center_pos[1] - int(rect.height / 2)
        case RelativePosition.TOP_CENTER:
            x = center_pos[0] - int(rect.width / 2)
            y = 0
        case RelativePosition.TOP_LEFT:
            x = 0
            y = 0
        case RelativePosition.TOP_RIGHT:
            x = screen_width - rect.width
            y = 0
        case RelativePosition.BOTTOM_CENTER:
            y = screen_height - rect.height
            x = center_pos[0] - int(rect.width / 2)
        case RelativePosition.BOTTOM_LEFT:
            x = 0
            y = screen_height - rect.height
        case RelativePosition.BOTTOM_RIGHT:
            y = screen_height - rect.height
            x = screen_width - rect.width
        case other:
            ValueError("Invalid RootPosition argument")
    return rect
