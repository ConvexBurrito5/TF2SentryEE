# TF2Sentry
![exp](https://wiki.teamfortress.com/w/images/3/3a/TF2LVL1SG.png)

This is the second half of a project with [Maiikiru](https://github.com/Maiikiru)
to create a fully functioning level one sentry from TF2 using AIRSOFT guns.
It is structurally impossible for this design to be used with a real weapon and is not our goal.

With that out of the way, lets look into what we have completed.
## Features
- Detection and tracking of a person, See Maiikiru's [CV Repo](https://github.com/Maiikiru/TF2SentrySource)
- We have provided Maiikiru's [CV Repo](https://github.com/Maiikiru/TF2SentrySource) with standard API interfaces is easy to implement multiple hardware solutions. So far:
  - Raspberry Pi 4
  - Standard laptop using [Adafruit's FT232H Breakout](https://www.adafruit.com/product/2264) 
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