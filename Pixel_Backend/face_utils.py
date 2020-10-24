## Theodora Tataru 
## Final Year Project - Pixel, echo dot with face recognition
## 24 October 2020

import imutils
import cv2

class face_utils:
    def __init__(self):
        self.face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    def update(self,frame,centerX,centerY):
        gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 

        ## TODO: keep track of the person was there first
        ##

        ## detect all faces in the video frame -> look up MIN NEIGHBOURS
        faces_detected = self.face_detector.detectMultiScale(gray_frame,scaleFactor=1.05,
            minNeighbors=9,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)

        if len(faces_detected) > 0:
            (top_left_x,top_left_y,face_width,face_height) = faces_detected[0] #First face detected
            ## get the center of the face detected
            center_face_x = int(top_left_x + (face_width / 2) )
            center_face_y = int(top_left_y + (face_height / 2) )

            return (center_face_x,center_face_y,faces_detected[0])
        ## if no face was dected, retern the initial value    
        return (centerX,centerY,None)



