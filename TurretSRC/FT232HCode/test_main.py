import time

from motorcontrollerft232h import MotorControllerFT232H
from firingcontrollerft232h import FiringControllerFT232H
from peripheralcontrollerft232h import PeripheralControllerFT232H
from soundcontrollerft232h import SoundControllerFT232H
from wranglercontrollerft232h import WranglerControllerFT232H

motor = MotorControllerFT232H()
fire = FiringControllerFT232H()
periph = PeripheralControllerFT232H()
sound = SoundControllerFT232H()
wrangler = WranglerControllerFT232H()

fire.fire()
#sound.play_target_spotted()

while True:
    print(motor.get_x_angle())
    print(motor.get_y_angle())
    motor.set_x_angle(10)
    motor.set_y_angle(10)
    time.sleep(1)
    print(motor.get_x_angle())
    print(motor.get_y_angle())
    motor.set_x_angle(100)
    motor.set_y_angle(100)
    time.sleep(1)


'''
#periph.led_state(True)
fire.fire()
#periph.led_state(False)
periph.led_state(True)
time.sleep(2)
periph.led_state(False)

while True:
    periph.led_state(False)
    time.sleep(1)
    periph.led_state(True)
    time.sleep(1)
'''