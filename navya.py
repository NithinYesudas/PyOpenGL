from OpenGL.GL import *
from OpenGL.GLU import*
from OpenGL.GLUT import*
import math
def clearScreen():
    glClearColor(0,0,0,0)
    gluOrtho2D(-100,100,-100,100)

def line():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,.5,0)
    glBegin(GL_LINES)
    glVertex2f(50,50)
    glVertex2f(-25,-25)
    glEnd()
    glFlush()
def circle():
    glClear(GL_COLOR_BUFFER_BIT)   
    glColor3f(1,0,0)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0,360,1):
        theta = math.pi *(i/180)
        x = 0+10*math.cos(theta)
        y = 0 +10*math.sin(theta)
        
        glVertex2f(x,y)
    glEnd()
    glFlush()    

def main():
    glutInit()
    glutInitWindowSize(500,500)
    glutCreateWindow("Navya")
    glutDisplayFunc(circle)
    clearScreen()
    glutMainLoop()
main()    