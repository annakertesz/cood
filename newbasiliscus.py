import time
import newharrypotter
import curses
from curses import wrapper
screen = curses.initscr()
curses.curs_set(0)
print("sss")
while newharrypotter.canexit():
    newharrypotter.step()
screen.clear()
if newharrypotter.is_win():
    print("You Win")
else:
    print("Game over")
time.sleep(5)
curses.endwin()
curses.wrapper
