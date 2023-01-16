from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import sys
sys.setrecursionlimit(1000000)
window_size = 500
point_size = 8

def rectangle(x1,y1,x2,y2,x3,y3,x4,y4):
    
    glBegin(GL_POLYGON)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)
    glVertex2f(x4,y4)
    glEnd()
    glFlush()
def plotRect():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0)
    rectangle(0,0,250,0,250,250,0,250)  
    glColor3f(0,1,0)
    rectangle(0,250,250,250,250,500,0,500)
    glColor3f(0,0,1)
    rectangle(250,0,500,0,500,250,250,250)
    glColor3f(0.5,0,1)
    rectangle(250,250,500,250,500,500,250,500) 
def getPixel(x,y):
    color = glReadPixels(x,window_size-y,1,1,GL_RGB,GL_FLOAT) 
    return color[0][0]  
def setPixel(x,y,color):
    glColor3f(*color) 
    glPointSize(point_size)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()
    glFlush()
def floodFill(x,y,oldColor,newColor):
    color = getPixel(x,y)
    if all(color == oldColor):
        setPixel(x,y,newColor)
        floodFill(x+point_size,y,oldColor,newColor)
        floodFill(x-point_size,y,oldColor,newColor)
        floodFill(x,y+point_size,oldColor,newColor)
        floodFill(x,y-point_size,oldColor,newColor)
        
def mouseClick(state,button,x,y):
    if(button == GLUT_LEFT_BUTTON and state == GLUT_DOWN):
        floodFill(x,y,getPixel(x,y),[0,.5,1])
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