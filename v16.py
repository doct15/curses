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

#The in-game map number of squares shown (3 or 5?)
map_max_x=5
map_hmax_x=int(map_max_x/2)
map_max_y=map_max_x
map_hmax_y=int(map_max_y/2)

#Map location on the screen x,y
map_placementx=screenmax_x-gsize*(map_max_x+1)-1
map_placementy=gsize+1
#print (map_placementx)
#print (map_placementy)
#print (map_placementx-1,map_placementy-1,gsize*(map_max_x)+2,gsize*(map_max_y))


#The users current location in the dungeon
currentx = 6
currenty = 4

#Colors
light_grey = (64,64,64)
black = (0,0,0)
yellow = (255,255,0)
white = (255,255,255)
green = (0,255,0)
blue = (0,0,255)

#Color assignments
wall_fill = light_grey
wall_outline = yellow
background_color = black
border_color = blue
border_width = 2
dude_color = green

#Key bindings
go_left = pygame.K_a
go_right = pygame.K_d
go_up = pygame.K_w
go_down = pygame.K_s
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

#More Global stuff
pygame.init()
size = (screenmax_x,screenmax_y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("dngn")

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
#print(map_3d_x,map_3d_y,map_3d_width,map_3d_height)

#Define 3d hallway points
xpoints=[i for i in range(12)]
xpoints[0]=1
#xpoints[0]=int(map_3d_width/26.242)
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
#ypoints_top[0]=int(map_3d_height/18.4)
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
  #print(i,i+6,11-i,ypoints_bottom[i+6],ypoints_top[11-i])
#Text configuration
font_size = 18

def main():
  clock = pygame.time.Clock()
  #print_grid()
  # Draw screen border
  # Draw map border
  create_character()
  clear_screen()
  draw_border(map_3d_x,map_3d_y,map_3d_width,map_3d_height,border_width)
  draw_border(map_placementx-1,map_placementy-1,gsize*(map_max_x)+2,gsize*(map_max_y)+2,border_width)
  #pygame.draw.circle(screen,yellow,[map_3d_x,map_3d_y],3,0)
  #for xpoint in range(len(xpoints)):
  for point in range(12):
    #pygame.draw.circle(screen,yellow,[xpoints[point]+map_3d_x,ypoints_top[point]+map_3d_y],3,0)
    #pygame.draw.circle(screen,yellow,[xpoints[point]+map_3d_x,map_3d_y+map_3d_height-ypoints_top[point]],3,0)
    pygame.draw.line(screen,yellow,[xpoints[point]+map_3d_x,ypoints_top[point]+map_3d_y],[xpoints[point]+map_3d_x,map_3d_y+map_3d_height-ypoints_top[point]],1)
    if point < 11:
      pygame.draw.line(screen,yellow,[xpoints[point]+map_3d_x,ypoints_top[point]+map_3d_y],[xpoints[point+1]+map_3d_x,ypoints_top[point+1]+map_3d_y],1)
      pygame.draw.line(screen,yellow,[xpoints[point]+map_3d_x,ypoints_bottom[point]+map_3d_y],[xpoints[point+1]+map_3d_x,ypoints_bottom[point+1]+map_3d_y],1)
      #print(xpoints[point]+map_3d_x,ypoints_bottom[point]+map_3d_y,xpoints[point+1]+map_3d_x,ypoints_bottom[point+1]+map_3d_y)
  print_dngn(currentx,currenty)
  write_status("The dungeon")
  getinput()

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
        pygame.draw.circle(screen,dude_color,[int(mapx+gsize/2),int(mapy+gsize/2)], int(gsize/3), int(gsize/5))
  pygame.display.flip()

def getinput():
  while True:
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == quit:
          quit()
        elif (event.key == go_left) or (event.key == pygame.K_LEFT):
          #myscreen.addstr(msg_locy,msg_locx,"Left")
          move_left()
        elif (event.key == go_up) or (event.key == pygame.K_UP):
          #myscreen.addstr(msg_locy,msg_locx,"Up")
          move_up()
        elif (event.key == go_right) or (event.key == pygame.K_RIGHT):
          #myscreen.addstr(msg_locy,msg_locx,"Right")
          move_right()
        elif (event.key == go_down) or (event.key == pygame.K_DOWN):
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
    clear_status()
    print_dngn(currentx,currenty)
    return 0
  else:
    write_status("BONK")
    return 1

def draw_border(x1,y1,x2,y2,w):
  pygame.draw.rect(screen,border_color,(x1-int(w/2),y1-int(w/2),x2,y2),w)

def move_left():
  check_move(currentx-1,currenty)

def move_right():
  check_move(currentx+1,currenty)

def move_up():
  check_move(currentx,currenty-1)

def move_down():
  check_move(currentx,currenty+1)

main()  
