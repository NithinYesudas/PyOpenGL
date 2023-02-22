from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import time
x1 = -40
y1 = 40


def clearScreen():
    gluOrtho2D(-100, 100, -100, 100)
    glClearColor(0.0, 0.0, 0.0, 1.0)


def bar(flag):
    global x1, y1

    for i in range(330, 390, 1):

        x1 = 40*math.cos(math.radians(i))
        y1 = 40*math.sin(math.radians(i))

        if (not flag):
            y1 = -y1

        glLineWidth(6)
        glColor3f(0, .8, .2)
        glBegin(GL_LINES)

        glVertex2f(-x1, -y1)
        glVertex2f(x1, y1)

        glEnd()

        glFlush()
        body()
        time.sleep(.05)


def animate():

    for i in range(1, 10, 1):
        if (i % 2 == 0):
            bar(False)

        else:
            bar(True)


def body():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor(.8, 0, .2)
    glBegin(GL_TRIANGLES)
    glVertex2f(-20, -25)
    glVertex2f(20, -25)
    glVertex2f(0, 0)
    glEnd()


def main():
    glutInit()
    glutInitWindowSize(750, 750)
    glutCreateWindow("See Saw")
    glutInitWindowPosition(1000, 1000)
    glutDisplayFunc(animate)

    clearScreen()
    glutMainLoop()


main()
