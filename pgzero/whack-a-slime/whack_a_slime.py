from pgzrun import go
from random import randint

# screen size
WIDTH = 800
HEIGHT = 600

# actors
slime = Actor('slime')
slime.x = 400
slime.y = 300

hole1 = Actor('hole')
hole1.x = 200
hole1.y = 300

hole2 = Actor('hole')
hole2.x = 600
hole2.y = 300


# runs 60 times per second
def draw():
    screen.fill('olive')
    slime.draw()
    hole1.draw()
    hole2.draw()


# runs 60 times per second
def update():
    rand_num = randint(1, 2)
    if rand_num == 1:
        slime.x = hole1.x
        slime.y = hole1.y - 25
    elif rand_num == 2:
        slime.x = hole2.x
        slime.y = hole2.y - 25


# Must be the last line
go()
