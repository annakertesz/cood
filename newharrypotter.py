import curses
import time
import sys
from curses import wrapper
from random import randint
screen = curses.initscr()
dims = screen.getmaxyx()
curses.start_color()
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.noecho()
dx, dy = 1, 0
mb_x, mb_y = 10, 10
fx, fy = 20, 20
snake = [[10, 10], [10, 11], [10, 12], [10, 13], [10, 14]]
quit, already_have = 0, 0
hx, hy = 10, 10
horcruxes = [["", " "], ["-o-", "Medál"], ["|-<", "Serleg"],
             ["\/", "Napló"], ["O", "Gyűrű"], ["-ww-", "Diadém"], ["S", "Nagini"]]
mylist = [["", ""]]
score = 1
life = 10


def is_win():
    global already_have, snake, quit
    if already_have == 6:
        quit = 1
        return True


def is_dead():
    global life, snake, quit
    if life == 0:
        quit = 1
    if snake[0] in snake[1:]:
        quit = 1


def appears(dx, dy):  # the snake appears
    global snake
    snake.append([((snake[len(snake) - 1][0]) + dx),
                  ((snake[len(snake) - 1][1]) + dy)])
    if mudbloods() == False:
        snake.pop(0)
    else:
        print ("yeah")
    screen.clear()
    for i in range(0, len(snake)):
        screen.addstr(snake[i][0], snake[i][1], "x", curses.color_pair(3))
    if snake[0] in snake[1:]:
        quit = 1


def horcrux():
    global already_have, hx, hy, horcruxes, dims, snake, score, mylist
    if score % 3 == 0:
        # horcruxes[already_have])
        screen.addstr(hx, hy, horcruxes[already_have + 1][0])
        if (snake[len(snake) -
                  1][1] == hy or snake[len(snake) -
                                       1][1] == hy +
            1 or snake[len(snake) -
                       1][1] == hy +
            2) and snake[len(snake) -
                         1][0] == hx:  # H_eating
            score += 1
            screen.addstr(hx, hy, "    ")
            hx = randint(2, dims[0] - 2)
            hy = randint(2, dims[1] - 14)
            screen.refresh()
            already_have += 1
            mylist.append(horcruxes[already_have])


def fawkes():
    global fx, fy, snake, life, quit
    fx = fx + randint(-1, 1)
    fy = fy + randint(-1, 1)
    for i in range(0, len(snake)):
        if snake[i][0] == fx and snake[i][1] == fy:  # if it meet Fawkes
            life = life - 1
            if life < 0:
                quit = 1
            fx = randint(5, dims[0] - 5)
            fy = randint(5, dims[1] - 14)
    if (fx < 4) or (fy < 4) or (fx > (dims[0] - 4)) or (fy > (dims[1] - 14)):
        fx = (randint(5, dims[0] - 5))
        fy = (randint(5, dims[1] - 14))
    screen.addstr(fx, fy, "~.~")


def press():  # control function
    global dx, dy
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


def canexit():
    global quit
    return quit == 0


def mudbloods():
    global mb_x, mb_y, did_catch, dims, dx, dy, score
    did_catch = False
    screen.addstr(mb_x, mb_y, "i")
    if (snake[len(snake) - 1][0]
        ) == mb_x and (snake[len(snake) - 1][1]) == mb_y:
        mb_x = (randint(2, dims[0] - 2))
        mb_y = (randint(2, dims[1] - 14))
        did_catch = True
        score += 1
    return did_catch


def walls(dims):
    for i in range(0, len(snake)):
        if snake[i][0] == 1:
            snake[i][0] = dims[0] - 2
        if snake[i][1] == 1:
            snake[i][1] = dims[1] - 15
        if snake[i][0] == dims[0] - 1:
            snake[i][0] = 2
        if snake[i][1] == dims[1] - 14:
            snake[i][1] = 2


def step():  # one complet step
    global score
    press()
    appears(dx, dy)
    walls(dims)
    mudbloods()
    fawkes()
    is_dead()
    horcrux()
    is_win()
    time.sleep(1 / score)
