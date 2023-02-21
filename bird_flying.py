from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import time
ref_x = 0
ref_y = 0
initPosition = 1

def clearScreen():
    gluOrtho2D(-100, 100, -100, 100)
    glClearColor(0.0, 0.0, 0.0, 1.0)
def bird():
    global ref_x,ref_y
    glClear(GL_COLOR_BUFFER_BIT)
    glColor(0,.8,.2)
    glBegin(GL_TRIANGLE_FAN)#body
    for i in range(0,360,1):
        theta = math.pi * (i/180)
        x = ref_x + 20*math.cos(theta)
        y =  ref_y +10 * math.sin(theta)
        glVertex2f(x,y)
    glEnd()
    glColor3f(0,0,0)
    glPointSize(5)
    glBegin(GL_POINTS)#eyes
    glVertex2f(ref_x+15,ref_y+2)
    glEnd()
    wings()#wings
    beak()#beak
    tail()
    glFlush()
def beak():
    global ref
    glColor3f(1,.5,0)
    glBegin(GL_TRIANGLES)
    glVertex2f(ref_x+19,ref_y+2)
    glVertex2f(ref_x+19,ref_y-2)
    glVertex2f(ref_x+23,ref_y)  
    glEnd() 
def tail():
    global ref_x,ref_y
    glColor3f(0,.8,.2)
    glBegin(GL_TRIANGLES)
    glVertex2f(ref_x-25,ref_y+10)
    glVertex2f(ref_x-25,ref_y-4)
    glVertex2f(ref_x-16,ref_y)  
    glEnd()     
def wings():
    global ref_x,initPosition,ref_y
    glColor3f(0,0.5,1)
    glBegin(GL_TRIANGLES)
    glVertex2f(ref_x-5,ref_y)
    glVertex2f(ref_x+5,ref_y)
    if initPosition%2 == 0:
        glVertex2f(ref_x,ref_y+15)   
    else:
        glVertex2f(ref_x,ref_y-15) 
    glEnd()
           
def move(key,x,y):
    global ref_x,initPosition,ref_y
    key = key.decode()
    initPosition+=1
    if(key == "w"):
        ref_y +=2
        bird()
    if(key == "s"):
        ref_y -=2  
        bird() 
    if(key == "a"):
        ref_x -=2
        bird()
    if(key == "d"):
        ref_x+=2  
        bird()           
def main():
    
    glutInit()
    glutInitWindowSize(1000, 1000)
    glutCreateWindow("Bird")
    glutInitWindowPosition(1000, 1000)
    glutDisplayFunc(bird)
    glutKeyboardFunc(move)

    clearScreen()
    glutMainLoop()


main()
