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
        print("main: Starting the joystick check")
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
    time.sleep(2)
    motor.idle(threadjoystickstate)

    #motor.rotate_x_relative(10)
    '''
    while True:
        
        while threadjoystickstate.isSet():
            print("STOPPPPPP")
            pass
        print(motor.wrangler_status)
        x = wrangler.read_radio()
        is_firing, direction = x
        #print(x)
        if is_firing:
            fire.fire()
        if direction == WranglerController.Direction.NOP:
            pass
        elif direction == WranglerController.Direction.UP:
            wrangler.increase_y_angle(turnstate,threadjoystickstate)

        elif direction == WranglerController.Direction.DOWN:
            wrangler.decrease_y_angle(turnstate,threadjoystickstate)

        elif direction == WranglerController.Direction.LEFT:
            wrangler.increase_x_angle(turnstate,threadjoystickstate)

        elif WranglerController.Direction.RIGHT:
            wrangler.decrease_x_angle(turnstate,threadjoystickstate)
            
    '''