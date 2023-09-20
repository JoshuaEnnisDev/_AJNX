# gives you access to extra functions that do not come with Python
import pgzrun

WIDTH = 800
HEIGHT = 600
TITLE = "AJNX"

# the Rect class creates a rectangle (x, y, width, height)
test_rect = Rect(20, 20, 20, 300)


# built in function that draws stuff on the screen
def draw():
    screen.draw.filled_rect(test_rect, "indigo")


# runs the game
pgzrun.go()
