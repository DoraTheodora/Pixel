## Theodora Tataru
## C00231174
## Pixel Virtual Assistant
## 23 December 2020

import numpy as np
import time
import os
import multiprocessing

from multiprocessing import Process
from multiprocessing import Manager

import face_recognition
import display
import virtual_assistant
import argparse
import argparse
import imutils
import pickle
import time
import cv2


def start(user:str, faceFound:bool, timeFaceFound:float, delay:float, runCamera:bool):
    """[summary]
    :param user: [description]
    :type user: str
    :param faceFound: [description]
    :type faceFound: bool
    :param timeFaceFound: [description]
    :type timeFaceFound: float
    :param delay: [description]
    :type delay: float
    """
    # load the known faces and embeddings along with OpenCV's Haar
    # cascade for face detection
    print("[INFO] loading encodings + face detector...")
    detector = cv2.CascadeClassifier("Cascades/haarcascade_frontalface_default.xml")
    data = pickle.loads(open("Cascades/encodings.pickle", "rb").read())

    # initialize the video stream and allow the camera sensor to warm up
    print("[INFO] starting video stream...")
    cam = cv2.VideoCapture(0)
    while runCamera:
        # grab the frame from the threaded video stream and resize it
	    # to 500px (to speedup processing)
        ret, frame = cam.read()
        #frame = imutils.resize(frame, width=300)
        # convert the input frame from (1) BGR to grayscale (for face
	    # detection) and (2) from BGR to RGB (for face recognition)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # detect faces in the grayscale frame
        rects = detector.detectMultiScale(gray, scaleFactor=1.1, 
            minNeighbors=5, minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE)
        # OpenCV returns bounding box coordinates in (x, y, w, h) order
        # but we need them in (top, right, bottom, left) order, so we
        # need to do a bit of reordering
        boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]

        # compute the facial embeddings for each face bounding box
        encodings = face_recognition.face_encodings(rgb, boxes)
        #print("[INFO] encodings: ", encodings)
        if len(encodings) > 0:
            faceFound.value = True
            timeFaceFound.value = time.time()
        else:
            faceFound.value = False
            delay.value = idle(timeFaceFound.value)
            print("[INFO] Idle time: ", delay.value)
        names = []

        # loop over the facial embeddings
        for encoding in encodings:
            # attempt to match each face in the input image to our known
            # encodings
            matches = face_recognition.compare_faces(data["encodings"],
                encoding)
            name = "stranger"

            # check to see if we have found a match
            if True in matches:
                # find the indexes of all matched faces then initialize a
                # dictionary to count the total number of times each face
                # was matched
                matchedFaceVectors = [i for (i, b) in enumerate(matches) if b]
                counts = {}

                # loop over the matched indexes and maintain a count for
                # each recognized face face
                for i in matchedFaceVectors:
                    name = data["names"][i]
                    counts[name] = counts.get(name, 0) + 1

                # determine the recognized face with the largest number
                # of votes (note: in the event of an unlikely tie Python
                # will select first entry in the dictionary)
                name = max(counts, key=counts.get)
                # print("[INFO] Counts: ", counts)

            # update the list of names
            names.append(name)
            user.value = name
            #*print("[INFO] Name: ", name)
        # loop over the recognized faces
        # print("[INFO] faceFound: ", faceFound.value)
        for ((top, right, bottom, left), name) in zip(boxes, names):
            # draw the predicted face name on the image
            cv2.rectangle(frame, (left, top), (right, bottom),
                (0, 255, 0), 2)
            y = top - 15 if top - 15 > 15 else top + 15
            cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                0.75, (0, 255, 0), 2)

        # display the image to our screen
        cv2.imshow("Frame", frame)

    if(runCamera.value == False):
        cam.release()
        cv2.destroyAllWindows()
        print("[INFO] Main camera stopped")


def idle(timeFaceFound):
    idleTime = time.time() - timeFaceFound
    return idleTime

#start(True, time.time(), 0)
    