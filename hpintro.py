import curses
screen = curses.initscr()
dims = screen.getmaxyx()
def intro():
    welcome1 = "Long time ago, Hogwarts was the best school for wizards"
    welcome2= "but some weak, guileless people ruined it."
    welcome3= "As the Heir of Slytherin, it's your job to restore the old glory"
    welcome4= "Use the Basiliscus to kill mudbloods, but be careful with Fawkes!"
    welcome5= "You can control the snake with 'w' 'a' 's' 'd'"
    welcome =([welcome1], [welcome2], [welcome3], [welcome4], [welcome5])
    screen.clear()
    screen.addstr(3, int((dims[1])/2-len(welcome1)/2), str(welcome1))
    screen.addstr(4, int((dims[1])/2-len(welcome2)/2), str(welcome2))
    screen.addstr(5, int((dims[1])/2-len(welcome3)/2), str(welcome3))
    screen.addstr(6, int((dims[1])/2-len(welcome4)/2), str(welcome4))
    screen.addstr(9, int((dims[1])/2-len(welcome5)/2), str(welcome5))
    screen.addstr(int(dims[0]-1), 2, "Press any key to countinue")
    hogwarts()
    screen.refresh()
    screen.getch()
def hogwarts():
    screen.addstr(dims[0]-13, 1, "                          _/\_ ")
    screen.addstr(dims[0]-12, 1, "                         /    \ ")
    screen.addstr(dims[0]-11, 1, "  .                     /      \ ")
    screen.addstr(dims[0]-10, 1, " / \                    |÷÷÷÷÷÷|   ¶")
    screen.addstr(dims[0]-9, 1, "/   \       wwwwww      |-[==]-|  / \ ")
    screen.addstr(dims[0]-8, 1, "|ooo|       |    |      ||    ||  |O|              ~.~")
    screen.addstr(dims[0]-7, 1, "|||||       | [] |      ||÷÷÷÷||__|-|")
    screen.addstr(dims[0]-6, 1, "|||||       |    |      ||    ||____|         O")
    screen.addstr(dims[0]-5, 1, "|||||===Ħ.Ħ.Ħ.Ħ.Ħ.Ħ.Ħ.Ħ.Ħ.|   ||            O |  O")
    screen.addstr(dims[0]-4, 1, "|||||   | [] [] |         |   ||            | |  |")
    screen.addstr(dims[0]-3, 1, "|||||   |       |         |   ||            | |  |")
    screen.addstr(dims[0]-2, 1, "------------------------------------------------------------------------")
    screen.addstr(dims[0]-1, 1, " ")
