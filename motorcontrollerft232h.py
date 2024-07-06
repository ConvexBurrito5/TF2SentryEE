import time
import board
import busio
import digitalio
from board import SDA, SCL
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
from threading import Event

#(Motorcontroller)
class MotorControllerFT232H:

    def __init__(self):
        self.x_pos = None
        self.y_pos = None

        # init Shooting pin
        self.shoot = digitalio.DigitalInOut(board.C0)
        self.shoot.direction = digitalio.Direction.OUTPUT
        self.shoot.value = False
        # init LED Pin
        self.LED = digitalio.DigitalInOut(board.C1)
        self.LED.direction = digitalio.Direction.OUTPUT
        self.shoot.value = False

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
            self.xAxis = servo.Servo(pwm_out=self.PCA.channels[0], min_pulse=500, max_pulse=2500, actuation_range=270)
            self.yAxis = servo.Servo(pwm_out=self.PCA.channels[1], min_pulse=500, max_pulse=2500, actuation_range=180)

        except:
            print("PCA Not Connected")
            self.i2c_bus.unlock()

    def get_x_angle_raw(self) -> int:
        # returns its current angle.
        self._update_position()
        return self.x_pos

    def get_y_angle_raw(self) -> int:
        # returns its current angle.
        self._update_position()
        return self.y_pos

    def get_x_angle(self) -> float:
        # Returns current angle in Percentage of 100
        return (self.get_x_angle()) / 270

    def get_y_angle(self) -> float:
        # Returns current angle in Percentage of 100
        return (self.get_y_angle()) / 180

    def set_x_angle(self, angle: int) -> bool:
        # Sets the current angle. MAX 270 DEG
        if angle > 270:
            return True
        else:
            self.xAxis.angle = angle

    def set_y_angle(self, angle: int) -> bool:
        # Sets the current angle. Max is 180 DEG
        if angle > 180:
            return True
        else:
            self.xAxis.angle = angle

    def rotate_x_relative(self, angle: int) -> bool:
        xCurrent = self.get_x_angle()
        xNew = angle + xCurrent
        if 0 > xNew or 270 < xNew:
            return True
        else:
            self.set_x_angle(int(xNew))

    def rotate_y_relative(self, angle: int) -> bool:
        yCurrent = self.get_x_angle()
        yNew = angle + yCurrent
        if 0 > yNew or 270 < yNew:
            return True
        else:
            self.set_x_angle(int(yNew))

    # set#Angle wrappers.
    def set_x_min(self) -> None:
        self.set_x_angle(0)

    def set_y_min(self) -> None:
        self.set_y_angle(0)

    def set_x_max(self) -> None:
        self.set_x_angle(270)

    def set_y_max(self) -> None:
        self.set_y_angle(180)

    def pause_movement(self):
        self.set_x_angle(int(self.get_x_angle()))
        self.set_y_angle(int(self.get_y_angle()))

    def idle(self, stopCon: Event) -> None:
        # There is no way to make PWM signals convey speed.
        # To get an IDLE state for the turret we just move a few degrees
        # at a time and wait a few ms between.
        # Runs till event is set.
        while not stopCon.isSet():
            for x in range(100):
                self.set_x_angle(int(2.70 * x))
                self.set_y_angle(int(1.80 * x))
                time.sleep(.025)
                if stopCon.isSet():
                    break

            if stopCon.isSet():
                break

            for x in range(100):
                self.set_x_angle(270 - int(2.70 * x))
                self.set_y_angle(180 - int(1.80 * x))
                time.sleep(.025)
                if stopCon.isSet():
                    break

    def fire(self) -> None:
        # Shoots one shot
        self.shoot.value = True
        time.sleep(0.1)
        self.shoot.value = False

    def led_state(self, state: bool) -> None:
        # Updates LED state
        self.LED.value = state

    def _update_position(self, failCounter=1) -> None:
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
            if integers[7] != 0 or integers[0] + integers[2] > 270:
                # if bad data. print
                print('InvalidData: #{}'.format(failCounter))
                time.sleep(.2)
                # give bus back and recursive call until good data pulled
                self.i2c_bus.unlock()
                self._update_position(failCounter=failCounter + 1)
            else:
                # update position status
                self.x_pos = integers[0] + integers[2]
                self.y_pos = integers[4]
        except:
            # Error catching. Happens when the aurduino cant be pinged from the I2C bus
            print("Aurduino not connected")
            self.i2c_bus.unlock()
        finally:
            # Finish by giving up the bus
            self.i2c_bus.unlock()
