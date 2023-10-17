# gives you access to extra functions that do not come with Python
import pgzrun

WIDTH = 800
HEIGHT = 500
TITLE = "AJNX"
# set a variable equal to a rbg value for colors
MIDNIGHT_BLUE = (8, 36, 78)

player = Actor("knight_idle")
player.bottom = HEIGHT
player.gravity = 0

bat = Actor("bat")
bat.x = WIDTH - 50
bat.bottom = HEIGHT
bat.speed = 3
bat.base_speed = bat.speed
bat.animation_timer = 20


# built in function that draws stuff on the screen
def draw():
    # fills the screen with a color of your choosing
    if player.colliderect(bat):
        player.draw()
        screen.fill("black")
    else:
        screen.fill(MIDNIGHT_BLUE)
        player.draw()
        bat.draw()


# called when any key on your keyboard is pressed
def on_key_down():
    # built in object from pgzero that represetns all the keys on the keyboard
    if keyboard.space:
        player.gravity = -20


# runs 60 times every second
def update():
    # moves the enemy to the left each frame
    bat.x -= bat.speed
    # checks if enemy is at the left edge of the screen
    if bat.right <= 0:
        bat.left = WIDTH
        bat.speed = bat.base_speed

    # increase gravity each frame
    player.gravity += 1
    #  add gravity to the player's y value
    player.y += player.gravity

    # check if the player is on the floor
    if player.bottom >= HEIGHT:
        # the bottom of the player set equal to the bottom of the screen
        player.bottom = HEIGHT

    # check if the player hits the top of the screen
    if player.top <= 0:
        player.gravity += 20
        bat.speed *= 2

    # subtract from the timer
    bat.animation_timer -= 1
    if bat.animation_timer <= 0:
        # reset it back
        bat.animation_timer = 20
        # check current image
        if bat.image == "bat":
            # switch it to the other image
            bat.image = "bat_fly"
        else:
            # switch it back
            bat.image = "bat"

# runs the game
pgzrun.go()
