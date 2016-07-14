import curses
import loader
from screen import screen

def draw(path):
    color_active = curses.color_pair(1)
    color_inactive = curses.color_pair(2)

    screen.printcn(0, 0, 'SSDX')
    screen.printcn(1, 0, 'COMMANDDD')

    screen.printcn(3, 0, loader.get_current(path))

def limit_cursor(app_count):
    if screen.cpos[0] > 3 + app_count-1:
        screen.cpos[0] = 3 + app_count-1
    if screen.cpos[0] < 3:
        screen.cpos[0] = 3
    screen.cpos[1] = 1

