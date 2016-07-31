#!/usr/bin/env python
# -*- coding: latin-1 -*-

from os import system
import curses

currentx = 3
currenty = 3
map_locx = 2
map_locy = 2
msg_locx = 10
msg_locy = 2
map_width = 5
#dngn_viewx = 3
#dngn_viewy = 3
go_left = ord("a")
go_right = ord("d")
go_up = ord("w")
go_down = ord("s")
quit = ord("q")
you = "*"
#print ("left", go_left)

#exit()

map = [
  " 0    ",
  "012345",
  " 2  x ",
  " 3  x ",
  " 4xxx ",
  " 5    "
  ]

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

myscreen = curses.initscr()
#maxy, maxx = myscreen.getmaxyx()
maxy = 24
maxx = 80
myscreen.clear()
curses.resizeterm(maxy, maxx)
myscreen.refresh()

def main():
  draw_border()
  myscreen.getch()
  print_dngn(currentx,currenty)
  #myscreen.move(0, 0)
  #myscreen.addstr(12,12 , "quit")
  getinput()


def draw_border():
  for y in range (0, maxy-1):
    for x in range (0, maxx-1):
      if (y < 1) or (y > maxy-3) or (x < 1) or (x > maxx-3):
        myscreen.addstr(y,x , ".")
        #print(x, y)
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
