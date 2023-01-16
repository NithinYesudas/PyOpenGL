from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

WINDOW_SIZE = 500


def clearScreen():
    gluOrtho2D(-100, 100, -100, 100)
    glClearColor(0, 0, 0, 0)

def plotPoints(x1,y1):
    glBegin(GL_POINTS)
    glVertex2f(x1, y1)
    glEnd()
    glFlush() 
def bresenhamLine(x1, y1, x2, y2):
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(10)
    dx = x2-x1
    dy = y2 - y1
    m = dy/dx
    if (m < 1):

        p = 2 * dy - dx
        for i in range(dy):
            if (p > 0):
                p = p + 2*dy - 2*dx
                x1 += 1

            else:
                p = p + 2 * dy
                x1 += 1
                y1 += 1
            plotPoints(x1,y1)   
    else:
        p = 2 * dx -dy
        for i in range(dx):
            if(p>0):
                p = p+2*dx - 2*dy
                y1+=1
            else:
                p = p+2*dx
                x1 +=1
                y1 += 1           
            plotPoints(x1,y1)    
   
   


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("Line")
    glutDisplayFunc(lambda: bresenhamLine(0, 0, 75, 75))
    clearScreen()
    glutMainLoop()


main()
