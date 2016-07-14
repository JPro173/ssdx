import main_menu
import app_menu
import command_menu
from screen import screen

state = 0
path = None

def draw():
    screen.clear()
    if state == 0:
        main_menu.draw()
    elif state >= 1:
        app_menu.draw(path)
    elif state <= -1:
        command_menu.draw(path)
    screen.validate_cursor()
    print(str(state)+' '+str(path))

