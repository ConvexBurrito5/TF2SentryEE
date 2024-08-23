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
        self.statusPin = digitalio.DigitalInOut(board.D7)
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
        result = bytearray(14)

        while not self.i2c_bus.try_lock():
            pass
        try:
            # Address of aurduino is 0x55, load data into it
            self.i2c_bus.readfrom_into(0x55, result)
            #NOTE, I2C bus doubles the data passed through.
            # Convert bits into ints and load into array
            self.i2c_bus.unlock()
            print(result)
            #data = result[8]
            data = [int(byte) for byte in result]
            # TBD RETURNCASEMODIFIED
            print(data)
            print(data[10])
            if data[8] == 1:
                tempData = True
            else:
                tempData = False

            if data[10] == 3:
                return tempData, WranglerController.Direction.LEFT
            elif data[10] == 4:
                return tempData, WranglerController.Direction.RIGHT
            elif data[10] == 1:
                return tempData, WranglerController.Direction.UP
            elif data[10] == 2:
                return tempData, WranglerController.Direction.DOWN
            else:
                return tempData, WranglerController.Direction.NOP
        except:
            # Error catching. Happens when the aurduino cant be pinged from the I2C bus
            print("Aurduino not connected(Wrangler). I2C returning Bad Data")
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