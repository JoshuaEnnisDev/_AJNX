from pgzrun import go

# screen setup
WIDTH = 1500
HEIGHT = 896
TITLE = "Survivor Game"

# create the background actor and store in a variable
bg = Actor("dungeon1")


# define the draw function (built in to pygame zero automatically)
def draw():
    bg.draw()


# last line of code
go()