from abc import ABC, abstractmethod
from pygame import Surface


class Drawable(ABC):
    def __init__(self, x=0, y=0):
        self.__visible = True
        self.__x = x
        self.__y = y

    def isVisible(self) -> bool:
        return self.__visible

    def setVisible(self, visibility: bool):
        self.__visible = visibility

    def get_rect(self):
        pass

    def getLoc(self) -> tuple:
        return self.__x, self.__y

    def setX(self, x: int):
        self.__x = x

    def setY(self, y: int):
        self.__y = y

    # ONLY FOR CHILDREN CLASSES
    def intersects(self, other) -> bool:
        rect1 = self.get_rect()
        rect2 = other.get_rect()
        # self's left side overlaps other
        # self's right side overlaps other
        # self's top side overlaps other
        # self's bottom overlaps other
        # return (rect1.x < rect2.x + rect2.width) and \
        #     (rect1.x + rect1.width > rect2.x) and \
        #     (rect1.y < rect2.y + rect2.height) and \
        #     (rect1.height + rect1.y > rect2.y)
        return rect1

    @abstractmethod
    def draw(self, surface: Surface):
        pass
