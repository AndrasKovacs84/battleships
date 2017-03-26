import curses

screen = curses.initscr()
screen.addstr("Hello World!!!")
screen.refresh()
screen.getch()
curses.endwin()

''' Contains functions to check if they meet certain criteria.
E.g.: if player is ok, or if a ship can be placed in a certain location.'''
