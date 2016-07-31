#!/usr/bin/python3.4
# -*- coding: latin-1 -*-

import sys
import curses

#print ('Number of arguments:', len(sys.argv), 'arguments.')
#print ('Argument List:', str(sys.argv))

text = [
" ",
"/",
"-",
"\\",
"|",
",",
"."
]

ascii = [
" ",
"┌",
"─",
"┐",
"│",
"└",
"┘"
]

myscreen = curses.initscr()
#maxy, maxx = myscreen.getmaxyx()
maxy = 24
maxx = 80
quit = ord("q")

myscreen.clear()
curses.resizeterm(maxy, maxx)
myscreen.refresh()

#print (text[0])
#print (ascii[0])
myscreen.addstr(text[0])
myscreen.addstr(ascii[0])

number_conversions=len(text)
#print ("text length",number_conversions)

file = sys.argv[1]

#print ("Opening",file)

map_ascii=[]
map_array=0
with open(file) as map_file:
  for line in map_file:
    map_ascii.extend("x")
    map_ascii[map_array]=""
    for char in list(line):
      for conversion in range(0,number_conversions-1):

        #print (conversion,"'",char,"'",text[conversion],ascii[conversion])

        if ( char == text[conversion]):
          #print (conversion,char)

          map_ascii[map_array] += ascii[conversion]

          break

    myscreen.addstr(map_ascii[map_array])
    map_array+=1
      

#for line in map_ascii:
  #print (line)

write_file=file+".ascii"
file_out=open(write_file,"w")
file_out.writelines(map_ascii)
file_out.close()


print ("end")
print (map_ascii)

c = myscreen.getch()

while True:
  # get keyboard input, returns -1 if none available
  c = myscreen.getch()
  if c != -1:
    #myscreen.move(0, 0)
    if (c == quit):
      #myscreen.addstr('Quit')
      break
      #myscreen.refresh()
curses.endwin()
