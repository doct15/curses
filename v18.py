#!/usr/bin/python3.5
# -*- coding: latin-1 -*-

#Global Stuff
from os import system
import sys
import curses
import pygame
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
pygame.display.set_caption("dngn")

#The in-game map number of squares shown (3 or 5?)
map_max_x=5
map_hmax_x=int(map_max_x/2)
map_max_y=map_max_x
map_hmax_y=int(map_max_y/2)

#Map location on the screen x,y
map_placementx=screenmax_x-gsize*(map_max_x+1)-1
map_placementy=gsize+1

#The users current location in the dungeon
currentx=6
currenty=4
direction=0

#Color assignments
wall_fill = light_grey
wall_outline = yellow
background_color = black
border_color = blue
border_width = 2
dude_color = green

#Key bindings
turn_left = pygame.K_a
turn_right = pygame.K_d
go_forward = pygame.K_w
go_backward = pygame.K_s
quit = pygame.K_q

#Debug/test dungeon map
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
  
#map_file = sys.argv[1]
map_file = "map2.txt"
map = [line for line in open(map_file, 'r')]

#Map status line info
map_statusx = screenmax_x-gsize*(map_max_x+1)-1
map_statusy = gsize*(map_max_x+2)
map_statussize = 18
map_statuswidth = (map_max_x+1)*gsize-1

#Define 3d map area
map_3d_x=gsize
map_3d_y=gsize*(map_max_y+1)+2
map_3d_width=map_statusx-gsize-1
map_3d_height=screenmax_y-gsize*7

#Define direction movements
#0=Left
#1=Up
#2=Right
#3=Down
dirx=[-1,0,1,0]
diry=[0,-1,0,1]

#Define 3d hallway size

#Define 3d hallway points
xpoints=[i for i in range(12)]
xpoints[0]=1
xpoints[5]=int(map_3d_width/2)-int(int(map_3d_width/26)/2)
hallway_length=xpoints[5]-xpoints[0]
xpoints[1]=xpoints[0]+int(hallway_length*.3)
xpoints[2]=xpoints[1]+int(hallway_length*.25)
xpoints[3]=xpoints[2]+int(hallway_length*.2)
xpoints[4]=xpoints[3]+int(hallway_length*.15)
xpoints[11]=map_3d_width-xpoints[0]
xpoints[10]=map_3d_width-xpoints[1]
xpoints[9]=map_3d_width-xpoints[2]
xpoints[8]=map_3d_width-xpoints[3]
xpoints[7]=map_3d_width-xpoints[4]
xpoints[6]=map_3d_width-xpoints[5]
ypoints_top=[i for i in range(12)]
ypoints_top[0]=1
ypoints_top[5]=int(map_3d_height/2)-int(int(map_3d_height/18.4)/2)
hallway_height=ypoints_top[5]-ypoints_top[0]
ypoints_top[1]=ypoints_top[0]+int(hallway_height*.3)
ypoints_top[2]=ypoints_top[1]+int(hallway_height*.25)
ypoints_top[3]=ypoints_top[2]+int(hallway_height*.2)
ypoints_top[4]=ypoints_top[3]+int(hallway_height*.15)
ypoints_top[11]=ypoints_top[0]
ypoints_top[10]=ypoints_top[1]
ypoints_top[9]=ypoints_top[2]
ypoints_top[8]=ypoints_top[3]
ypoints_top[7]=ypoints_top[4]
ypoints_top[6]=ypoints_top[5]
ypoints_bottom=[i for i in range(12)]
for i in range(12):
  ypoints_bottom[i]=map_3d_height-ypoints_top[i]
#Text configuration
font_size = 18

#Define 3d grid
#debug
map_3d_width=100
map_3d_x=220
#eod
GRID_SIZE = 6
ADJX = map_3d_width/10
LINEX=[[z for z in range(GRID_SIZE)] for x in range(GRID_SIZE)]
LINEY=[z for z in range(GRID_SIZE)]
print ( "Doing this" )
for z in range(GRID_SIZE):
  ML = z * ADJX
  MR = map_3d_width - ML
  GAP = MR - ML
  LINEY[z]=map_3d_height - z * 20
  print ( "ML:", ML, " MR:", MR, " GAP:", GAP )
  for x in range(GRID_SIZE):
    LINEX[z][x] = map_3d_x + ML + GAP * ( x - 2 )
    print ( "Z:", z, " X:", x, " LINEX: ", LINEX[z][x] )
  pygame.draw.line(screen,yellow,[LINEX[z][0],LINEY[z]],[LINEX[z][GRID_SIZE - 1],LINEY[z]],1)



def main():
  clock = pygame.time.Clock()
  create_character()
  clear_screen()
  draw_border(map_3d_x,map_3d_y,map_3d_width,map_3d_height,border_width)
  draw_border(map_placementx-1,map_placementy-1,gsize*(map_max_x)+2,gsize*(map_max_y)+2,border_width)
  #for point in range(12):
  #  pygame.draw.line(screen,yellow,[xpoints[point]+map_3d_x,ypoints_top[point]+map_3d_y],[xpoints[point]+map_3d_x,map_3d_y+map_3d_height-ypoints_top[point]],1)
  #  if (point < 11):
  #    pygame.draw.line(screen,yellow,[xpoints[point]+map_3d_x,ypoints_top[point]+map_3d_y],[xpoints[point+1]+map_3d_x,ypoints_top[point+1]+map_3d_y],1)
  #    pygame.draw.line(screen,yellow,[xpoints[point]+map_3d_x,ypoints_bottom[point]+map_3d_y],[xpoints[point+1]+map_3d_x,ypoints_bottom[point+1]+map_3d_y],1)
  print_dngn(currentx,currenty)
  write_status("The dungeon")
  getinput()

def print_wall():
  print( "Printing Wall")

def create_character():
  clear_screen()

def write_text(message,x,y):
  font = pygame.font.Font(None, font_size)
  text = font.render(message, 1, white)
  screen.blit(text, (x, y))
  pygame.display.flip()

def clear_screen():
  draw_border(0,0,screenmax_x,screenmax_y,border_width)
  
def clear_status():
  pygame.draw.rect(screen,background_color,[map_statusx,map_statusy,map_statuswidth,map_statussize])

def write_status(message):
  clear_status()
  write_text(message,map_statusx,map_statusy)

def draw_wall(tx,ty):
  pygame.draw.rect(screen,wall_outline,[tx,ty,gsize,gsize],1)
  pygame.draw.rect(screen,wall_fill,[tx+1,ty+1,gsize-2,gsize-2])

def clear_dngn():
  pygame.draw.rect(screen,background_color,[map_placementx,map_placementy,gsize*(map_max_x),gsize*(map_max_y)])

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
      if (y == int(map_hmax_y)) and (x == int(map_hmax_x)):
        if (direction == 0):
          pygame.draw.line(screen,royalblue,[int(mapx),int(mapy+gsize/2)-1],[int(mapx+gsize),int(mapy+gsize/2)-1],2)
          pygame.draw.line(screen,royalblue,[int(mapx),int(mapy+gsize/2)-1],[int(mapx+gsize/3),int(mapy)],2)
          pygame.draw.line(screen,royalblue,[int(mapx),int(mapy+gsize/2)-1],[int(mapx+gsize/3),int(mapy)+gsize],2)
        elif (direction == 1):
          pygame.draw.line(screen,royalblue,[int(mapx+gsize/2),int(mapy)-1],[int(mapx+gsize/2),int(mapy+gsize)-1],2)
          pygame.draw.line(screen,royalblue,[int(mapx+gsize/2),int(mapy)-1],[int(mapx),int(mapy+gsize/3)],2)
          pygame.draw.line(screen,royalblue,[int(mapx+gsize/2),int(mapy)-1],[int(mapx+gsize),int(mapy+gsize/3)],2)
        elif (direction == 2):
          pygame.draw.line(screen,royalblue,[int(mapx+gsize),int(mapy+gsize/2)-1],[int(mapx),int(mapy+gsize/2)-1],2)
          pygame.draw.line(screen,royalblue,[int(mapx+gsize),int(mapy+gsize/2)-1],[int(mapx+gsize-gsize/3),int(mapy)],2)
          pygame.draw.line(screen,royalblue,[int(mapx+gsize),int(mapy+gsize/2)-1],[int(mapx+gsize-gsize/3),int(mapy)+gsize],2)
        elif (direction == 3):
          pygame.draw.line(screen,royalblue,[int(mapx+gsize/2),int(mapy+gsize)],[int(mapx+gsize/2),int(mapy)-1],2)
          pygame.draw.line(screen,royalblue,[int(mapx+gsize/2),int(mapy+gsize)],[int(mapx),int(mapy+gsize/3)],2)
          pygame.draw.line(screen,royalblue,[int(mapx+gsize/2),int(mapy+gsize)],[int(mapx+gsize),int(mapy+gsize/3)],2)
  pygame.display.flip()

def getinput():
  while True:
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

def check_move(x,y):
  global currentx, currenty
  if (map[y][x] == " "):
    currentx = x
    currenty = y
    clear_dngn()
    clear_status()
    print_dngn(currentx,currenty)
    return 0
  else:
    write_status("BONK")
    return 1

def draw_border(x1,y1,x2,y2,w):
  pygame.draw.rect(screen,border_color,(x1-int(w/2),y1-int(w/2),x2,y2),w)

def turn_left():
  global direction
  direction=direction-1
  if direction < 0:
    direction=3
  clear_dngn()
  clear_status()
  print_dngn(currentx,currenty)

def turn_right():
  global direction
  direction=direction+1
  if direction > 3:
    direction=0
  clear_dngn()
  clear_status()
  print_dngn(currentx,currenty)

def go_forward():
  check_move(currentx+dirx[direction],currenty+diry[direction])

def go_backward():
  check_move(currentx-dirx[direction],currenty-diry[direction])

main()  
