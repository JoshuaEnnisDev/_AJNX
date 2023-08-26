from pgzrun import go

# screen size
WIDTH = 800
HEIGHT = 600
mouse_pos = (0, 0)

# actors
slime = Actor('slime', pos=(400, 300))

hole1 = Actor('hole')
hole1.x = 200
hole1.y = 300

hole2 = Actor('hole')
hole2.x = 600
hole2.y = 300

help(Actor)


# runs 60 times per second
def draw():
    slime.draw()
    hole1.draw()
    hole2.draw()


def on_mouse_move(pos):
    screen.draw.text(f"({pos[0]}, {pos[1]})", (pos[0] + 10, pos[1]))


# runs 60 times per second
def update():
    # rand_num = randint(1, 2)
    # if rand_num == 1:
    #     slime.x = hole1.x
    #     slime.y = hole1.y - 25
    # elif rand_num == 2:
    #     slime.x = hole2.x
    #     slime.y = hole2.y - 25
    screen.draw.text("hello", (10, 10))
    if keyboard.d:

        slime.x += slime.speed


def test():
    pass


# Must be the last line
go()
