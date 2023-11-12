import pgzrun

WIDTH = 800
HEIGHT = 500

# different screen states
start_screen = True
main_screen = False
game_over_screen = False
win_screen = False

player = Actor("piranha")
player.bottom = HEIGHT
player.health = 20
player.score = 0

worm = Actor("worm_walk")
worm.bottom = 0
worm.speed = 3
worm.animation_timer = 20

kemo_is_silly_rect = Rect(20, 20, 200, 100)
retry_button = Rect(300, 300, 200, 50)


def draw():
    if start_screen:
        # draw a title and a start button (later add levels and saving)
        pass
    elif main_screen:
        screen.fill("navy")
        screen.draw.text(f"Health:{player.health}", (20, 20), fontsize=35)
        # display score
        player.draw()
        worm.draw()
    elif game_over_screen:
        screen.draw.text("Game Over")
    elif win_screen:
        # draw a win screen and maybe a playe again button
        pass


def on_mouse_down(pos):
    global game_over_screen
    global main_screen
    # checks if the mouse is clicking on the retry button
    if retry_button.collidepoint(pos):
        player.health = 20
        player.score = 0
        game_over_screen = False
        main_screen = True


def update():
    # moves left and right
    if keyboard.left:
        player.x -= 5
    if keyboard.right:
        player.x += 5


pgzrun.go()