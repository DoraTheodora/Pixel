## Theodora Tataru 
## Final Year Project - Pixel, echo dot with face recognition
## 24 October 2020

from multiprocessing import Manager,Process
import pantilthat as hat
import PID
import signal
import sys
import cv2
from imutils.video import VideoStream
import face_utils

## everything in this method will run concurrently
## because we are using the Proceess when is called 

def test(sig,frame):
    sys.exit()

def center_face(faceX,faceY,centerX,centerY):
    signal.signal(signal.SIGINT,test)

    stream = VideoStream(usePiCamera=True).start()
    #time.sleep(2.0)

    faceDetector = face_utils.face_utils()

    while True:
        frame = stream.read()

        ## get the resolution of the frame
        (Height, Width) = frame.shape[:2] 
        ## get the middle of the frame
        centerX.value = Width // 2
        centerY.value = Height // 2

        center_coordinates = faceDetector.update(frame,centerX.value,centerY.value)

        (faceX.value,faceY.value,faceFound) = center_coordinates

        if faceFound is not None:
            (top_left_x,top_left_y,face_width,face_height) = faceFound
            cv2.rectangle(frame, (top_left_x,top_left_y),
            (top_left_x+face_width,top_left_y+face_height),(51, 204, 255),2) ## 2 is for thickness

        cv2.imshow('Face Tracking Pixel',frame)
        cv2.waitKey(1)

def move_servos(pan,tilt):
    signal.signal(signal.SIGINT,test)

    while True:
        pan_value = tilt.value
        tilt_value = pan.value
        print(f"{pan_value}    \t  {tilt_value}")
        if pan_value >= -90 and pan_value <= 90:
            hat.pan(pan_value)
        if tilt_value >= -90 and tilt_value <= 90:
            hat.tilt(tilt_value)

## controler for pan and tilt
## v is the output value: pan or the tilt
def controller(v,P,I,D,face_coordinate,center_coordinate):
    signal.signal(signal.SIGINT,test)

    p = PID.PID(P.value,I.value,D.value)

    while True:
        error = center_coordinate.value - face_coordinate.value
        v.value = p.calculate_new_angle(error)

if __name__ == '__main__':

    with Manager() as manager:

        hat.servo_enable(1, True)
        hat.servo_enable(2, True)
        
        faceX = manager.Value("i", 0)
        faceY = manager.Value('i',0)

        centerX = manager.Value("i", 0)
        centerY = manager.Value("i", 0)

        horizontal_value = manager.Value('i',0)
        horizontalP = manager.Value('f',0.09)
        horizontalI = manager.Value('f',0.08)
        horizontalD = manager.Value('f',0.002)

        vertical_value = manager.Value('i',0)
        verticalP = manager.Value('f',0.10)
        verticalI = manager.Value('f',0.11)
        verticalD = manager.Value('f',0.002)

        #together.move_servos_together()

        process_center_face = Process(target=center_face,
            args=(faceX,faceY,centerX,centerY))

        process_horizontal = Process(target=controller,
            args=(horizontal_value,horizontalP,horizontalI,horizontalD,faceX,centerX))

        process_vertical = Process(target=controller,
            args=(vertical_value,verticalP,verticalI,verticalD,faceY,centerY))

        process_move_servos = Process(target=move_servos,
            args=(horizontal_value,vertical_value))

        process_center_face.start()
        process_horizontal.start()
        process_vertical.start()
        process_move_servos.start()

        process_center_face.join()
        process_horizontal.join()
        process_vertical.join()
        process_move_servos.join()

        # disable the servos
        hat.servo_enable(1, False)
        hat.servo_enable(2, False)