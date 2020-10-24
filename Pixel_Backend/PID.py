## Theodora Tataru 
## Final Year Project - Pixel, echo dot with face recognition
## 24 October 2020


## PID Controller implementation
import time

class PID:
    def __init__(self,kP=1,kI=0,kD=0):
        self.kP = kP
        self.kI = kI
        self.kD = kD

        self.current_time = time.time()
        self.previous_time = self.current_time
        self.previous_error = 0
        self.cP = 0
        self.cI = 0
        self.cD = 0

    def calculate_new_angle(self,error):
        time.sleep(0.1)

        self.current_time = time.time()

        ## time difference between cycles
        delta_time = self.current_time - self.previous_time

        ## difference between current error and prev error
        delta_error = error - self.previous_error

        ## error
        self.cP = error

        ## the integral will accumulate overtime until the setpoint is reached
        self.cI += error * delta_time

        ## is monitoring the slope to don't overshoot the error
        self.cD = (delta_error/delta_time) if delta_time > 0 else 0

        ## save current values for next iteration
        self.previous_time = self.current_time
        self.previous_error = error

        ## returns the new coordonates fot the servo
        return sum([
            self.kP * self.cP,
			self.kI * self.cI,
			self.kD * self.cD])