import pygame as pg
from ball import Ball
from paddle import Paddle
from text import Text
from colors import Colors
from game_information import WindowInfo as wi

drawn_items = list()
pg.init()

window_surface = pg.display.set_mode((wi.SCREEN_WIDTH, wi.SCREEN_HEIGHT))
drawn_items.append(window_surface)

myBall = Ball(400, 300, 15, Colors.PADDLE1_BLUE)
myBall.draw(window_surface)
drawn_items.append(myBall)

paddle1 = Paddle(150, 20)
drawn_items.append(paddle1)

paddle2 = Paddle(150, 20, Colors.PADDLE2_ORANGE, wi.SCREEN_WIDTH / 2, 30)
drawn_items.append(paddle2)

scoreboard = Text("Score: 0", 10, 10)
drawn_items.append(scoreboard)

score = 0

def drawDrawables(items: list, score: int):
    for item in items:
        if item is window_surface:
            item.fill(Colors.WHITE)
        elif isinstance(item, Ball):
            item.draw(window_surface)

            if item.intersects(paddle1):
                score += 1
                item.setYSpeed(item.getYSpeed() * -1)
                scoreboard.setMessage(f"Score: {score}")

            item.move()
        elif isinstance(item, Paddle):
            item.draw(window_surface)
        elif item is scoreboard:
            scoreboard.draw(window_surface)


def gameLoop():
    running = True

    while running:
        drawDrawables(drawn_items, score)

        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                myBall.setVisible(not myBall.isVisible())  # not how I would've done this but ok

        fpsClock.tick(30)


if __name__ == "__main__":
    fpsClock = pg.time.Clock()

    gameLoop()

    exit()
