from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import time


def clearScreen():
    gluOrtho2D(-100, 100, -100, 100)
    glClearColor(0.0, 0.0, 0.0, 1.0)
def pipe():
    glColor3f(1,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(50,45)
    glVertex2f(50,75)
    glVertex2f(90,75) 
    glVertex2f(90,45)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(50,65)
    glVertex2f(30,65)
    glVertex2f(30,35)
    glVertex2f(40,35)
    glVertex2f(30,55)
    glVertex2f(50,55)
    glEnd()
    
def waterdrops(y):
    glColor3f(0.1,.216,.7)
    glBegin(GL_TRIANGLES)
    glVertex2f(37,y)
    glVertex2f(33,y)
    glVertex2f(35,y-4)
    glEnd()
def water():
    
    for i in range(0,-15,-1):
        glClear(GL_COLOR_BUFFER_BIT)
        
        waterdrops(i + 40)
        waterdrops(i+35)
        waterdrops(i+31)
        waterdrops(i+24)
        waterdrops(i+22) 
        waterdrops(i + 18)
        waterdrops(i+15)
        waterdrops(i+12)
        waterdrops(i+8)
        waterdrops(i+4)
        waterdrops(i)
        waterdrops(i-4)
        waterdrops(i-8)
        pipe()
        glFlush()
        time.sleep(.05)
def animate():
    for i in range(0,5,1):
        water()  
            
def main():
    global ref_x
    glutInit()
    glutInitWindowSize(1000, 1000)
    glutCreateWindow("Car")
    glutInitWindowPosition(1000, 1000)
    glutDisplayFunc(animate)

    clearScreen()
    glutMainLoop()


main()
