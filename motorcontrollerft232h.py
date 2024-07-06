import time
import board
import busio
import digitalio
from board import SDA, SCL
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
from threading import Event
from ..IO.motorcontroller import MotorController


class MotorControllerFT232H(MotorController):

    def __init__(self):
        self._raw_x_pos = None
        self._raw_y_pos = None
        self.MAX_X_ANGLE = 270
        self.MAX_Y_ANGLE = 180
        self.total_fails = 0

        # create i2c Bus
        self.i2c_bus = busio.I2C(SCL, SDA)

        try:
            # Create the PCA9685 slave on the I2C bus
            self.PCA = PCA9685(self.i2c_bus)
            # Setup the SCL Freq
            self.PCA.frequency = 50
            self.PCA.channels[0].duty_cycle = 0x7FFF
            # DEFINE the servos HERE. In this case there is only one PCA9685 board here.
            # 500 & 2500 are the magic numbers for the Servos. Ripped off amazon page
            self.xAxis = servo.Servo(pwm_out=self.PCA.channels[0], min_pulse=500, max_pulse=2500, actuation_range=self.MAX_X_ANGLE)
            self.yAxis = servo.Servo(pwm_out=self.PCA.channels[1], min_pulse=500, max_pulse=2500, actuation_range=self.MAX_Y_ANGLE)
            print("Initialization of FT232H MotorController")

        except:
            print("PCA Not Connected")
            self.i2c_bus.unlock()

    def get_x_angle_raw(self) -> int:
        # returns its current angle.
        self._update_position()
        return self._raw_x_pos

    def get_y_angle_raw(self) -> int:
        # returns its current angle.
        self._update_position()
        return self._raw_y_pos

    """
    Returns the XY angle to 12 decimal places as to match gpiozero.
    Returns: the angle that the XY servo is currently in.
    """
    def get_x_angle(self) -> float:
        # Returns current angle in Percentage of 100
        return round(self.get_x_angle() / self.MAX_X_ANGLE,12)

    """
    Returns the YZ angle to 12 decimal places as to match gpiozero.
    Returns: the angle that the YZ servo is currently in.
    """
    def get_y_angle(self) -> float:
        # Returns current angle in Percentage of 100
        return round(self.get_y_angle() / self.MAX_Y_ANGLE,12)

    """
    Pass 0-MAX_X_ANGLE in, Sends CMD for XY(X) servo motor to turn.
    If the angle provided is too big, it will set the current_angle to MAX_Y_ANGLE
        and return False.
    If the angle is too small, it will set the current_angle to 0 
        and return False.
    angle: float the raw(not relative) angle that it should turn to.
    Returns True if 0<=angle<=MAX_X_ANGLE
        False if this condition is not met.
    """
    def set_x_angle(self, angle: float) -> bool:
        # Sets the current angle. MAX is MAX_X_ANGLE DEG
        if angle < 0:
            self.xAxis.angle = 0
            return False
        elif angle > self.MAX_X_ANGLE:
            self.xAxis.angle = self.MAX_X_ANGLE
            return False 
        else:
            self.xAxis.angle = angle
            return True

    """
    Pass 0-MAX_Y_ANGLE in, Sends CMD for YZ (Y) motor to turn.
    If the angle provided is too big, it will set the current_angle to MAX_Y_ANGLE
        and return False.
    If the angle is too small, it will set the current_angle to 0 
        and return False.
    angle: float the raw(not relative) angle that it should turn to.
    Returns True if 0<=angle<=MAX_Y_ANGLE
        False if this condition is not met.
    """
    def set_y_angle(self, angle: float) -> bool:
        # Sets the current angle. Max is MAX_Y_ANGLE DEG
        if angle < 0:
            self.yAxis.angle = 0
            return False
        elif angle > self.MAX_Y_ANGLE:
            self.yAxis.angle = self.MAX_Y_ANGLE
            return False 
        else:
            self.yAxis.angle = angle
            return True

    """
    This function will rotate the XY (X) motor by a relative input.
    For example, if you pass in 10 degrees and the motor is currently
    at 100 degrees, then the servo will spin to 110 degrees.
    It also accepts negative inputs, so -10 is also valid.

    *If the angle you specified was too much, it will just move to the max
    in that direction*
    E.g. If you put set angle = 1000, then it will just rotate to MAX_X_ANGLE.
    Same applies for the negative direction, if you try to spin too far, it
    will just go to zero.
    
    angle: float how many degrees we want to increase/decrease the servo
    Returns: True if 0 <= (angle + current_angle) <= MAX_X_ANGLE
        False if this condition is not met.
        Beware of floating point errors as you could get something that
        should be true, but isnt true.
    """
    def rotate_x_relative(self, angle: float) -> bool:
        xCurrent:float = self.get_x_angle()
        xNew = angle + xCurrent
        if xNew < 0:
            self.xAxis.angle = 0
            return False
        elif xNew > self.MAX_X_ANGLE:
            self.xAxis.angle = self.MAX_X_ANGLE
            return False
        else:
            self.set_x_angle(xNew)
            return True

    """
    This function will rotate the YZ (Y) motor by a relative input.
    For example, if you pass in 10 degrees and the motor is currently
    at 100 degrees, then the servo will spin to 110 degrees.
    It also accepts negative inputs, so -10 is also valid.

    *If the angle you specified was too much, it will just move to the max
    in that direction*
    E.g. If you put set angle = 1000, then it will just rotate to MAX_Y_ANGLE.
    Same applies for the negative direction, if you try to spin too far, it
    will just go to zero.
    
    angle: float how many degrees we want to increase/decrease the servo
    Returns: True if 0 <= (angle + current_angle) <= MAX_Y_ANGLE
        False if this condition is not met.
        Beware of floating point errors as you could get something that
        should be true, but isnt true.
    """
    def rotate_y_relative(self, angle: float) -> bool:
        yCurrent:float = self.get_x_angle()
        yNew = angle + yCurrent
        if yNew < 0:
            self.yAxis.angle = 0
            return False
        elif yNew > self.MAX_Y_ANGLE:
            self.yAxis.angle = self.MAX_Y_ANGLE
            return False
        else:
            self.set_y_angle(yNew)
            return True

    # set#Angle wrappers.
    def set_x_min(self) -> None:
        self.set_x_angle(0)

    def set_y_min(self) -> None:
        self.set_y_angle(0)

    def set_x_max(self) -> None:
        self.set_x_angle(self.MAX_X_ANGLE)

    def set_y_max(self) -> None:
        self.set_y_angle(self.MAX_Y_ANGLE)

    def pause_movement(self):
        self.set_x_angle(self.get_x_angle())
        self.set_y_angle(self.get_y_angle())

    def idle(self, stopCon: Event) -> None:
        # There is no way to make PWM signals convey speed.
        # To get an IDLE state for the turret we just move a few degrees
        # at a time and wait a few ms between.
        # Runs till event is set.
        while True:
            for _ in range(100):
                if stopCon.isSet():
                    stopCon.clear()
                    return
                self.rotate_x_relative(2.70)
                time.sleep(.025)

            for _ in range(100):
                if stopCon.isSet():
                    stopCon.clear()
                    return 
                self.rotate_x_relative(-2.70)
                time.sleep(.025)
            

    def _update_position(self, failCounter=1,limit=10) -> None:
        if failCounter >= limit:
            raise RuntimeError("Got bad data "+limit+" times in a row. Please check the code.")
        # Updates X and Y position from Using I2C comm with the aurduino that is monitoring the potentiometers
        # Check if I2C is open, if so take ctrl
        while not self.i2c_bus.try_lock():
            pass
        try:
            result = bytearray(8)
            # Address of aurduino is 0x55, load data into it
            self.i2c_bus.readfrom_into(0x55, result)
            # Convert bits into ints and load into array
            integers = [int(byte) for byte in result]
            # error checking of data, integers[7] is designed to be empty.
            # sometimes pulling info off aurduino takes too long and bad data pulled
            if integers[7] != 0 or integers[0] + integers[2] > self.MAX_X_ANGLE:
                # if bad data. print
                print('InvalidData: #{}'.format(failCounter))
                time.sleep(.2)
                # give bus back and recursive call until good data pulled
                self.i2c_bus.unlock()
                self.total_fails += 1
                self._update_position(failCounter=failCounter + 1)
            else:
                # update position status
                # Reset the fail counter
                failCounter = 0
                self._raw_x_pos = integers[0] + integers[2]
                self._raw_y_pos = integers[4]
        except:
            # Error catching. Happens when the aurduino cant be pinged from the I2C bus
            print("Aurduino not connected")
            self.i2c_bus.unlock()
        finally:
            # Finish by giving up the bus
            self.i2c_bus.unlock()
