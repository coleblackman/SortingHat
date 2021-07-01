from curses import wrapper
import curses

def main(screen):
    # Clear screen
    screen.clear()
    screen.border(0)

    intro = 'Sorting Hat'

    # Remember integer division vs float division in python (weird-ass language)

    #screen.addstr(curses.LINES // 2, curses.COLS // (2-len(intro)) // 2, intro)
    screen.addstr(0, curses.COLS//2 - 5, intro)
    screen.refresh()
    screen.getkey()

wrapper(main)
