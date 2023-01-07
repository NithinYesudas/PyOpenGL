from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import time
ref_x = -15
ref_y = 0


def clearScreen():
    gluOrtho2D(-100, 100, -100, 100)
    glClearColor(0.0, 0.0, 0.0, 1.0)


def pendulum():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, .5, .7)
    glPointSize(10)
    glBegin(GL_LINES)
    glVertex2f(0, 50)
    glVertex2f(ref_x, ref_y)
    glEnd()
    glColor3f(0, 1, 0)
    circle(1, 0, 50)
    glColor3f(1, 0, 0)
    circle(4, ref_x, ref_y)
    glFlush()


def circle(radius, x, y):
    glColor3f(0, 1, 0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for i in range(0, 361, 1):
        glVertex2f(radius*math.cos(math.pi*i/180.0)+x,
                   radius*math.sin(math.pi*i/180.0)+y)

    glEnd()


def movePendulum(phase):
    pi = 3.1419
    global ref_x
    global ref_y
    for i in range(10):
        x = ref_x
        y = ref_y

        theta = i * (pi/180)
        if (phase == True):
            ref_x = x*math.cos(theta) - (y-50)*math.sin(theta)
            ref_y = x*math.sin(theta) + (y-50)*math.cos(theta) + 50
        else:
            ref_x = x*math.cos(theta) + (y-50)*math.sin(theta)
            ref_y = -x*math.sin(theta) + (y-50)*math.cos(theta) + 50
        pendulum()
        time.sleep(.08)
        if (i == 9):
            if (phase == True):
                phase = False
            else:
                phase = True
            movePendulum(phase)


def main():

    glutInit()
    glutInitWindowSize(1000, 1000)
    glutCreateWindow("Car")
    glutInitWindowPosition(1000, 1000)
    glutDisplayFunc(lambda: movePendulum(True))
    clearScreen()
    glutMainLoop()


main()
