#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from multiprocessing import Process, Manager
from OpenGL_runner import start_opengl

def draw_item(data):
    #"/usb_cam/image_raw"토픽을 통해서 얻은 이미지를 받아서, 공유메모리의 이미지를 수정한다.
    try :
        cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e :
        print(e)
    info["activate"] = True
    info["image"] = cv_image


if __name__ =='__main__':
    rospy.init_node('box_maker', anonymous=True)

    #멀티프로세스 th1에서 이미지를 얻어서 OpenGL을 적용해야한다.
    #미리 공유메모리를 딕셔너리 형태로 만들어둔다.
    manager = Manager()
    info = manager.dict()
    info["activate"] =False
    info["stop"] = False
    
    #PyopenGL을 돌릴 프로세스를 만든다.
    OG_worker = Process(target=start_opengl, args=(info,4))
    OG_worker.start()
    
    #image msg를 받아서, OpenCV numpy 이미지로 바꿔주는 CvBridge 인스턴스 생성
    bridge = CvBridge()
    #이미지를 받아주는 Subsriber핸들러를 만든다. 
    image_sub = rospy.Subscriber("/usb_cam/image_raw", Image, draw_item, queue_size=1)
    rospy.spin()
    
    #ros종류후에 pyopengl도 종료시킨다. 
    info["stop"] = True
    OG_worker.join()
