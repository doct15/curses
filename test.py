#!/usr/bin/env python
# -*- coding: latin-1 -*-

from os import system
import curses

myscreen = curses.initscr()

maxy = 24
maxx = 80
myscreen.clear()
curses.resizeterm(maxy, maxx)
myscreen.refresh()
quit = ord("q")

myscreen.move(1,1)
myscreen.addch(curses.ACS_ULCORNER)


def getinput():
  curses.noecho()
  while True:
      # get keyboard input, returns -1 if none available
      c = myscreen.getch()
      if c != -1:
          myscreen.move(0, 0)
          if (c == quit):
            #myscreen.addstr('Quit')
            break
            #myscreen.refresh()
  curses.endwin()

getinput()

