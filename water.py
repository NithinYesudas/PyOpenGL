from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import time
y1 = -65
start = 265
end = 275

def clearScreen():
    gluOrtho2D(-100, 100, -100, 100)
    glClearColor(0.0, 0.0, 0.0, 1.0)
def line(x1,y1,x2,y2):
    
    glLineWidth(4)
    glBegin(GL_LINES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glEnd()
   

def pipe(start):
    balls()
    glColor3f(.8,0.3,0)
    for i in range(41,135,1):
        theta = math.radians(i)
        x1 = 30*math.cos(theta)
        y1 = 20*math.sin(theta)
        x2 = 40*math.cos(theta)
        y2 = 30*math.sin(theta)
        line(x1,y1,x2,y2)
    glBegin(GL_POLYGON)
    glVertex2f(10,40)
    glVertex2f(10,-40)
    glVertex2f(30,-40)
    glVertex2f(30,40)  
    glEnd()
    glColor3f(.8,0,0)
    for i in range(start,165,1):
        theta = math.radians(i)
        x1 = 27*math.cos(theta)
        y1 = 17*math.sin(theta)
        x2 = 42*math.cos(theta)
        y2 = 32*math.sin(theta)
        line(x1,y1,x2,y2)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0,360,1):
        theta = math.radians(i)
        x = -33.75 + 7.8*math.cos(theta)
        y = 6+6*math.sin(theta)
        glVertex2f(x,y)
    glEnd()  
    glColor3f(0,0,0)
    glLineWidth(5) 
    glBegin(GL_LINES)
    glVertex2f(-37,.5)
    glVertex2f(-36,2)
    glEnd() 
    
    
    

def balls():
    
    glColor3f(.5,0,0)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0,360,1):
        theta = math.radians(i)
        x = 6+9*math.cos(theta)
        y = 9+9*math.sin(theta)
        glVertex2f(x,y)
    glEnd() 
    glColor3f(.8,0,0)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0,360,1):
        theta = math.radians(i)
        x = 6+10*math.cos(theta)
        y = 14+10*math.sin(theta)
        glVertex2f(x,y)
    glEnd() 
def water(y):
    
    glLineWidth(5)
    glColor3f(.8,.8,.8)
    glBegin(GL_LINES)
    glVertex2f(-37,y)
    glVertex2f(-37,y+3)
    glEnd()
def moveWater():
    global y1,start,end
    for i in range(0,-40,-1):
        glClear(GL_COLOR_BUFFER_BIT)
        water(i)
        water(i+4.5)
        water(i+9)
        water(i+12.5)
        
        pipe(135)    
        bowl()
        
        
        filling()
        y1 = y1+.12
        if(i%3==0):
            start= start -1
            end = end +1
       
        
        glutSwapBuffers()
        time.sleep(.01) 
def animate():
    for i in range(0,6,1): 
        moveWater()
def bowl():
    glColor3f(.8,.3,0)
    glPointSize(5)
    glBegin(GL_POINTS)
    for i in range(180,360,1):
        theta = math.radians(i)
        x = -35+30*math.cos(theta)
        y = -35+30*math.sin(theta)
        glVertex2f(x,y)
    glEnd()    
                
def filling():
    global y1, start,end
    glColor3f(1,1,1)
    for i in range(start, end,1):
        theta = math.radians(i)
        x = -35+29*math.cos(theta)
        y = -35+29*math.sin(theta)
        glBegin(GL_LINES)
        glVertex2f(-35,y1)
        glVertex2f(x,y)
        glEnd()         
def main():
    global ref_x
    glutInit()
    glutInitWindowSize(1000, 1000)
    glutCreateWindow("Car")
    glutInitWindowPosition(1000, 1000)
    glutDisplayFunc(animate)

    clearScreen()
    glutMainLoop()


main()
