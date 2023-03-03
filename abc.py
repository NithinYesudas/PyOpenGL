from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time

WINDOW_SIZE = 500

def clearscreen():
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)
    glClearColor(1,1,1,1)

def drawline():
    glColor3f(1,0,1)
    glPointSize(10)
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(100,100)
    glEnd()
    glFlush()

def plotpoint(x,y):
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()


def symmetry(x,y,x_centre,y_centre):
    plotpoint(x+x_centre,y+y_centre)
    plotpoint(x+x_centre,-y+y_centre)
    plotpoint(-x+x_centre,y+y_centre)
    plotpoint(-x+x_centre,-y+y_centre)
    plotpoint(y+x_centre,x+y_centre)
    plotpoint(y+x_centre,-x+y_centre)
    plotpoint(-y+x_centre,x+y_centre)
    plotpoint(-y+x_centre,-x+y_centre)

def circle(r,x_centre,y_centre):
    x=0
    y=r
    p=1-r
    glClear(GL_COLOR_BUFFER_BIT)

    while(x<y):
        symmetry(x,y,x_centre,y_centre)
        x=x+1
        if(p<0):
            p=p+2*x+1

        else:
            p=p+2*x-2*y+1
            y=y-1

    glFlush()

def animate():
    while(True):
        for i in range(0,500,1):
            circle(10,0,i)
            time.sleep(.008) 
        for i in range(500,0,-1):
            circle(10,0,i)
            time.sleep(.008) 


def triangletest():
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0,1000,10):
        x=i
        y=0
        glVertex2f(x,y)
    glEnd()
    glFlush()

def main():
    glutInit()
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutCreateWindow("new window")
    glutInitWindowPosition(WINDOW_SIZE,WINDOW_SIZE)
    glutDisplayFunc(animate)

    clearscreen()
    glutMainLoop()

main()