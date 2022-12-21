from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points(x, y):
    glPointSize(1) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    #draw_points(250, 250)
    #x=200
    #y=200
    #draw_line(250,250,250+x,250+y)
    unit=50
    number_1=[[-4,-2],[-4,2],[-1,2],[-1,-2],[-4,-2]]
    number_2=[[1,2],[4,2],[4,-2]]
    for a in range(len(number_1)):
        number_1[a]=[number_1[a][0]*unit+250,number_1[a][1]*unit+250]
    for a in range(len(number_2)):
        number_2[a]=[number_2[a][0]*unit+250,number_2[a][1]*unit+250]

    for a in range(len(number_1)-1):
        draw_line(number_1[a][0],number_1[a][1],number_1[a+1][0],number_1[a+1][1])
    for a in range(len(number_2)-1):
        draw_line(number_2[a][0],number_2[a][1],number_2[a+1][0],number_2[a+1][1])
    
    glutSwapBuffers()



def draw_line(x1,y1,x2,y2):
    delx=x2-x1
    dely=y2-y1
    modx=abs(delx)
    mody=abs(dely)
    coords=[]
    modg=1
    modz=modx
    if modx>mody:
        gradient = mody/modx
    else:
        gradient = modx/mody
        modg=-1
        modz=mody
    #print(gradient)
    coord2=0
    for coord1 in range(modz+1):
        coord2+=gradient
        if coord2>=int(coord2)+0.5:
            coords.append([coord1,int(coord2)+1])
        else:
            coords.append([coord1,int(coord2)])
    if modg==-1:
        for a in range(len(coords)):
            swap = coords[a][1]
            coords[a][1] = coords[a][0]
            coords[a][0] = swap
    if delx<0:
        for a in range(len(coords)):
            coords[a][0] = -coords[a][0]
    if dely<0:
        for a in range(len(coords)):
            coords[a][1] = -coords[a][1]
    for a in range(len(coords)):
        coords[a] = [coords[a][0]+x1,coords[a][1]+y1]
    #print(coords)
    for coord in coords:
        draw_points(coord[0],coord[1])
    


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"CSE 423 - Lab 2") #window name
glutDisplayFunc(showScreen)

glutMainLoop()