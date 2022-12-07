from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math



def clearScreen():
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
    glClearColor(0.0, 0.0, 0.0, 1.0)


def triangle():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()
    glFlush()


def translation():
    tx = float(input("Enter tx: "))
    ty = float(input("Enter ty: "))
    x1 = x1+tx
    x2 = x2+tx
    x3 = x3 + tx
    y1 = y1+ty
    y2 = y2+ty
    y3 = y3+ty


def anticlock_rotation():
    #
    x11 = x1
    x22 = x2
    x33 = x3  # to preserve the original value of x components for using in y equation
   
    x1 = x1*math.cos(radian) - y1*math.sin(radian)
    x2 = x2*math.cos(radian) - y2*math.sin(radian)
    x3 = x3*math.cos(radian) - y3*math.sin(radian)
    y1 = x11*math.sin(radian) + y1*math.cos(radian)
    y2 = x22*math.sin(radian) + y2*math.cos(radian)
    y3 = x33*math.sin(radian) + y3 * math.cos(radian)

def input():
    global x1,x2,x3,y1,y2,y3
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    x3 = float(input("Enter x3: "))
    y3 = float(input("Enter y3: "))
    
        
def main():
    global theta, radian
    pi = 3.1415
    input()
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("2DTransformations")
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(200, 200)
    glutDisplayFunc(triangle)
    choice = int(input("Enter 1 for translation and 2 for rotation: "))
    if(choice == 1):
        glutDisplayFunc(translation)
    else:
        theta = float(input("Enter x where pi/x = theta: "))
        radian = pi/theta
        glutDisplayFunc(anticlock_rotation)    
           
    clearScreen()
    glutMainLoop()

main()    