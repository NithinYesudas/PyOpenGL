from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
ref_x = 0
ref_y = 0
initPosition = 1


def moveCar(key, x, y):
    global ref_x, initPosition
    key = key.decode()
    initPosition += 1

    if (key == 'w'):
        ref_x += 1
        drawCar()

    if (key == "s"):
        ref_x -= 1
        drawCar()
    if (key == "q"):
        glutLeaveMainLoop()


def drawCar():
    global ref_x
    global ref_y
    # cars low body
    glColor3f(1, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POLYGON)
    glVertex2f(ref_x-20, ref_y-10)
    glVertex2f(ref_x-20, ref_y+5)
    glVertex2f(ref_x+20, ref_y+5)
    glVertex2f(ref_x+20, ref_y-10)
    glEnd()
   # cars top body trapezium
    glBegin(GL_POLYGON)
    glVertex2f(ref_x-10, ref_y-10)
    glVertex2f(ref_x-5, ref_y+20)
    glVertex2f(ref_x+5, ref_y+20)
    glVertex2f(ref_x+10, ref_y-10)
    glEnd()
    # window
    glColor3f(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2f(ref_x-5, ref_y+5)
    glVertex2f(ref_x-3, ref_y+18)
    glVertex2f(ref_x+3, ref_y+18)
    glVertex2f(ref_x+5, ref_y+5)
    glEnd()
    drawWheels(+10)
    drawWheels(-10)

    glFlush()


def clearScreen():
    gluOrtho2D(-100, 100, -100, 100)
    glClearColor(0.0, 0.0, 0.0, 1.0)


def drawWheels(x):
    glColor3f(0, 1, 0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(ref_x+x, ref_y-10)
    for i in range(0, 361, 1):
        # changing the colors of each segment of wheel for each keypress
        if (initPosition % 2 == 0):
            if (i < 90 or (i > 180 and i < 270)):
                glColor3f(0, 1, 0)
            else:
                glColor3f(0, 0, 1)
        else:
            if (i < 90 or (i > 180 and i < 270)):
                glColor3f(0, 0, 1)
            else:
                glColor3f(0, 1, 0)
        glVertex2f(5*math.cos(math.pi*i/180.0)+ref_x+x,
                   5*math.sin(math.pi*i/180.0)+ref_y-10)

    glEnd()


def main():
    
    glutInit()
    glutInitWindowSize(1000, 1000)
    glutCreateWindow("Car")
    glutInitWindowPosition(1000, 1000)
    glutDisplayFunc(drawCar)
    glutKeyboardFunc(moveCar)
    clearScreen()
    glutMainLoop()

main()
