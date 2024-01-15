# flake8: noqa

from pgzrun import go
from pgzhelper import Actor

# screen setup
WIDTH = 1500
HEIGHT = 750
TITLE = "Survivor Game"

# create the background actor and store in a variable
bg = Actor("dungeon1")

# create player Actor
player = Actor("woman")
player.pos = (300, 300)
player.scale = 4
player.speed = 5


# ~~~~~~~~~~~~~~~~~~~~~~~~~ Our Functions ~~~~~~~~~~~~~~~~~~~~~~~~~ #
def move_player():
    # move to the left
    if keyboard.a:
        player.x -= player.speed
    # move to the right
    elif keyboard.d:
        player.x += player.speed
    # move up
    elif keyboard.w:
        player.y -= player.speed
    # move down
    elif keyboard.s:
        player.y += player.speed


def bound_player():
    if player.left < 100:
        player.left = 100
    if player.y < 100:
        player.y = 100
    if player.right > WIDTH - 100:
        player.right = WIDTH - 100
    if player.bottom > HEIGHT - 105:
        player.bottom = HEIGHT - 105

# make an empty list
enemies = []
def create_enemy():
    e = Actor("ghost")
    # add to the enemy list
    enemies.append(e)


def move_enemies():
    for e in enemies:
        e.move_towards(player, 3)
    


# ************************** Built in functions ************************** #

# runs when any mouse button is pressed
def on_mouse_down(pos):
    print(pos)


# runs everytime update does
def draw():
    ''' define the draw function (built in to pygame zero automatically) '''
    bg.draw()
    player.draw()
    for enemy in enemies:
        enemy.draw()


# define the update function (runs a forever loop ---- while True) runs 60 times a second
def update():
    move_player()
    bound_player()
    create_enemy()
    move_enemies()

# last line of code
go()
