import pygame as pg

# general ball info
class BallInfo:
    X_SPEED = 8
    Y_SPEED = 8

class TextInfo:
    DEFAULT_FONT = "freesansbold.ttf"

class PaddleInfo:
    pass

class WindowInfo:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

class Surfaces:
    WINDOW_SURFACE = pg.display.get_surface()
