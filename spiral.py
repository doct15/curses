#!/usr/bin/python3.5
# -*- coding: latin-1 -*-

#Global Stuff
from os import system
import sys
import curses
import pygame
import math
import time
from graphics import *

#How big in pixels are the walls/floor
gsize=20
gradius=int(gsize/2)

#The screen resolution
screenmax_x=800
screenmax_y=600

#Colors
light_grey = (64,64,64)
black = (0,0,0)
yellow = (255,255,0)
white = (255,255,255)
green = (0,255,0)
blue = (0,0,255)
grey = (127,127,127)
red = (255,0,0)
royalblue = (65,105,225)

#More Global stuff
pygame.init()
size = (screenmax_x,screenmax_y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Spiral Test1")

#Key bindings
turn_left = pygame.K_a
turn_right = pygame.K_d
go_forward = pygame.K_w
go_backward = pygame.K_s
quit = pygame.K_q

radian=math.pi/180
spiralstart=0
spiralend=360
radiusoffset=.01
radiusstart=1
centerx=int(screenmax_x/2)
centery=int(screenmax_y/2)
currentangle=spiralstart
circleradius=1
circlewidth=0

def main():
	print("Testing")
	getinput()

def getinput():
  global currentangle,radiusoffset
  while True:
    x=int(centerx+math.sin(currentangle*radian)*(currentangle*radiusoffset))
    y=int(centery+math.cos(currentangle*radian)*(currentangle*radiusoffset))
    pygame.draw.circle(screen,yellow,[x,y],circleradius,circlewidth)
    print(currentangle,x,y)
    currentangle=currentangle+1
    radiusoffset=radiusoffset+(radiusoffset*.0001)
    pygame.display.flip()
    #time.sleep(1)
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == quit:
          quit()
        elif (event.key == turn_left) or (event.key == pygame.K_LEFT):
          turn_left()
        elif (event.key == go_forward) or (event.key == pygame.K_UP):
          go_forward()
        elif (event.key == turn_right) or (event.key == pygame.K_RIGHT):
          turn_right()
        elif (event.key == go_backward) or (event.key == pygame.K_DOWN):
          go_backward()
        elif event.key == pygame.K_b:
          return "b"
          break

main()