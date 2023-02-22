from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import time
ref_x = -100
ref_y = 0


def clearScreen():
    gluOrtho2D(-100, 100, -100, 100)
    glClearColor(0.0, 0.0, 0.0, 1.0)


def drawBoundaries():
    glColor(1, 0, 0)
    glPointSize(10)
    glBegin(GL_LINES)
    glVertex2f(-100, -40)
    glVertex2f(100, -40)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(-100, 40)
    glVertex2f(100, 40)
    glEnd()
    glFlush()

    
def bounce():
    global ref_x, ref_y
    amp = 30
    for i in range(-89, 900, 1):
        theta = math.pi*(i/180)
        ref_y = amp*math.sin(theta)
        if math.sin(theta) == -1:
            
            amp = amp - 10

        if math.sin(theta) < 0:
            ref_y = 30*math.sin(theta)
        ref_x += .2
        time.sleep(0.008)
        x =  7*math.cos(theta)
        y = 7*math.sin(theta)
        ball(x,y)


def ball(x1,y1):
    global ref_x, ref_y

    glClear(GL_COLOR_BUFFER_BIT)
    drawBoundaries()
    glColor(1, 0, 0)
    glBegin(GL_TRIANGLE_FAN)
   
    for i in range(0, 360, 1):
         
        theta = math.pi * (i/180)
        x = ref_x + 10*math.cos(theta)
        y = ref_y + 10*math.sin(theta)
        glVertex2f(x, y)
    glEnd()
    glPointSize(4)
    
    glColor(1, 1, 1)
    glBegin(GL_POINTS)
    
    glVertex2f(ref_x-x1, ref_y+y1)
    glEnd()

    glFlush()


def main():

    glutInit()
    glutInitWindowSize(750, 750)
    glutCreateWindow("ball bounce")
    glutInitWindowPosition(1000, 1000)
    glutDisplayFunc(bounce)
    
    clearScreen()
    glutMainLoop()


main()
