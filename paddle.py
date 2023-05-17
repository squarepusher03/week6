from drawable import Drawable
from colors import Colors
from game_information import WindowInfo as wi
import pygame as pg


class Paddle(Drawable):
    def __init__(self, width: int, height: int, color: tuple = Colors.PADDLE1_BLUE,
                 x: int = wi.SCREEN_WIDTH / 2, y: int = wi.SCREEN_HEIGHT / 2):
        super().__init__(x, y)
        self.__color = color
        self.__width = width
        self.__height = height

    def draw(self, surface: pg.Surface):
        pg.draw.rect(surface, self.__color, self.get_rect())

    def move(self):
        pass

    def get_rect(self):
        if self.getLoc()[1] >= wi.SCREEN_HEIGHT / 2:
            rect = pg.Rect(pg.mouse.get_pos()[0] - self.__width / 2,
                           wi.SCREEN_HEIGHT - 20 - self.__height,
                           self.__width, self.__height)
        else:
            rect = pg.Rect(pg.mouse.get_pos()[0] - self.__width / 2, 20,
                           self.__width, self.__height)

        return rect
