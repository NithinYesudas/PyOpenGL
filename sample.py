from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def plot_points():
    x1 = float(input("enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("enter x2: "))
    y2 = float(input("Enter y2: "))
    x3 = float(input("enter x3: "))
    y3 = float(input("Enter y3: "))
    
    glColor3f(0, .5, .5)
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(10)
    glBegin(GL_TRIANGLES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()
    glFlush()


def main():

    glutInit()
    glutCreateWindow("points")
    glutInitWindowSize(600, 600)
    glutDisplayFunc(plot_points)
    #gluOrtho2D(-600,600,-600,600)
    glutMainLoop()


main()
