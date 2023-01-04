from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
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