import time

from motorcontrollerft232h import MotorControllerFT232H
from firingcontrollerft232h import FiringControllerFT232H
from peripheralcontrollerft232h import PeripheralControllerFT232H
from soundcontrollerft232h import SoundControllerFT232H
from wranglercontrollerft232h import WranglerControllerFT232H
from IO.wranglercontroller import WranglerController
from threading import Event, Thread
motor = MotorControllerFT232H()
fire = FiringControllerFT232H()
periph = PeripheralControllerFT232H()
sound = SoundControllerFT232H()
wrangler = WranglerControllerFT232H(motor)

#sound.play_target_spotted()
turnstate = Event()
threadjoystickstate = Event()
def check_joystick_state(turnstate: Event, threadjoystickstate: Event):
    joystickCount = 0
    while 1:
        threadjoystickstate.wait()
        #print("main: Starting the joystick check")
        complete = False
        while not complete:
            wranglerData = wrangler.read_radio()
            #print("inside loop")
            if wranglerData[1] == WranglerController.Direction.NOP:
                joystickCount+=1
                if joystickCount >= 2:
                    turnstate.set()
                    complete = True
            else:
                joystickCount = 0
        joystickCount = 0
        #print("Joystick let go")
        threadjoystickstate.clear()




if __name__ == "__main__":
    check_joystick: Thread = Thread(target=check_joystick_state, name="check_joystick", args=(turnstate,threadjoystickstate))
    check_joystick.start()
    # WranglerRadioTest
    #x = wrangler.read_radio()
    #print("-----------------")
    #print(x)
    motor.set_x_angle(0)
    motor.set_y_angle(0)
    while True:

        x = wrangler.read_radio()
        is_firing, direction = x

        print(x)
        if is_firing:
            fire.fire()
        if direction == WranglerController.Direction.NOP:
            pass
        elif direction == WranglerController.Direction.UP:
            #temp = motor.get_y_angle()
            #motor.set_y_angle(temp + 10)

            wrangler.increase_y_angle(turnstate,threadjoystickstate)

            #print(motor.get_y_angle())
            print("Turning Up!")
            #motor.rotate_y_relative(3)

        elif direction == WranglerController.Direction.DOWN:
            wrangler.decrease_y_angle(turnstate,threadjoystickstate)
            print("Turning Down!")

        '''
        
        elif direction == WranglerController.Direction.LEFT:
            temp = motor.get_x_angle()
            motor.set_x_angle(temp + 10)
            print("Turning Left! 3 Degrees")

            #motor.rotate_x_relative(-3)
        elif WranglerController.Direction.RIGHT:
            temp = motor.get_x_angle()
            motor.set_x_angle(temp - 10)
            print("Turning Right! 3 Degrees")
        
        '''