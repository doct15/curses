#!/usr/bin/env python
# -*- coding: latin-1 -*-

from os import system
import sys
import curses

currentx = 3
currenty = 3
#map_locx = 2
#map_locy = 2
msg_locx = 10
msg_locy = 2
map_width = 5
maxy_screen = 24
maxx_screen = 80
#dngn_viewx = 3
#dngn_viewy = 3
go_left = ord("a")
go_right = ord("d")
go_up = ord("w")
go_down = ord("s")
quit = ord("q")
you = "*"

map_locx = maxx_screen - (map_width+3)
map_locy = 3

map_file = sys.argv[1]
map = [line for line in open(map_file, 'r')]

#print (map)

if (0):
  map = [
    "                  ",
    "                  ",
    "  +------------+  ",
    "  |            |  ",
    "  | +--------+ |  ",
    "  | |        | |  ",
    "  | +---+ +--+ |  ",
    "  |            |  ",
    "  +------------+  ",
    "                  ",
    "                  "
    ]

#print (map)

#quit()

myscreen = curses.initscr()
#maxy, maxx = myscreen.getmaxyx()
myscreen.clear()
curses.resizeterm((maxy_screen+1), maxx_screen)
myscreen.refresh()

def main():
  draw_border(0,0,maxx_screen,maxy_screen)
  draw_border(map_locx-2, map_locy-2, map_locx+map_width+2, map_locy+map_width+1)
  myscreen.getch()
  print_dngn(currentx,currenty)
  #myscreen.move(0, 0)
  #myscreen.addstr(12,12 , "quit")
  getinput()


def draw_border(startx,starty,maxx,maxy):
  for y in range (starty, maxy):
    if (y == starty):
      myscreen.addch(starty,startx,curses.ACS_ULCORNER)
      for x in range (startx+1, maxx-1):
        myscreen.addch(starty,x,curses.ACS_HLINE)
      myscreen.addch(starty,maxx-1,curses.ACS_URCORNER)
    elif (y == maxy-1):
      #print ("DOIT")
      myscreen.addch(maxy-1,startx,curses.ACS_LLCORNER)
      for x in range (startx+1, maxx-1):
        myscreen.addch(maxy-1,x,curses.ACS_HLINE)
      myscreen.addch(maxy-1,maxx-1,curses.ACS_LRCORNER)
      break
    else:
      myscreen.addch(y,startx,curses.ACS_VLINE)
      #myscreen.addstr(y,startx,str(y))
      myscreen.addch(y,maxx-1,curses.ACS_VLINE)
    myscreen.refresh()


def getinput():
  curses.noecho()
  while True:
      # get keyboard input, returns -1 if none available
      c = myscreen.getch()
      if c != -1:
          # print numeric value
          #myscreen.addstr('C:' + str(c) + ' |')
          #myscreen.refresh()
          # return curser to start position
          #reset_cursor()
          if (c == go_left):
            #myscreen.addstr(msg_locy,msg_locx,"Left")
            move_left()
          elif (c == go_up):
            #myscreen.addstr(msg_locy,msg_locx,"Up")
            move_up()
          elif (c == go_right):
            #myscreen.addstr(msg_locy,msg_locx,"Right")
            move_right()
          elif (c == go_down):
            #myscreen.addstr(msg_locy,msg_locx,"Down")
            move_down()
          elif (c == quit):
            #myscreen.addstr('Quit')
            break
          # myscreen.refresh()
  curses.endwin()

def check_move(x,y):
  global currentx, currenty, map
  #print ("CX", currentx, "CY", currenty, "X", x, "Y" , y , "MAP:", map[y][x], "|")
  if (map[y][x] == " "):
    currentx = x
    currenty = y
    print_dngn(currentx,currenty)
    return 0
  else:
    #print ("BONK")
    return 1



def move_left():
  check_move(currentx-1,currenty)

def move_right():
  check_move(currentx+1,currenty)

def move_up():
  check_move(currentx,currenty-1)

def move_down():
  check_move(currentx,currenty+1)


def print_dngn(x,y):
  "This draws the dungeon"
  global map_locx, map_locy, map_width, map
  myscreen.addstr(map_locy, map_locx, "")
  #for y in range (currenty-1, currenty+2):
  for y in range (currenty-int(map_width/2), currenty+int(map_width/2)+1):
    #print ('Y:', y)
    #print (map_locx, map_locy)
    #print (currentx, currenty)
    myscreen.addstr((map_locy+(y-currenty))+1,map_locx,map[y][currentx-int(map_width/2):currentx+int(map_width/2)+1])
  myscreen.addstr(map_locy+int(map_width/2)-1,map_locx+int(map_width/2),you)    
  reset_cursor()
  return;
  
def reset_cursor():
  myscreen.addstr(0,0, "")

main()  
