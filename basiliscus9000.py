import time, harrypotter, hpintro, curses
from curses import wrapper
curses.curs_set(0)
screen = curses.initscr()
dims = screen.getmaxyx()
bye = "Thanks for helping Mardekar to clean Hogwarts"
mb = 0
pb = 0
quit=0
life = 3
snake = [[10,10], [10,11], [10,12]]
c = 100
hpintro.intro()
while harrypotter.canexit():
    harrypotter.move()
screen.clear()
screen.addstr(5, int((dims[1])/2-len(bye)/2), str(bye))
screen.refresh()
time.sleep(4)
