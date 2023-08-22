from pgzrun import go

WIDTH = 800
HEIGHT = 600

slime = Actor('slime')
slime.x = 650
slime.y = 385

def draw():
    slime.draw()

# Must be the last line
go()
