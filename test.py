import numpy as np
import cv2

faceCascade = cv2.CascadeClassifier('AI-Pixel/Cascades/haarcascade_frontalface_default.xml')
capture = cv2.VideoCapture(0)
capture.set(3,300)
capture.set(3,300)

while True:
    ret, image = capture.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,     
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )
    print(faces)

    for(x,y,w,h) in faces:
        cv2.rectangle(image,(x,y), (x+w,y+h), (255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color=image[y:y+h, x:x+w]
        cv2.imshow('video',image)
        k = cv2.waitKey(30) & 0xff
        if k == 25:
            break

capture.release()
cv2.destroyAllWindows()