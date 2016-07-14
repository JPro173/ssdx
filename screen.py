import curses


class Screen:
    def start(self, stdscr):
        self.stdscr = stdscr
        stdscr.clear()
        stdscr.refresh()

        self.mpos = stdscr.getmaxyx()
        self.cpos = [3, 0]

    def full_line(self, text):
        return ' ' + text + ' '*(self.mpos[1]-len(text)-3)

    def clear(self):
        self.stdscr.clear()
        self.stdscr.refresh()

    def println(self, y, x, text, color=0):
        self.stdscr.addstr(y, x, self.full_line(text), color)

    def printcn(self, y, x, text, color=0):
        self.stdscr.addstr(y, x, ('{:^'+str(self.mpos[1])+'}').format(text), color)

    def validate_cursor(self):
        self.stdscr.addstr(self.cpos[0], self.cpos[1], '')

    def cursor_pos(self, pos=None):
        if pos:
            self.cpos = pos
            self.stdscr.addstr(pos[0], pos[1], '')
        else:
            return self.cpos

    def cursor_down(self):
        self.cpos[0] += 1
        self.cpos[0] = self.cpos[0] if self.cpos[0] < self.mpos[0] else self.mpos[0]-1
        curses.setsyx(*self.cpos)
        curses.doupdate()

    def cursor_up(self):
        self.cpos[0] -= 1
        self.cpos[0] = self.cpos[0] if self.cpos[0] > 0 else 0
        curses.setsyx(*self.cpos)
        curses.doupdate()

    def cursor_left(self):
        self.cpos[1] -= 1
        self.cpos[1] = self.cpos[1] if self.cpos[1] > 0 else 0
        curses.setsyx(*self.cpos)
        curses.doupdate()

    def cursor_right(self):
        self.cpos[1] += 1
        self.cpos[1] = self.cpos[1] if self.cpos[1] < self.mpos[1] else self.mpos[1]-1
        curses.setsyx(*self.cpos)
        curses.doupdate()

screen = Screen()

