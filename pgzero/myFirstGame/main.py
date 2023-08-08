from pgzrun import go

WIDTH = 800
HEIGHT = 600

# Actors
npc = Actor('chicken1')
npc.x = 100
npc.y = 300


def draw():
    screen.fill('black')
    npc.draw()


def update():
    npc.x += 1
    if npc.image == 'chicken1':
        npc.image = 'chicken2'
    elif npc.image == 'chicken2':
        npc.image = 'chicken1'


def on_mouse_down(pos):
    print('you clicked me')


# last line of code
go()
