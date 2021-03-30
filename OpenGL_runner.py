import pygame
from pygame.locals import*
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from Itembox import Itembox_v1
import numpy as np
import cv2

def start_opengl(info, no_use):
    #setting pygame and pyopengl
    pygame.init()
    display=(640, 480)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 500.0)

    x_move = 0
    y_move = 0

    #setting boxes
    box1 = Itembox_v1(5.0, -8.0, -30)
    box2 = Itembox_v1(0.0, -8.0, -30, (0, 0, 1))
    box3 = Itembox_v1(-5.0, -8.0, -30, (0, 0, 1))
    box4 = Itembox_v1(-10.0, -8.0, -30, (0, 0, 1))
    box5 = Itembox_v1(10.0, -8.0, -30, (0, 0, 1))
    while info["activate"] == False:
        continue

    while True:
        flag = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_move = -0.3
                if event.key == pygame.K_RIGHT:
                    x_move = 0.3
                if event.key == pygame.K_DOWN:
                    y_move = -0.3
                if event.key == pygame.K_UP:
                    y_move = 0.3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_move = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_move = 0
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        currFrame = info["image"]
        currFrame = cv2.flip(currFrame, 0)
        glDisable(GL_DEPTH_TEST)
        glDrawPixels(currFrame.shape[1], currFrame.shape[0], GL_BGR, GL_UNSIGNED_BYTE, currFrame)
        glEnable(GL_DEPTH_TEST)
        #move the boxes
        glTranslatef(x_move, y_move, 0)

        time = pygame.time.get_ticks()%10
        if time ==0 :
            #turn every 10ms
            box1.draw(True)
            box2.draw(True)
            box3.draw(True)
            box4.draw(True)
            box5.draw(True)
        else :
            box1.draw()
            box2.draw()
            box3.draw()
            box4.draw()
            box5.draw()
        pygame.display.flip()
	
	#end drawing
        if info["stop"] or flag:
            break
    pygame.quit()
    print("end")
