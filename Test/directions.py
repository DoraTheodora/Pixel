#Theodora Tataru
#C00231174

#This class implements the communication between the chip set

import time
import math
import RPi.GPIO as GPIO
from PCA9685 import PCA9685


class Directions(object):
    def __init__(self):
        print("starting...")
        self.pwm = PCA9685() #communication with the chipset
        self.PWM_FREQUENCY = 50 #max 1500
        self.pwm.setPWMFreq(self.PWM_FREQUENCY)

        self.INIT_HORIZONTAL_ANGLE = 70
        self.INIT_VERTICAL_ANGLE = 70
        self.move(horizontal = self.INIT_HORIZONTAL_ANGLE, vertical=self.INIT_VERTICAL_ANGLE)

    def __del__(self):
        """ Class that will run when the object is destroyed """
        print("done...")
        self.pwm.exit_PCA9685()
        GPIO.cleanup()

    def move(self, horizontal, vertical):
        self.move_horizontal(horizontal_angle = horizontal)
        self.move_vertical(vertical_angle= vertical)

    def move_horizontal(self, horizontal_angle):
        self.pwm.setRotationAngle(0, horizontal_angle)

    def move_vertical(self, vertical_angle):
        self.pwm.setRotationAngle(1, vertical_angle)

    ## Range tests
    def horizontal_range_test(self):
        """ Testing the X axis range """
        for angle in range(10,170,1):
            print(("Moving Horizontally...." + str(angle)))
            self.move_horizontal(horizontal_angle=angle)
            time.sleep(0.1) 
        for angle in range(170,10,-1):
            print(("Moving Horizontally...." + str(angle)))
            self.move_horizontal(horizontal_angle=angle)
            time.sleep(0.1) 

    def vertical_range_test(self):
        """ Testing the Y axis range """
        for angle in range(70,170,1):
            print(("Moving Vetically..." + str(angle)))
            self.move_vertical(vertical_angle=angle)
            time.sleep(0.1)
        for angle in range(170,70,-1):
            print(("Moving Vetically..." + str(angle)))
            self.move_vertical(vertical_angle=angle)
            time.sleep(0.1)

    ## Tests
    def input_horizontal_test(self):
        while True:
            x_axis = input("Horizontal Angle: ")
            angle = int(x_axis)
            self.move_horizontal(horizontal_angle=angle)

    def input_vertical_test(self):
        while True:
            y_axis = input("Vertical Angle: ")
            angle = int(y_axis)
            self.move_vertical(vertical_angle=angle)

    
    def circle_test(self, repetitions=1):

        # These values are base on Hardware observations where they are stable.
        max_range = 100
        min_range = 30
        period = 0.1
        increments = 10

        for num in range(repetitions):
            for angle in range(0,359,increments):
                h_angle = int((((math.sin(math.radians(angle)) + 1.0) / 2.0) * (max_range - min_range)) + min_range)
                v_angle = int((((math.cos(math.radians(angle)) + 1.0) / 2.0) * (max_range - min_range)) + min_range)

                print(("Moving Yaw="+str(v_angle)))
                print(("Moving Pitch=" + str(h_angle)))

                self.move_vertical(h_angle)
                self.move_horizontal(v_angle)
                time.sleep(period)

            for angle in range(0,359,-increments):
                h_angle = int((((math.sin(math.radians(angle)) + 1.0) / 2.0) * (max_range - min_range)) + min_range)
                v_angle = int((((math.cos(math.radians(angle)) + 1.0) / 2.0) * (max_range - min_range)) + min_range)

                print(("Moving Yaw="+str(v_angle)))
                print(("Moving Pitch=" + str(h_angle)))

                self.move_vertical(v_angle)
                self.move_horizontal(h_angle)
                time.sleep(period)

def horizontal_test():
    this_object = Directions()
    this_object.horizontal_range_test()

def vertical_test():
    this_object = Directions()
    this_object.vertical_range_test()

def input_horizontal_test():
    this_object = Directions()
    this_object.input_horizontal_test()

def input_vertical_test():
    this_object = Directions()
    this_object.input_vertical_test()   

def input_test():
    this_object = Directions()
    while True:
        x = input("x angle: ")
        y = input("y angle: ")
        this_object.move(int(x), int(y))    



if __name__ == "__main__":
    horizontal_test()
    #vertical_test()
    #input_horizontal_test()
    #input_vertical_test()
    #input_test()


    

