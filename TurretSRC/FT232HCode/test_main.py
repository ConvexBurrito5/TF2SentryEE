import time

from motorcontrollerft232h import MotorControllerFT232H
from firingcontrollerft232h import FiringControllerFT232H
from peripheralcontrollerft232h import PeripheralControllerFT232H
from soundcontrollerft232h import SoundControllerFT232H
from wranglercontrollerft232h import WranglerControllerFT232H
from IO.wranglercontroller import WranglerController

motor = MotorControllerFT232H()
fire = FiringControllerFT232H()
periph = PeripheralControllerFT232H()
sound = SoundControllerFT232H()
wrangler = WranglerControllerFT232H()

#sound.play_target_spotted()


if __name__ == "__main__":
    while True:
        '''
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

        #WranglerRadioTest
        x = wrangler.read_radio()
        print(x)
        is_firing, direction = x
        if is_firing:
            fire.fire()
        if direction == WranglerController.Direction.NOP:
            pass
        elif direction == WranglerController.Direction.UP:
            motor.rotate_y_relative(3)
        elif direction == WranglerController.Direction.DOWN:
            motor.rotate_y_relative(-3)
        elif direction == WranglerController.Direction.LEFT:
            motor.rotate_x_relative(-3)
        elif WranglerController.Direction.RIGHT:
            motor.rotate_x_relative(3)
        time.sleep(.5)


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


