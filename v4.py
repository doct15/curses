#!/usr/bin/env python
# -*- coding: latin-1 -*-

from os import system
import curses

currentx = 2
currenty = 2
map_locx = 2
map_locy = 2
#dngn_viewx = 3
#dngn_viewy = 3

map = [
  " 0    ",
  "012345",
  " 2  x ",
  " 3  x ",
  " 4xxx ",
  " 5    "
  ]

myscreen = curses.initscr()

#maxy, maxx = myscreen.getmaxyx()
maxy = 24
maxx = 80
myscreen.clear()
curses.resizeterm(maxy, maxx)
myscreen.refresh()

def main():
  for y in range (0, maxy-1):
    for x in range (0, maxx-1):
      if (y < 1) or (y > maxy-3) or (x < 1) or (x > maxx-3):
        myscreen.addstr(y,x , ".")
        #print(x, y)
        myscreen.refresh()
  myscreen.getch()
  print_dngn(currentx,currenty)
  myscreen.getch()
  curses.endwin()

def print_dngn(x,y):
  "This draws the dungeon"
  myscreen.addstr(map_locy, map_locx, "")
  for y in range (currenty-1, currenty+2):
    #print ('Y:', y)
    #print (map_locx, map_locy)
    #print (currentx, currenty)
    myscreen.addstr((map_locy+(y-currenty))+1,map_locx,map[y][currentx-1:currentx+2])
      
  return;
  
main()  
