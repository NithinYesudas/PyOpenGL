from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math


def clearScreen():
    gluOrtho2D(-10, 10, -10, 10)
    glClearColor(0.0, 0.0, 0.0, 1.0)


def triangle(x1, y1, x2, y2, x3, y3):

    glBegin(GL_TRIANGLES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()
    glFlush()


def translation(x1, y1, x2, y2, x3, y3, tx, ty):
    plotGraph()
    glColor3f(1.0, 0.0, 0.0)

    triangle(x1, y1, x2, y2, x3, y3)

    x1 += tx
    x2 += tx
    x3 += tx
    y1 = y1+ty
    y2 = y2+ty
    y3 = y3+ty
    glColor3f(0, 1, 0)
    triangle(x1, y1, x2, y2, x3, y3)
def plotGraph():#to plot gridlines on the screen

    
    for i in range(-10,10,2):
        if i == 0:
            glPointSize(7)
            glColor3f(1,0,0) 
        else:
            
            glColor3f(1,1,1)
            glPointSize(5)
        glBegin(GL_LINES)
        glVertex2f(-10,i)
        glVertex2f(10,i)
        glEnd()
        glBegin(GL_LINES)
        glVertex2f(i,-10)
        glVertex2f(i,10)
        glEnd()
        glFlush()

def anticlock_rotation(x1, y1, x2, y2, x3, y3, radian):
    plotGraph()
    glColor3f(1.0, 0.0, 0.0)

    triangle(x1, y1, x2, y2, x3, y3)
    x11 = x1
    x22 = x2
    x33 = x3  # to preserve the original value of x components for using in y equation

    x1 = x1*math.cos(radian) - y1*math.sin(radian)
    x2 = x2*math.cos(radian) - y2*math.sin(radian)
    x3 = x3*math.cos(radian) - y3*math.sin(radian)
    y1 = x11*math.sin(radian) + y1*math.cos(radian)
    y2 = x22*math.sin(radian) + y2*math.cos(radian)
    y3 = x33*math.sin(radian) + y3 * math.cos(radian)
    glColor3f(0, 1, 0)
    triangle(x1, y1, x2, y2, x3, y3)


def scaling(x1, y1, x2, y2, x3, y3, scalingFactor):
    plotGraph()
    glColor3f(1, 0, 0)
    triangle(x1, y1, x2, y2, x3, y3)
    x1 *= scalingFactor
    x2 *= scalingFactor
    x3 *= scalingFactor
    y3 *= scalingFactor
    y2 *= scalingFactor
    y1 *= scalingFactor
    glColor3f(0, 1, 0)
    triangle(x1, y1, x2, y2, x3, y3)


def shear(x1, y1, x2, y2, x3, y3, shearAxis, shearDistance):
    plotGraph()
    glColor3f(1, 0, 0)
    triangle(x1, y1, x2, y2, x3, y3)
    if (shearAxis == "x"):
        x2 = x2+ y2* shearDistance
    else:
        y2 = y2+ shearDistance*x2
    glColor3f(0, 1, 0)
    triangle(x1, y1, x2, y2, x3, y3)

def reflection(x1, y1, x2, y2, x3, y3,reflectAxis):
    plotGraph()
    glColor3f(1,0,0)
    triangle(x1, y1, x2, y2, x3, y3)
    if(reflectAxis == 'y'):
        x1 = -x1
        x2 = -x2
        x3 = -x3
    else:
        y1 = -y1
        y2 = -y2
        y3 = -y3    
    glColor3f(0, 1, 0)
    triangle(x1, y1, x2, y2, x3, y3)    
def main():
    global theta, radian
    pi = 3.1415

    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    x3 = float(input("Enter x3: "))
    y3 = float(input("Enter y3: "))
    choice = int(
        input("Enter 1 for translation and 2 for rotation, 3 for scaling, 4 for shearing and 5 for reflection: "))
    if (choice == 1):
        tx = float(input("Enter tx: "))
        ty = float(input("Enter ty: "))
    elif (choice == 2):
        theta = float(input("Enter x where pi/x = theta: "))
    elif choice == 3:
        scaleFactor = float(input("Enter scaling factor: "))
    elif choice == 4:
        shearAxis = input("Enter shear axis: ")
        shearDistance = float(input("Enter shear distance: "))
    else:
        rotateAxis = input("Enter rotate Axis: ")
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("2DTransformations")
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(200, 200)
    
    if (choice == 1):
        glutDisplayFunc(lambda: translation(x1, y1, x2, y2, x3, y3, tx, ty))
    elif choice == 2:

        radian = pi/theta
        glutDisplayFunc(lambda: anticlock_rotation(
            x1, y1, x2, y2, x3, y3, radian))
    elif choice == 3:
        glutDisplayFunc(lambda: scaling(x1, y1, x2, y2, x3, y3, scaleFactor))
    elif choice == 4:
        glutDisplayFunc(lambda: shear(x1, y1, x2, y2, x3,
                        y3, shearAxis, shearDistance))
    else:
        glutDisplayFunc(lambda: reflection(x1, y1, x2, y2, x3, y3,rotateAxis))
    clearScreen()
    glutMainLoop()


main()
