from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import sys
import numpy as np
sys.setrecursionlimit(1000000)
window_size = 500

def rectangle(x1,y1,x2,y2,x3,y3,x4,y4):
    glLineWidth(5)
    glBegin(GL_LINE_LOOP)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)
    glVertex2f(x4,y4)
    glEnd()
    glFlush()
def plotRect():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0)
    rectangle(10,10,220,10,220,220,10,220)  
    
   
def getPixel(x,y):
    color = glReadPixels(x,window_size-y,1,1,GL_RGB,GL_FLOAT,None) 
    return np.array([round(x, 1) for x in color[0][0]])  
def setPixel(x,y,color):
    glColor3f(*color) 
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()
    glFlush()
def boundaryFill(x,y,boundaryColor,newColor):
    color = getPixel(x,y)
    if  (not all(color == boundaryColor)) and not all(color == newColor):
        setPixel(x,y,newColor)
        boundaryFill(x+5,y,boundaryColor,newColor)
        boundaryFill(x,y+5,boundaryColor,newColor)
        boundaryFill(x-5,y,boundaryColor,newColor)
        boundaryFill(x,y-5,boundaryColor,newColor)
        
def mouseClick(state,button,x,y):
    if(button == GLUT_LEFT_BUTTON and state == GLUT_DOWN):
        boundaryFill(x,y,[1,0,0],[0,.5,1])
def clearScreen():
    gluOrtho2D(0,window_size,window_size,0)
    
def main():
    glutInit()
    glutInitWindowSize(window_size,window_size)
    glutCreateWindow("Flood Filling")
    glutDisplayFunc(plotRect)
    glutMouseFunc(mouseClick)
    clearScreen()
    glutMainLoop()
main()    