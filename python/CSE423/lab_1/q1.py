from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def dda(x_1,y_1,x_2,y_2):
    coordinate_set=[]
    delta_x=x_2-x_1
    delta_y=y_2-y_1
    if delta_x==0:
        coordinate_set.append([x_1,y_1])
        for a in range(delta_y):
            coordinate_set.append([x_1,y_1+1+a])
    elif delta_y==0:
        coordinate_set.append([x_1,y_1])
        for a in range(delta_x):
            coordinate_set.append([x_1+1+a,y_1])
    else:
        gradient=delta_y/delta_x
        #print(gradient,delta_x,delta_y)
        if gradient>1 or gradient<-1:
            gradient=1/gradient
            x_curr=x_1
            modifier=int(delta_y/abs(delta_y))
            for y in range(0,delta_y+modifier,modifier):
                coordinate_set.append([round(x_curr),y_1+y])
                #print(x_curr,coordinate_set[y])
                x_curr+=gradient*modifier
        else:
            y_curr=y_1
            modifier=int(delta_x/abs(delta_x))
            for x in range(0,delta_x+modifier,modifier):
                coordinate_set.append([x_1+x,round(y_curr)])
                #print(coordinate_set[x],y_curr)
                y_curr+=gradient*modifier

    return coordinate_set

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
    glColor3f(1.0, 0.0, 1.0) #konokichur color set (RGB)
    #call the draw methods here

    star_points_1=[[150,200],[300,200],[225,350]]
    star_points_2=[[150,310],[300,310],[225,160]]

    for a in range(-1,len(star_points_1)-1):
        #print(a,star_points_1[a][0],star_points_1[a][1],star_points_1[a+1][0],star_points_1[a+1][1])
        line_1 = dda(star_points_1[a][0],star_points_1[a][1],star_points_1[a+1][0],star_points_1[a+1][1])
        #print(line_1)
        for b in line_1:
            draw_points(b[0],b[1])
        #print()
    for a in range(-1,len(star_points_2)-1):
        #print(a,star_points_2[a][0],star_points_2[a][1],star_points_2[a+1][0],star_points_2[a+1][1])
        line_2 = dda(star_points_2[a][0],star_points_2[a][1],star_points_2[a+1][0],star_points_2[a+1][1])
        #print(line_2)
        for b in line_2:
            draw_points(b[0],b[1])
        #print()

    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()


#print(dda(1,1,11,6))