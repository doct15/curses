#!/usr/bin/python3.5
# -*- coding: latin-1 -*-

from os import system
import curses
import sys
sys.path
ADJY=10
GRID_SIZE=6
for z in range(GRID_SIZE):
  y=z * (ADJY - z)
  #print (z," * ",ADJY," - ",z," = ",y)
  #print ("z",z,"y",y)

stop

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

