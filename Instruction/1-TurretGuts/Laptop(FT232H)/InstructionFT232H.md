# Instructions - Laptop + FT232H:
Now that you have purchased all the goodies in the prior step, manufacturing can begin.

### Begin building the circuit
Using the below media, build your circuit ignoring the 'POT data' wire between the servos and the aurduino.
- Picture of turret circuitry.png
- Picture of turret code.png

DO NOT! power your circuit before verifying that everything is
connected properly. When building this for a second time I was lazy and ruined a 4 relay and one
of the NRF24L01+ transmitters.

Flash your Aurduino using the provided 'Receiver-Turret.ino' file.

### Setup your linux instance
Go to 

'/Instruction/1-TurrentGuts/Requirements/VanillaReqs/readme.md' 

and follow that.

### Setup your Servos
One this is done, go to 

'/Instruction/1-TurrentGuts/Universal/PoteometerInstructions.md' 

and follow that. 

After, plug in your 4th wire to the Aurduino a0/a1 slot.

### Testing
If everything was done correctly, you should be able to run 'IFORGOTTHERUNSCRIPTLOL'

If this executes correctly you can then move onto 2-WranglerGuts.