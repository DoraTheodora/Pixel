## Theodora Tataru
## C00231174
## Pixel Virtual Assistant
## 23 December 2020

import numpy as np
import cv2
import time
import os
import multiprocessing

from multiprocessing import Process
from multiprocessing import Manager

import display
import virtual_assistant

faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
capture = cv2.VideoCapture(0)
capture.set(3,300)
capture.set(3,300)

def start(faceFound:bool, timeFaceFound:float, delay:float):
    while True:
        ret, image = capture.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #faces.remove()
        #print(dir(faces))
        faces = (faceCascade.detectMultiScale(
            gray,     
            scaleFactor=1.2,               
            minNeighbors=5,     
            minSize=(20, 20)
        ))
        if len(faces) > 0:
            faceFound.value = True
        else:
            faceFound.value = False
            delay.value =  idle(timeFaceFound.value)
            #print("------",faceFound.value, delay.value)

        #print(faces)
        for(x,y,w,h) in faces:
            timeFaceFound.value = time.time()
            cv2.rectangle(image,(x,y), (x+w,y+h), (255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = image[y:y+h, x:x+w]
            #cv2.imshow('video',image)
            k = cv2.waitKey(30) 
            if k == 25:
                break

    capture.release()
    cv2.destroyAllWindows()


def idle(timeFaceFound):
    idleTime = time.time() - timeFaceFound
    return idleTime
    #print("Idle time: ", idleTime)
    