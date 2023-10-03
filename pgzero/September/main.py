# gives you access to extra functions that do not come with Python
import pgzrun

WIDTH = 800
HEIGHT = 500
TITLE = "AJNX"

player = Actor("knight_idle")
player.bottom = HEIGHT

bat = Actor("bat")
bat.x = WIDTH - 50
bat.bottom = HEIGHT
bat.speed = 3
bat.animation_timer = 20


# built in function that draws stuff on the screen
def draw():
    screen.clear()
    player.draw()
    bat.draw()


# runs 60 times every second
def update():
    # moves the enemy to the left each frame
    bat.x -= bat.speed
    # checks if enemy is at the left edge of the screen
    if bat.right <= 0:
        bat.left = WIDTH

    # subtract from the timer
    bat.animation_timer -= 1
    if bat.animation_timer <= 0:
        # reset it back
        bat.animation_timer = 20
        # check current image

# runs the game
pgzrun.go()
