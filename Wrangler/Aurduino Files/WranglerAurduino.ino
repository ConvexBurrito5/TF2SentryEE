//Steven Naliwajka
//TF2 Turrent Proj
//Code on the Handheld Wrangler Componenet
//On An Aurduino UNO:
//Pinout..


//Transmittal Code and implementation of NRF24L01
//based from 
/*
Dejan Nedelkovski, www.HowToMechatronics.com
Library: TMRh20/RF24, https://github.com/tmrh20/RF24/
*/

//Libs for the NRF24L01
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
//Var for All of the GPIO pins.. 
int right = 5;
int left = 4;
int up = 3;
int down = 6;
int fire = 2;
//int ctrlSwitch = 9;

//NRF24L01 Radio Pins
RF24 radio(7, 8); // CE, CSN

//Address of NRF24L01 Receiver
const byte address[6] = "00001";


void setup() {
  // put your setup code here, to run once:

  //Init Pins to read HIGH untill they are connected to ground..
    pinMode(right, INPUT_PULLUP);
    pinMode(left, INPUT_PULLUP);
    pinMode(up, INPUT_PULLUP);
    pinMode(down, INPUT_PULLUP);
    pinMode(fire, INPUT_PULLUP);
    //pinMode(ctrlSwitch, INPUT);

    //Start Serial..
    Serial.begin(9600);
    //Serial.println("HI111!!!");

    //Start NRF24L01
    radio.begin();
    //Start writing to stored address
    radio.openWritingPipe(address);
    //Set 'volume' level
    radio.setPALevel(RF24_PA_MIN);
    //No need to take input
    radio.stopListening();
}

void loop() {     
  //Logic for the command to be sent over NRF24L01
  char message = 'N';
       //Nothing
  //if(digitalRead(ctrlSwitch)){
  if(!digitalRead(fire)){
    //Serial.println("Fire");
    message = 'F';          //Fire
  }else{
    message = '';
  }
  if(!digitalRead(right)){
    //Serial.println("right");
    message = message +'R';          //Right
  }else if(!digitalRead(left)){
    //Serial.println("left");
    message = message +'L';          //Left
  }else if(!digitalRead(up)){
    //Serial.println("up");
    message = message +'U';          //Up
  }else if(!digitalRead(down)){
    //Serial.println("down");
    message = message +'D';          //Down
  }

  radio.write(&message, sizeof(message));
  Serial.println(message);
  //}
  

  delay(5);
}
