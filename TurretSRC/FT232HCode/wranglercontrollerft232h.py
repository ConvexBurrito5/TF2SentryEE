from __future__ import annotations

import time

import board
import digitalio
from threading import Event
from IO.wranglercontroller import WranglerController
from singletonboardft232h import SingletonBoardFT232H
from motorcontrollerft232h import MotorControllerFT232H


class WranglerControllerFT232H(WranglerController):

    def __init__(self, MotorController: MotorControllerFT232H):
        # Create wrangler status event
        self.WranglerStatus = Event()
        self.Motorcontroller = MotorController
        #Create the pin for the wrangler to monitor.
        self.statusPin = digitalio.DigitalInOut(board.D7)
        self.statusPin.direction = digitalio.Direction.INPUT
        print("Initialized: Wrangler Controller")

    #Checks the pin and updates event for the brain
    #if pin is low for more than 2 seconds, wrangler
    #is turned off.
    def check_status(self) -> None:
        if self.statusPin.value:
            self.WranglerStatus.set()
        else:
            self.WranglerStatus.clear()

    def increase_y_angle(self, turnstate: Event, threadjoystickstate: Event) -> bool:
        # Sets the current angle. Max is MAX_Y_ANGLE DEG

        threadjoystickstate.set()
        turnstate.wait()
        self.Motorcontroller.pause_y()
        turnstate.clear()
        return True

    def decrease_y_angle(self, turnstate: Event, threadjoystickstate: Event) -> bool:
        threadjoystickstate.set()
        turnstate.wait()
        self.Motorcontroller.pause_y()
        turnstate.clear()
        return True

    def read_radio(self) -> tuple[bool, WranglerController.Direction]:
        self.Motorcontroller.update_position()

        if self.Motorcontroller.fire_state == 1:
            tempData = True
        else:
            tempData = False

        if self.Motorcontroller.move_state == 3:
            return tempData, WranglerController.Direction.LEFT
        elif self.Motorcontroller.move_state == 4:
            return tempData, WranglerController.Direction.RIGHT
        elif self.Motorcontroller.move_state == 1:
            return tempData, WranglerController.Direction.UP
        elif self.Motorcontroller.move_state == 2:
            return tempData, WranglerController.Direction.DOWN
        else:
            return tempData, WranglerController.Direction.NOP
