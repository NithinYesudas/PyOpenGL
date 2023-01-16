from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
window_size = 500


def clearScreen():
    gluOrtho2D(-window_size, window_size, window_size, -window_size)


def midpointCircle():
    xc = 0
    yc = 0
    radius = 100
    p = 1-radius
    x = 0
    y = radius
    while x < y:
        x += 1
        if p < 0:
            p = p+2*x + 1
        else:
            y -= 1
            p = p+2*x + 1 - 2*y
        plotSymmetricCircle(x, y)


def plotSymmetricCircle(x, y):

    plotPoints(x, y)
    plotPoints(-x, -y)
    plotPoints(-x, y)
    plotPoints(x, -y)
    plotPoints(y, x)
    plotPoints(-y, x)
    plotPoints(y, -x)
    plotPoints(-y, -x)


def plotPoints(x, y):

    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()


def main():
    glutInit()
    glutInitWindowSize(window_size, window_size)
    glutCreateWindow("Circle")
    glutDisplayFunc(midpointCircle)

    clearScreen()
    glutMainLoop()


main()
