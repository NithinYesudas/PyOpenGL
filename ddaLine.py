from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

def clearScreen():
    gluOrtho2D(-100,100,-100,100)
    glClearColor(0,0,0,0)

def dda(x1,y1,x2,y2):
    
    m = (y2-y1)/(x2-x1)
    glPointSize(10)
    for i in range((y2-y1)):
        glBegin(GL_POINTS)
        glVertex2f(x1,y1)
        glEnd()
        glFlush()
        if(m<0):
            x1 += 1
            y1 += int(m)
        else:
            x1 += int(1/m)
            y1 += 1    
    
def main():
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y2: "))
    x2 = int(input("x2: "))
    y2 = int(input("x2: "))
    glutInit()
    glutInitWindowSize(500,500)
    glutCreateWindow("DDA Line") 
    glutInitWindowPosition(500,500)
    glutDisplayFunc(lambda: dda(x1,y1,x2,y2))
    clearScreen()
    glutMainLoop()
main()    