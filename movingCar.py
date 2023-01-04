from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

ref_x = 0
ref_y = 0


def inc(key,x,y):
    global ref_x
    key = key.decode()
    if (key == 'w'):
        ref_x += 1
        drawCar()
    if (key == "s"):
        ref_x-=1
        drawCar()
    if (key == "q"):
        glutLeaveMainLoop()
def drawCar():
    global ref_x
    global ref_y

    glColor3f(1, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POLYGON)
    glVertex2f(ref_x-20, ref_y-10)
    glVertex2f(ref_x-20, ref_y+10)
    glVertex2f(ref_x+20, ref_y+10)
    glVertex2f(ref_x+20, ref_y-10)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(ref_x-10, ref_y-10)
    glVertex2f(ref_x-5, ref_y+20)
    glVertex2f(ref_x+5, ref_y+20)
    glVertex2f(ref_x+10, ref_y-10)
    glEnd()
    for i in range(0,360,1):
        glBegin(GL_POINTS)
        glVertex2f()

    glFlush()


def clearScreen():
    gluOrtho2D(-100, 100, -100, 100)
    glClearColor(0.0, 0.0, 0.0, 1.0)


def main():
    global ref_x
    glutInit()
    glutInitWindowSize(1000, 1000)
    glutCreateWindow("Car")
    glutInitWindowPosition(1000, 1000)

    glutDisplayFunc(drawCar)
    glutKeyboardFunc(inc)

    clearScreen()
    glutMainLoop()


main()
