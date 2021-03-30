from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
colors = ((1,0,0),
          (0,1,0),
          (0,0,1),
          (0,1,0),
          (1,1,1),
          (0,1,1),
          (1,0,0),
          (1,1,1),
          (0,1,1)
          )

surfaces = ((0,1,2,3),
            (3,2,7,6),
            (6,7,5,4),
            (4,5,1,0),
            (1,5,7,2),
            (4,0,3,6))
box_half =2
vertices =((box_half,-box_half,-box_half), (box_half,box_half,-box_half),
           (-box_half,box_half,-box_half),(-box_half,-box_half,-box_half),
           (box_half,-box_half,box_half),(box_half,box_half,box_half),
           (-box_half,-box_half,box_half),(-box_half,box_half,box_half))

edges= ((0,1),(0,3),(0,4),
        (2,1),(2,3),(2,7),
        (6,3),(6,4),(6,7),
        (5,1),(5,4),(5,7))
class Itembox_v1:
    def __init__(self, x, y, z= -8, color=(1,0,0)):
        self.x =x
        self.y =y
        self.z =z
        self.color =color
        self.ang = 0
        self.floating_range = 0.5
        self.floating_height = self.floating_range
        self.floating_direction = -0.1

    def draw(self, turn = False):
        glPushMatrix()
        glTranslatef(self.x, self.y, self.z)
        if turn :
            self.ang += 1
            if self.ang > 359:
                ang = 0

            self.floating_height += self.floating_direction
            if self.floating_height < -self.floating_range:
                self.floating_direction = 0.1
            elif self.floating_height > self.floating_range:
                self.floating_direction = -0.1
            glPushMatrix()
            glRotatef(self.ang, 0, 1, 0)
            glTranslatef(0, self.floating_height, 0)

            self.drawCube(self.color)

            glPopMatrix()
        else :
            glRotatef(self.ang, 0, 1, 0)
            glTranslatef(0, self.floating_height, 0)
            self.drawCube(self.color)
        glPopMatrix()


    def drawCube(self, color):
        glBegin(GL_QUADS)
        x = 0
        # print(color)
        for surface in surfaces:
            glColor3fv(color)
            x += 1
            for vertex in surface:
                glVertex3fv(vertices[vertex])

        glEnd()
        glColor3fv((0,0,0))
        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd()
