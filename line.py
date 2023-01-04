import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
<<<<<<< HEAD
import sys

WINDOW_SIZE = 500

def clearScreen():
    gluOrtho2D(-10,10,-10,10)
    glClearColor(0,0,0,0)

def line(x1,y1,x2,y2):
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0, 0.0, 0.0)
	glPointSize(5)
	glBegin(GL_LINES)
	glVertex2f(x1,y1)
	glVertex2f(x2,y2)
	glEnd()
	glFlush()
 
def main():
	glutInit()
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
	glutInitWindowPosition(50,50)
	glutCreateWindow("Line")
	glutDisplayFunc(lambda: line(1,1,8,8))
	clearScreen()
	glutMainLoop()
 
 
main()
=======
def clearScreen():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1.0, 1.0,-1.0,1.0)
def plot_line():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,0.0)
    glPointSize(5.0)
    glBegin(GL_LINES)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0,-1.0)
    glVertex2f(1.0,0.0)
    glEnd()
    glFlush()
glutInit()
glutInitDisplayMode(GLUT_RGB)
glutCreateWindow("Lines")
glutInitWindowSize(500, 500)
glutInitWindowPosition(50, 50)
glutDisplayFunc(plot_line)
clearScreen()
glutMainLoop()
>>>>>>> fdc2323c53c2a214992a0504f152e878090ed9c7
