import curses
import time
import sys
from curses import wrapper
from random import randint
screen = curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
dims = screen.getmaxyx()
curses.curs_set(0)
curses.noecho()
dx, dy, mb = 0, 1, 0
life, grow = 3, 0
mx, my, fx, fy = 10, 10, 20, 20
snake = [[10, 10], [10, 11], [10, 12], [10, 13], [10, 14]]
c = 100
quit = 0


def main(stdscr):
    stdscr.clear()


def canexit():
    global quit
    return quit != 1


def step():  # method od one step
    global grow, life, fy, fx, mx, my, mb, grow, quit
    if grow != 1:
        snake.pop(0)
    else:
        grow = 0
    snake.append([((snake[len(snake) - 1][0]) + dx),
                  ((snake[len(snake) - 1][1]) + dy)])
    screen.clear()
    fawkes()
    mudblood()
    screen.addstr(dims[0] - 1, 1, "You killed " + str(mb) + " mudbloods")
    screen.addstr(dims[0] - 2, 1, "life: " + str(life))  # print score
    for i in range(0, len(snake)):
        wall(i)
        screen.addstr(snake[i][0], snake[i][1], "▓", curses.color_pair(3))
        if snake[i][0] == fx and snake[i][1] == fy:  # if it meet Fawkes
            life = life - 1
            fx = randint(2, dims[0] - 2)
            fy = randint(2, dims[1] - 2)
    if snake[i][0] == mx and snake[i][1] == my:  # eating
        mb = mb + 1
        grow = 1
        mx = randint(2, dims[0] - 2)
        my = randint(2, dims[1] - 2)
        screen.refresh()
    if life < 1:
        quit = 1


def wall(i):  # cross walls
    if snake[i][0] == 0:
        snake[i][0] = dims[0] - 1
    if snake[i][1] == 0:
        snake[i][1] = dims[1] - 1
    if snake[i][0] == dims[0]:
        snake[i][0] = 1
    if snake[i][1] == dims[1]:
        snake[i][1] = 1


def move():  # reaction to users input
    global dx, dy, c, quit
    screen.nodelay(True)
    c = screen.getch()
    if c == 100:
        if dy != -1:
            dy = 1
            dx = 0
    elif c == 97:
        if dy != 1:
            dy = -1
            dx = 0
    elif c == 115:
        if dx != -1:
            dy = 0
            dx = 1
    elif c == 119:
        if dx != 1:
            dy = 0
            dx = -1
    elif c == 27:
        quit = 1
    step()
    if snake[0] in snake[1:]:
        quit = 1
    time.sleep(0.5 / (1 + mb))


def mudblood():
    global mx, my, mb
    m = [mx, my]
    mx = mx + randint(-1, 1)
    my = my + randint(-1, 1)
    if mx < 2:
        mx = dims[1] - 4
    if my < 2:
        my = dims[0] - 4
    if mx > dims[0] - 4:
        mx = 2
    if my > dims[1] - 4:
        my = 2
    screen.addstr(mx, my, "i", curses.color_pair(1))


def fawkes():
    global fx, fy, pb
    f = [fx, fy]
    fx = fx + randint(-1, 1)
    fy = fy + randint(-1, 1)
    if fx < 2:
        fx = dims[1] - 4
    if fy < 2:
        fy = dims[0] - 4
    if fx > dims[0] - 4:
        fx = 2
    if fy > dims[1] - 4:
        fy = 2
    screen.addstr(fx, fy, "~.~", curses.color_pair(2))
