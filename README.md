### To the ATF, It is structurally impossible for this design to be used with a real weapon and is not our goal. I am a law-abiding citizen.
### To Lockheed Martin, call me...
# TF2Sentry
This is the physical portion of a project with [Maiikiru](https://github.com/Maiikiru)
to create a fully functioning level one sentry from TF2 using AIRSOFT guns.

This repo is my work (Steven Naliwajka/ConvexBurrito5), [GitHub](https://github.com/ConvexBurrito5), [LinkedIn](https://www.linkedin.com/in/steven-naliwajka-69564929a/)

See [Maiikiru's CV Repo](https://github.com/Maiikiru/TF2SentrySource) for his magic!
### Two options for movement, 
1) Maiikiru has gone through and created a Computer vision (CV) repo that automaticaly detects and targets people: [Maiikiru's CV Repo](https://github.com/Maiikiru/TF2SentrySource)
2) I have also gone and created a remote control, [a slightly modified wrangler](https://www.youtube.com/watch?v=LYPzGNSfVRk)


To jump straight into it see the instruction folder.

![sentry](https://wiki.teamfortress.com/w/images/thumb/3/3a/TF2LVL1SG.png/163px-TF2LVL1SG.png)
![wrangler](https://wiki.teamfortress.com/w/images/thumb/2/27/BLU_Wrangler.png/192px-BLU_Wrangler.png)

## Skills
- At a high level, what we are trying to accomplish is simple however, as always, implementation is not as easy. I have learned lots:
  - Communication!
    - I2C Communication, learned how to implement and write code to utilize it. 
    - Radio, utilizing 2.4Ghz wireless transceiver modules to talk from the turret to the wrangler
  - Power!
    - The turrent and wrangler run off batteries
    - 7v, 12v, 6v was all required. Got to use Buck DC voltage regulators.
    - Load calculation to make sure at least 5 hours of battery life.
  - Circuitry!
    - Circuitry to be able to plug in the turret without removing the battery. Same for Wrangler.
  - Working with Motors/Servos with control from both I2C and PWM pins.
  - Improved my coding skill, Arduino(C++), Python.
  - Improved my 3D printing skill... and gotten a sizeable print farm out of it.



With that out of the way, lets look into what we have completed.
## Features
- Detection and tracking of a person, See [Maiikiru's CV Repo](https://github.com/Maiikiru/TF2SentrySource)
- We have provided [Maiikiru's CV Repo](https://github.com/Maiikiru/TF2SentrySource) with standard API interfaces so it easy to implement multiple hardware solutions. So far:
  - Raspberry Pi 4, See 'instructionFT232H.md'
  - Standard laptop using [Adafruit's FT232H Breakout](https://www.adafruit.com/product/2264), See 'instructionRaspberryPi4.md'
- There are 4 interfaces implemented in each solution
  - FiringController
    - Handles the firing by pulling logic high on a switch to bridge the motor on the airsoft gun.
  - MotorController
    - Handles all motion. Basic set of methods to move your servos.
    - Idle motion, pans slowly looking for people.
  - PeripheralController
    - Handles the leds
  - SoundController
    - Handles all the sound, runs off of the devices default speaker.
- If a switch on the wrangler is turned on, automatic movement from [Maiikiru's CV Repo](https://github.com/Maiikiru/TF2SentrySource) will be disabled and overruled.
  - Input will be solely from the joystick and the firing button on the Wrangler.