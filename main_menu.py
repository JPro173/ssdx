import curses
import loader
from screen import screen

def draw():
    color_active = curses.color_pair(1)
    color_inactive = curses.color_pair(2)

    screen.printcn(0, 0, 'SSDX')
    screen.printcn(1, 0, 'choose application')

    apps = loader.get_apps()
    app_names = list(apps.keys())

    limit_cursor(len(app_names))

    for i in range(screen.mpos[0]):
        active =  i+3 == screen.cpos[0]

        color = color_active if active else color_inactive

        if i < len(app_names):
            screen.println(i+3, 1, apps[app_names[i]]['title'], color)

def limit_cursor(app_count):
    if screen.cpos[0] > 3 + app_count-1:
        screen.cpos[0] = 3 + app_count-1
    if screen.cpos[0] < 3:
        screen.cpos[0] = 3

    screen.cpos[1] = 1

