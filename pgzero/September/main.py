# gives you access to extra functions that do not come with Python
import pgzrun
import time
from random import randint # only
from pgzhelper import Actor

WIDTH = 800
HEIGHT = 500
TITLE = "Neal and Xi Xi"
# set a variable equal to a rbg value for colors
MIDNIGHT_BLUE = (8, 36, 78)

# create our actors
player = Actor("knight_idle")
player.bottom = HEIGHT
player.gravity = 0
player.health = 20
player.score = 0
player.game_over = False
player.hit_top = False
player.start_time = time.time()
player.score = 0

bat = Actor("bat")
bat.x = WIDTH + 50  # somewhere towards the right edge
bat.y = randint(50, HEIGHT - 250)
bat.speed = 3
bat.base_speed = bat.speed
bat.animation_timer = 20
bat.damage = 5

# rectangles (x pos, y pos, width, height)
hacky_neal_rect = Rect(20, 20, 200, 100)
retry_button = None


# built in function that draws stuff on the screen
def draw():
    global retry_button
    # check if player's health is greater than 0
    if player.health > 0:
        # fills the screen with a color of your choosing
        screen.fill(MIDNIGHT_BLUE)
        screen.draw.text(f"Health: {player.health}", (20, 20), fontsize=35)
        screen.draw.text(f"Score: {player.score}", (600, 20), fontsize=35)
        retry_button = None
        player.draw()
        bat.draw()
    else:
        screen.draw.filled_rect(hacky_neal_rect, color=MIDNIGHT_BLUE)
        screen.draw.text(f"Health: {player.health}", (20, 20), fontsize=35)
        screen.draw.text("Game over", (300, 200), fontsize=50, color="red")
        # make the button rectangle
        retry_button = Rect(300, 300, 200, 50)
        screen.draw.filled_rect(retry_button, color="navy")
        screen.draw.text("Retry", (350, 310), fontsize=50)


def on_mouse_down(pos):
    if retry_button is not None and retry_button.collidepoint(pos):
        player.health = 20
        bat.x = 900
        player.bottom = HEIGHT
        player.start_time = time.time()


# called when any key on your keyboard is pressed
def on_key_down():
    # built in object from pgzero that represetns all the keys on the keyboard
    if keyboard.space and not player.hit_top:
        player.gravity = -20


# runs 60 times every second
def update():
    # counts times and increases score
    player.score = int(time.time() - player.start_time)
    
    # ENEMY STUFF
    # moves the enemy to the left each frame
    bat.x -= bat.speed
    
    # checks if enemy is at the left edge of the screen
    if bat.right <= 0:
        # sets the enemy back to the right side of the screen
        bat.left = WIDTH
        # resets the speed back to the normal speed
        bat.speed = bat.base_speed
# _________________________________________________________________________#
    # PLAYER STUFF    
    # increase gravity each frame
    player.gravity += 1
    #  add gravity to the player's y value
    player.y += player.gravity

    # check if the player is on the floor
    if player.bottom >= HEIGHT:
        # the bottom of the player set equal to the bottom of the screen
        player.bottom = HEIGHT
        player.hit_top = False

    # check if the player hits the top of the screen
    if player.top <= 0:
        player.hit_top = True
        player.gravity += 20
        bat.speed *= 1.5
# _________________________________________________________________________#
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

    # check for collision
    if player.colliderect(bat):
        bat.left = WIDTH
        bat.speed = bat.base_speed
        # take away life
        player.health -= bat.damage
        player.scale = 2

    # keeps the larger of 0 and player's health
    player.health = max(0, player.health)


# runs the game
pgzrun.go()
