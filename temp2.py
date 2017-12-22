from graphics import *

gsize=20
gradius=int(gsize/2)
map_placementx=20
map_placementy=20


def main():
    win = GraphWin('Draw a Triangle', 350, 350)
    #win.yUp() # right side up coordinates
    win.setBackground('yellow')
    #message = Text(Point(win.getWidth()/2, 30), 'Click on three points')
    #message.setTextColor('red')
    #message.setStyle('italic')
    #message.setSize(20)
    #message.draw(win)

    draw_wall(win,map_placementx,map_placementy)
    draw_wall(win,map_placementx+gsize,map_placementy)
    draw_wall(win,map_placementx,map_placementy+gsize)

    # Get and draw three vertices of triangle
    #p1 = win.getMouse()
    #p1.draw(win)
    #p2 = win.getMouse()
    #p2.draw(win)
    #p3 = win.getMouse()
    #p3.draw(win)
    #vertices = [p1, p2, p3]

    # Use Polygon object to draw the triangle
    #triangle = Polygon(vertices)
    #triangle.setFill('gray')
    #triangle.setOutline('cyan')
    #triangle.setWidth(4)  # width of boundary line
    #triangle.draw(win)



    message = Text(Point(win.getWidth()/2, 300), 'Click on three points')
    message.setTextColor('red')
    message.setStyle('italic')
    message.setSize(20)
    message.draw(win)
    message.setText('Click anywhere to quit') # change text message
    win.getMouse()
    win.close() 


def draw_wall(win,x,y):
    #global win
    wall1 = Rectangle(Point(x,y),Point(x+gsize,y+gsize))
    wall1.setFill(color_rgb(64,64,64))
    wall1.draw(win)

main()
