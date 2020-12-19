## Theodora Tataru
## Pixel the echodot
## Servos Script

import pantilthat
from time import sleep
#import RPi.GPIO as GPIO

def setServoAngle(servo, angle):
    ## vertical
    if servo == 'pan':
        pantilthat.servo_two(angle)
    ## horizontal
    if servo == 'tilt':
        pantilthat.servo_one(angle)
    sleep(0.3)


## this script will move both servos
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        setServoAngle('pan', 0)
        setServoAngle('tilt', 0)
    else:
        setServoAngle('pan', int(sys.argv[1]))
        setServoAngle('tilt', int(sys.argv[2]))
