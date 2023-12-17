from pgzrun import go

# screen setup
WIDTH = 1500
HEIGHT = 896
TITLE = "Survivor Game"

# create the background actor and store in a variable
bg = Actor("dungeon1")

# create player Actor
player = Actor("green_guy")



###########################Built in functions###############
# define the draw function (built in to pygame zero automatically)
def draw():
    bg.draw()
    player.draw()


# define the update function (runs a forever loop ---- while True) runs 60 times a second
def update():
    pass

# last line of code
go()