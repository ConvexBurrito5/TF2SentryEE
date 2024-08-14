## How do I get live position data from a 3 Wire servo?
Servos traditionally have 3 wires
1) Signal wire - Sends PWM data
2) Vcc
3) GND

Spoiler: We add a 4th wire. A wire that sends analog (# data, not binary) data.

To do this, we will disassemble our brand-new servos and solder a new wire. 
A broad statement but, every servo I have run into has contained a potentiometer.

### What is a Potentiometer?
The common Potentiometer that we will be dealing with here has 3 pins.
The left one traditionally is Vcc and the right one is GND. The middle pin is the one that we care about.
Besides the pins of the potentiometer is a piece that spins on a fixed range. The degree of the spin determines
the voltage of the middle pin.

--PHOTO OF POTENTIOMETER HERE

### What does this mean for us?
So for example... if the middle bit is spun all the way to the left a voltage of 0v may be passed 
through the middle pin. If spun all the way to the right maybe its 5v. We can then go
back and then solve for the voltage at any point.

Do you see where I'm going with this?

### How can we implement this with our servos?
In the turret, we have a 270 and a 180 Degree servo.
I have soldered an extra wire to both. Please see the photos below for where to solder your wire!

Please keep a few things in mind before you begin
- Keep the exposed copper portion on your wire very small. We do not want to bridge anything after closing the servo back up.
- These servos are very tiny, I suggest using helping hands. Amazon: "Soldering hands" or an actual person to help hold.

--PHOTOS OF BOTH 270 + 180 HERE

### What now?
Congrats! You have completed the arguably most skilled part of the build.
If you have purchased the same servos as me. You are done.

If not or if you are interested in how I got my magic numbers; there is still work to be done.

### Calculating our position
Power your servos with its rated voltage. After this use the demo_main program to set the servos to zero and max degree
measuring the voltage of the 4th wire at each value.

Single degree value = (max voltage-Min voltage)/degree

Take the single degree value for both X and Y and update the 'Receiver-Turret.ino' file.
Remember if you do this, re-flash your Arduino.