from pgzrun import go
from random import randint

# screen size
WIDTH = 800
HEIGHT = 600

# actors
slime = Actor('slime', pos=(400, 300))
slime.wait_time = 60
slime.counter = slime.wait_time
slime.last_hole = 0

hole1 = Actor('hole', pos=(200, 300))
hole2 = Actor('hole', pos=(600, 300))

# global variable
score = 0


def draw():
    screen.fill("green")
    slime.draw()
    hole1.draw()
    hole2.draw()


# runs 60 times per second
def update():
    place_slime()


def on_mouse_down(pos):
    global score
    if slime.collidepoint(pos):
        score += 1
        print(score)


def place_slime():
    slime.counter = slime.counter - 1
    if slime.counter <= 0:
        slime.counter = slime.wait_time
        rand_num = randint(1, 2)
        if slime.last_hole == rand_num:
            rand_num = randint(1, 2)
        slime.last_hole = rand_num
        if rand_num == 1:
            slime.x = hole1.x
            slime.y = hole1.y - 25
        elif rand_num == 2:
            slime.x = hole2.x
            slime.y = hole2.y - 25


# Must be the last line

go()
