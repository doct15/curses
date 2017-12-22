#!/usr/bin/env python
# -*- coding: latin-1 -*-

from os import system
import sys
import curses
import pygame
from graphics import *

gsize=20
gradius=int(gsize/2)
map_placementx=20
map_placementy=20
map_max_x=2
map_hmax_x=int(map_max_x/2)
map_max_y=map_max_x
map_hmax_y=int(map_max_y/2)
screenmax_x=640
screenmax_y=480
currentx = 3
currenty = 3
light_grey = (64,64,64)
wall_fill = light_grey
black = (0,0,0)
yellow = (255,255,0)


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

quit = pygame.K_q


def main():
  pygame.display.set_caption("My Game")
   
  # Loop until the user clicks the close button.
  #done = False
   
  # Used to manage how fast the screen updates
  clock = pygame.time.Clock()
  #get_keys_pressed()
  print_dngn()
  getinput()

def getinput():
  while True:
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == quit:
          quit()
        elif event.key == pygame.K_a:
          print("A")
        elif event.key == pygame.K_b:
          return "b"
          break
        elif event.key == pygame.K_q:
          print("Q")

def print_dngn():
  #global screen
  #This draws the dungeon
  #global map_locx, map_locy, map_max_x, map, currentx, currenty
  for y in range (0,map_max_y):
    for x in range (0,map_max_x):
      dcx = x + currentx - map_hmax_x
      dcy = y + currenty - map_hmax_y
      dngn_char=map[dcy][dcx:dcx+1]
      mapx = x * gsize + map_placementx
      mapy = y * gsize + map_placementy

      #print ("dngn",dngn_char,x,y)
      #print ("map",mapx,mapy,gsize)

      if (dngn_char != " "):
        draw_wall(mapx,mapy)

      #getinput()

def draw_wall(tx,ty):
    #global screen
    #print ("1x",x,y,gsize)
    print ("rect",tx,ty,tx+gsize-1,ty+gsize-1)
    pygame.draw.rect(screen,yellow,[tx,ty,tx+gsize-1,ty+gsize-1])
    pygame.draw.rect(screen,wall_fill,[tx+1,ty+1,tx+gsize-2,ty+gsize-2])
    #pygame.draw.rect(screen,yellow,[tx+3,ty+3,tx+gsize-3,ty+gsize-3])
    pygame.display.flip()
    a = getinput()


pygame.init()
size = (screenmax_x,screenmax_y)
screen = pygame.display.set_mode(size)

main()  
