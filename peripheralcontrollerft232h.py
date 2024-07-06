from ..IO.peripheralcontroller import PeripheralController


class PeripheralControllerFT232H(PeripheralController):

    def __init__(self):
        # init LED Pin
        self.LED = digitalio.DigitalInOut(board.C1)
        self.LED.direction = digitalio.Direction.OUTPUT
        self.shoot.value = False

    def led_state(self, state: bool) -> None:
        # Updates LED state
        self.LED.value = state
