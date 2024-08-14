from __future__ import annotations



import board
import digitalio
from threading import Event
from IO.wranglercontroller import WranglerController
from singletonboardft232h import SingletonBoardFT232H


class WranglerControllerFT232H(WranglerController):

    def __init__(self):
        # Create wrangler status event
        self.WranglerStatus = Event()
        self.i2c_bus = SingletonBoardFT232H().i2c_bus

        #Create the pin for the wrangler to monitor.
        self.statusPin = digitalio.DigitalInOut(board.C1)
        self.statusPin.direction = digitalio.Direction.INPUT

    #Checks the pin and updates event for the brain
    #if pin is low for more than 2 seconds, wrangler
    #is turned off.
    def check_status(self) -> None:
        if self.statusPin.value:
            self.WranglerStatus.set()
        else:
            self.WranglerStatus.clear()

    def read_radio(self) -> tuple[bool, WranglerController.Direction]:

        while not self.i2c_bus.try_lock():
            pass
        try:
            result = bytearray(9)
            # Address of aurduino is 0x55, load data into it
            self.i2c_bus.readfrom_into(0x55, result)
            # Convert bits into ints and load into array
            self.i2c_bus.unlock()
            data = result[8]
            # TBD RETURNCASEMODIFIED
            if data[0] == 'N':
                return False, WranglerController.Direction.NOP
            if data[0] == 'F':
                tempData = True
            else:
                tempData = False

            if data[0] == "L":
                return tempData, WranglerController.Direction.LEFT
            elif data[0] == "R":
                return tempData, WranglerController.Direction.RIGHT
            elif data[0] == "U":
                return tempData, WranglerController.Direction.UP
            elif data[0] == "D":
                return tempData, WranglerController.Direction.DOWN
        except:
            # Error catching. Happens when the aurduino cant be pinged from the I2C bus
            print("Aurduino not connected")
            self.i2c_bus.unlock()
        finally:
            # Finish by giving up the bus
            self.i2c_bus.unlock()

        #L, R, U, D, F
        #LEFT (L) - X neg 3 deg
        #RIGHT (R) - X pos 3 deg
        #UP (U) - Y pos 3 deg
        #DOWN (D) - Y neg 3 deg
        #SHOOT (F) - Shoot 1 Shot