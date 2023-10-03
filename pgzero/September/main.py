# gives you access to extra functions that do not come with Python
import pgzrun

WIDTH = 800
HEIGHT = 500
TITLE = "AJNX"

# the Rect class creates a rectangle (x, y, width, height)
test_rect = Rect(200, 20, 20, 300)

# The Actor class draws a rectangle around an image 
alien = Actor("alien")
alien.x = 300
alien.y = 500
# space between each actor
zom = Actor("zombie", (WIDTH - 100, 200))

player = Actor("dino")
player.bottom = HEIGHT
player.direction = 1


# built in function that draws stuff on the screen
def draw():
    screen.clear()
    alien.draw()
    zom.draw()
    player.draw()


# runs 60 times every second
def update():
    # my actors new x value is now 2 more than its old x value
    player.x = player.x + 2 * player.direction
    player.y -= 2 * player.direction

    if player.x >= WIDTH or player.y <= 0:
        player.direction = -1


# runs the game
pgzrun.go()
