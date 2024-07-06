import time

import board
import digitalio

from ..IO.firingcontroller import FiringController


class FiringControllerFT232H(FiringController):

    def __init__(self):
        # init Shooting pin
        self.shoot = digitalio.DigitalInOut(board.C0)
        self.shoot.direction = digitalio.Direction.OUTPUT
        self.shoot.value = False

    def fire(self) -> None:
        # Shoots one shot
        self.shoot.value = True
        time.sleep(0.1)
        self.shoot.value = False
