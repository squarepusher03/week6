from drawable import Drawable
from game_information import TextInfo as ti
import pygame as pg


class Text(Drawable):
    def __init__(self, message: str = "Pygame", x: int = 0, y: int = 0, color: tuple = (0, 0, 0), size: int = 24):
        super().__init__(x, y)
        self.__surface = None
        self.__message = message
        self.__color = color
        self.__fontObj = pg.font.Font(ti.DEFAULT_FONT, size)

    def draw(self, surface):
        self.__surface = self.__fontObj.render(self.__message, True, self.__color)

        surface.blit(self.__surface, self.getLoc())

    def get_rect(self):
        return self.__surface.get_rect()

    def setMessage(self, message: str):
        self.__message = message
