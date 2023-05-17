from drawable import Drawable
from game_information import BallInfo as bi
import pygame as pg


class Ball(Drawable):
    __instances = list()

    def __init__(self, x: int = 0, y: int = 0, radius: float = 10, color: tuple = (0, 0, 0)):
        super().__init__(x, y)
        self.__radius = radius
        self.__color = color
        self.__xSpeed = bi.X_SPEED
        self.__ySpeed = bi.Y_SPEED
        Ball.__instances.append(self)

    def draw(self, surface: pg.Surface):
        if super().isVisible():
            pg.draw.circle(surface, self.__color, self.getLoc(), self.__radius)

    def getRadius(self):
        return self.__radius

    def getColor(self):
        return self.__color

    def getXSpeed(self):
        return self.__xSpeed

    def getYSpeed(self):
        return self.__ySpeed

    def get_rect(self):
        return pg.Rect(self.getLoc()[0] - self.__radius, self.getLoc()[1] - self.__radius,
                       2 * self.__radius, 2 * self.__radius)

    def setRadius(self, radius: float):
        self.__radius = radius

    def setColor(self, color: tuple):
        self.__color = color

    def setXSpeed(self, speed: int):
        self.__xSpeed = speed

    def setYSpeed(self, speed: int):
        self.__ySpeed = speed

    def move(self):
        currentX, currentY = self.getLoc()
        newX = currentX + self.__xSpeed
        newY = currentY + self.__ySpeed
        self.setX(newX)
        self.setY(newY)

        surface = pg.display.get_surface()
        width, height = surface.get_size()

        # if radius distance away from left or right border
        if newX <= self.__radius or newX + self.__radius >= width:
            self.__xSpeed *= -1

        if newY + 2 * self.__radius <= 0 or newY >= height:
            self.__ySpeed = 0
            super().setVisible(False)
