#!/usr/bin/env python
# -*- coding: latin-1 -*-

from os import system
import sys
import curses
import pygame
from graphics import *

gsize=20
gradius=int(gsize/2)
map_placementx=33
map_placementy=31
map_max_x=5
map_hmax_x=int(map_max_x/2)
map_max_y=map_max_x
map_hmax_y=int(map_max_y/2)
screenmax_x=640
screenmax_y=480
currentx = 3
currenty = 3
light_grey = (64,64,64)
black = (0,0,0)
yellow = (255,255,0)
divisor = 20
white = (255,255,255)
green = (0,255,0)

wall_fill = light_grey
wall_outline = yellow
background_color = black

go_left = pygame.K_a
go_right = pygame.K_d
go_up = pygame.K_w
go_down = pygame.K_s
quit = pygame.K_q

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

pygame.init()
size = (screenmax_x,screenmax_y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")


def main():
  clock = pygame.time.Clock()
  #print_grid()
  print_dngn(currentx,currenty)
  getinput()

def draw_wall(tx,ty):
    pygame.draw.rect(screen,wall_outline,[tx,ty,gsize,gsize],1)
    pygame.draw.rect(screen,wall_fill,[tx+1,ty+1,gsize-2,gsize-2])

def clear_dngn():
  pygame.draw.rect(screen,background_color,[map_placementx,map_placementy,map_placementx+gsize*map_max_x,map_placementy+gsize*map_max_y])


def print_dngn(pdcx,pdcy):
  for y in range (0,map_max_y):
    for x in range (0,map_max_x):
      dcx = x + pdcx - map_hmax_x
      dcy = y + pdcy - map_hmax_y
      dngn_char=map[dcy][dcx:dcx+1]
      mapx = x * gsize + map_placementx
      mapy = y * gsize + map_placementy
      if (dngn_char != " "):
        draw_wall(mapx,mapy)
  pygame.display.flip()

def print_grid():
  font = pygame.font.Font(None, 12)
  xstep = screenmax_x/(screenmax_x/divisor)
  ystep = screenmax_y/(screenmax_y/divisor)
  for x in xrange(0,screenmax_x,xstep):
    pygame.draw.line(screen,yellow,(x,0),(x,screenmax_y))
    pygame.draw.rect(screen,black,(x,0,x+xstep,ystep))
    text = font.render(str(x), 1, white)
    screen.blit(text, (x,0))
  for y in xrange(0,screenmax_y,ystep):
    pygame.draw.line(screen,yellow,(0,y),(screenmax_x,y))
    pygame.draw.rect(screen,black,(0,y,xstep,y+ystep))
    text = font.render(str(y), 1, white)
    screen.blit(text, (0,y))
  pygame.display.flip()

def getinput():
  while True:
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == quit:
          quit()
        elif (event.key == go_left):
          #myscreen.addstr(msg_locy,msg_locx,"Left")
          move_left()
        elif (event.key == go_up):
          #myscreen.addstr(msg_locy,msg_locx,"Up")
          move_up()
        elif (event.key == go_right):
          #myscreen.addstr(msg_locy,msg_locx,"Right")
          move_right()
        elif (event.key == go_down):
          #myscreen.addstr(msg_locy,msg_locx,"Down")
          move_down()
        elif event.key == pygame.K_b:
          return "b"
          break

def check_move(x,y):
  global currentx, currenty
  if (map[y][x] == " "):
    currentx = x
    currenty = y
    clear_dngn()
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

main()  
