from dataclasses import dataclass, field
from typing import Optional

import pygame

from .color import Color


@dataclass
class TextStyle:
    """A class with the style data for text."""
    font_file: str = pygame.font.get_default_font()
    size: int = 30
    antialias: bool = True
    color: tuple[int, int, int] = Color.BLACK

    @property
    def font(self):
        return pygame.font.Font(self.font_file, self.size)


@dataclass
class Text:
    """
    A class for handling text in pygame.
    """

    string: str = ""
    x: int = 0
    y: int = 0
    style: TextStyle = field(default_factory=TextStyle)
    newline_width: Optional[int] = None

    def __post_init__(self):
        self.set(self.string)

    def set(self, string: str):
        """Sets the text value."""
        self.raw_string = string
        self.lines = string.split("\n")
        self.string = string.replace("\n", "")
        if self.newline_width is not None:
            new_lines = []
            for line in self.lines:
                new_line = ""
                for char in line:
                    new_line = new_line + char
                    if (
                        self.get_pygame_text_size(new_line, self.style)[0]
                        >= self.newline_width
                    ):
                        new_lines.append(new_line.strip())
                        new_line = ""
                if new_line:
                    new_lines.append(new_line.strip())
            self.lines = new_lines
        self._load_surface()

    def add(self, string: str):
        """Adds a string to the current text value."""
        self.set(self.raw_string + string)

    def pop(self) -> str:
        """Removes the last character of the current text value."""
        char = self.string[len(self.string) - 1]
        self.set(self.string[: len(self.string) - 1])
        return char

    def get_width(self) -> int:
        """Returns the width of the text surface."""
        return self.surface.get_width()

    def get_height(self) -> int:
        """Returns the height of the text surface."""
        return self.surface.get_height()

    def get_size(self) -> tuple[int, int]:
        """Returns the width and height of the text surface."""
        return self.get_width(), self.get_height()

    def get_rect(self) -> pygame.Rect:
        """Returns a rect the text."""
        return pygame.Rect(self.x, self.y, self.get_width(), self.get_height())

    def _load_surface(self):
        if len(self.lines) > 1:
            renders: list[pygame.Surface] = []
            for string in self.lines:
                renders.append(
                    self.style.font.render(
                        string, self.style.antialias, self.style.color
                    )
                )

            height = 0
            width = 0
            for line_surf in renders:
                height += line_surf.get_height()
                if line_surf.get_width() > width:
                    width = line_surf.get_width()

            self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
            x = y = 0
            for line_surf in renders:
                self.surface.blit(line_surf, (x, y))
                y += line_surf.get_height()

        else:
            self.surface = self.style.font.render(
                self.string, self.style.antialias, self.style.color
            )

    def render(self, surface: pygame.Surface):
        """Renders the text onto the surface."""
        surface.blit(self.surface, (self.x, self.y))

    def center_y(self, rect: pygame.Rect):
        """Centers the y value of the text inside a rect."""
        self.y = (rect.y + rect.height // 2) - self.get_height() // 2

    def center_x(self, rect: pygame.Rect):
        """Centers the x value of the text inside a rect."""
        self.x = (rect.x + rect.width // 2) - self.get_width() // 2

    def center(self, rect: pygame.Rect):
        """Centers the text inside a rect."""
        self.center_x(rect)
        self.center_y(rect)

    def center_relative(self, rect: pygame.Rect):
        """Centers the text inside a rect relative to the texts coordinates."""
        x, y = self.x, self.y
        self.center(rect)
        self.x += x
        self.y += y

    @classmethod
    def calc_text_size(
        cls, string: str, style: TextStyle = TextStyle()
    ) -> tuple[int, int]:
        """Gives the size of text surface without having to create a Text object."""
        font = pygame.font.Font(style.font_file, style.size)
        surface = font.render(string, style.antialias, style.color)
        return surface.get_size()
