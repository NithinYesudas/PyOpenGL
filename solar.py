from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import time


def clearScreen():
    gluOrtho2D(-100, 100, -100, 100)
    glClearColor(0.0, 0.0, 0.0, 1.0)


def planet(rx, ry):
   # glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_TRIANGLE_FAN)  # for sun
    for i in range(0, 360, 1):
        theta = math.pi * (i/180)
        x = rx+7*math.cos(theta)
        y = ry + 7*math.sin(theta)

        glVertex2f(x, y)
    glEnd()


def sun():
    glColor3f(1, .3, 0)
    glBegin(GL_TRIANGLE_FAN)  # for sun
    for i in range(0, 360, 1):
        theta = math.pi * (i/180)
        x = 0+10*math.cos(theta)
        y = 0 + 10*math.sin(theta)

        glVertex2f(x, y)
    glEnd()

def path(r):
        glColor3f(1,1,1)
        glBegin(GL_LINE_LOOP)
        for i in range(0,360,1):
            theta = math.pi*(i/180)
            x = 1.8*r*math.cos(theta)
            y = r * math.sin(theta)
            glVertex2f(x,y)
        glEnd()
        
    
def solar():

    for i in range(0, 720, 1):
        glClear(GL_COLOR_BUFFER_BIT)

        sun()
        path(20)
       
            
        time.sleep(.05)
        glColor3f(0, 1, 0)
        theta = math.pi*(i/180)
        x = 36*math.cos(theta)
        y = 20 * math.sin(theta)

        planet(x, y)
        glColor3f(0, 0, 1)
        path(40)
        x = 72*math.cos(theta)
        y = 40 * math.sin(theta)
        planet(x, y)
        glFlush()


def main():
    global ref_x
    glutInit()
    glutInitWindowSize(1000, 1000)
    glutCreateWindow("Car")
    glutInitWindowPosition(1000, 1000)
    glutDisplayFunc(solar)

    clearScreen()
    glutMainLoop()


main()
