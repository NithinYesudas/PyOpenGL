from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import time
def clearScreen():
    gluOrtho2D(-100, 100, -100, 100)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    
def manBody():

    glColor3f(.9,.1,0)
    glBegin(GL_POLYGON)
    glVertex2f(-2,6)
    glVertex2f(2,6)
    glVertex2f(2,-2)
    glVertex2f(-2,-2)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(7,-2)
    glVertex2f(7,-40)
    glVertex2f(-7,-40)
    glVertex2f(-7,-2)
    
    glEnd()
    glLineWidth(8)
    glBegin(GL_LINES)
    glVertex2f(-6,-40)
    glVertex2f(-6,-80)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(6,-40)
    glVertex2f(6,-80)
    glEnd()
    glColor(0,0.9,.2)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0,360,1):
        theta = math.radians(i)
        x =  5*math.cos(theta)
        y = 10 + 5*math.sin(theta)
        glVertex2f(x,y)   
    glEnd()
    
def hands(x,y):
    glColor3f(.9,.1,0)
    glBegin(GL_LINES)
    glVertex2f(7,-3)
    glVertex2f(x,y)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(-7,-3)
    glVertex2f(-x,y)
    glEnd()
def move(flag):
    for i in range(330,390):
        glClear(GL_COLOR_BUFFER_BIT)
        theta = math.radians(i)
        x=40*math.cos(theta)
        y = 40*math.sin(theta)
        if(not flag):
            y = -y
            
        manBody()
        hands(x,y)
        glFlush()
        time.sleep(0.01)
def animate():
    for i in range(1,10,1):
        if(i%2==0):
            move(False)
        else:
            move(True)                     
def main():
    glutInit()
    glutInitWindowSize(750, 750)
    glutCreateWindow("See Saw")
    glutInitWindowPosition(1000, 1000)
    glutDisplayFunc(animate)

    clearScreen()
    glutMainLoop()


main()
