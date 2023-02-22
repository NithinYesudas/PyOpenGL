
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import time


def peacockBody():
    legs(2, -12)
    legs(-2, -12)
    glColor3f(0, 0, 1)
    glBegin(GL_POLYGON)
    glVertex2f(0, 20)
    glVertex2f(-10, -5)
    glVertex2f(0, -15)
    glVertex2f(10, -5)
    glEnd()

    glColor3f(1, 1, 1)
    eyes(-3, 2)
    eyes(3, 2)
    glColor3f(0, 0, 0)
    eyes(-3, 1)
    eyes(3, 1)
    beak()


def beak():
    glColor3f(.8, .3, 0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-2, 8)
    glVertex2f(2, 8)
    glVertex2f(0, 0)
    glEnd()


def legs(x, y):
    glColor3f(.8, .3, 0)
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2f(x, y)
    glVertex2f(x, y-5)
    glEnd()


def eyes(x1, radius):
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0, 360, 1):
        theta = math.radians(i)
        x = x1+radius*math.cos(theta)
        y = 12+radius*math.sin(theta)
        glVertex2f(x, y)

    glEnd()


def subWing(x, y):
    glColor3f(0, 1, 0)
    glBegin(GL_LINES)
    glVertex2f(0, -13)
    glVertex2f(x, y)
    glEnd()


def wings():

    for i in range(90, 180, 1):
        theta = math.radians(i)
        x = 40*math.cos(theta)
        y = -15+40*math.sin(theta)
        subWing(x, y)
        subWing(-x,y)
        peacockBody()
        glFlush()
        time.sleep(0.05)


def clearScreen():
    gluOrtho2D(-100, 100, -100, 100)
    glClearColor(0.0, 0.0, 0.0, 1.0)


def main():
    glutInit()
    glutInitWindowSize(750, 750)
    glutCreateWindow("Peacock")
    glutInitWindowPosition(1000, 1000)
    glutDisplayFunc(wings)

    clearScreen()
    glutMainLoop()


main()
