import curses
from curses import wrapper

import loader
import panel
from screen import screen
from app_path import Path

stdscr = curses.initscr()

curses.noecho()
curses.cbreak()

stdscr.keypad(True)

def main(stdscr):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

    screen.start(stdscr)
    panel.draw()

    while True:
        try:
            key = stdscr.getkey()
            key_processor(stdscr, key)
        except KeyboardInterrupt:
            exit(1)

def key_processor(stdscr, key):
    if key == 'h':
        screen.cursor_left()
    elif key == 'l':
        screen.cursor_right()
    elif key == 'k':
        screen.cursor_up()
    elif key == 'j':
        screen.cursor_down()
    elif key == 'b':
        if panel.state < 0:
            panel.state *= -1
            screen.cpos[0] = 3
            panel.state -= 1
        elif panel.state > 0:
            if len(panel.path):
                panel.path.pop()
            panel.state -= 1
            screen.cpos[0] = 3
    elif key == 'y':
        cursor_y = screen.cursor_pos()[0] - 3

        panel.state += 1
        if panel.state == 1:
            panel.path = Path(cursor_y)
        else:
            panel.path.append(cursor_y)
        screen.cpos[0] = 3
        if str(type(loader.get_list(panel.path))) == 'unicode':
            panel.state *= -1
            #panel.path.pop()
    panel.draw()

wrapper(main)

