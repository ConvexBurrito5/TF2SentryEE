# Instructions - Laptop + FT232H:
Now that you have purchased all the goodies in the prior step, manufacturing can begin.

### 1. Begin building the circuit
Using the below media, build your circuit ignoring the 'POT data' wire between the servos and the aurduino.
- Picture of turret circuitry.png
- Picture of turret code.png

DO NOT! power your circuit before verifying that everything is
connected properly. When building this for a second time I was lazy and ruined a 4 relay and one
of the NRF24L01+ transmitters.

Flash your Aurduino using the provided 'Receiver-Turret.ino' file.

### 2. Setup your linux instance
Inside your linux machine, open terminal and paste
```
git clone --recursive 
https://github.com/Maiikiru/TF2SentrySource.git "SentryGun"
cd SentryGun
bash "RequirementsFiles/install_linux.bash"
```
This makes everything super easy. Installs 

### 3. Setup your Servos
One this is done, go to 

[PoteometerInstructions.md](Documentation\1-TurretGuts\PoteometerInstructions.md) 

and follow the instructions on how to modify your 2 servos to give live position data.

After, plug in your 4th wire to the Aurduino a0/a1 slot.

### 4. Testing
If everything was done correctly, you should be able to run 

If this executes correctly you can then move onto 2-WranglerGuts.