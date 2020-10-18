## Theodora Tataru
## Pixel the echodot
## Servos Script

import pantilthat
from time import sleep
import RPi.GPIO as GPIO

def setServoAngle(servo, angle):
    ## vertical
    if servo == 'pan':
        pantilthat.servo_two(angle)
    ## horizontal
    if servo == 'tilt':
        pantilthat.servo_one(angle)
    sleep(0.3)

if __name__ == '__main__':
    import sys
    servo = str(sys.argv[1])
    angle = int(sys.argv[2])
    setServoAngle(servo, angle)
    #GPIO.cleanup()
        