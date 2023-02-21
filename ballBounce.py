from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import time
ref_x = -80
ref_y = 0

def clearScreen():
    gluOrtho2D(-100, 100, -100, 100)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    
def drawLine():
    glColor(1,0,0)
    glPointSize(10)
    glBegin(GL_LINES)   
    glVertex2f(-100,-40)
    glVertex2f(100,-40)
    glEnd()
    glFlush()
def bounce():
    global ref_x,ref_y
    
    for i in range(0,900,1):
        theta = math.pi*(i/180)
        ref_y = 30*math.sin(theta)
        ref_x +=.2
        time.sleep(0.02)
        ball()   
def ball():
    global ref_x,ref_y
    
    glClear(GL_COLOR_BUFFER_BIT)
    drawLine()
    glColor(1,0,0)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0,360,1):
        theta = math.pi * (i/180)
        x = ref_x + 10*math.cos(theta)
        y = ref_y + 10*math.sin(theta)
        glVertex2f(x,y)
    glEnd()
    glPointSize(4)
    glColor(1,1,1)
    glBegin(GL_POINTS)
    glVertex2f(ref_x-5,ref_y+5)
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
