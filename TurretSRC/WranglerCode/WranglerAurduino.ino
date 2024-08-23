//Steven Naliwajka
//TF2 Turrent Proj
//Code on the Handheld Wrangler Componenet
//On An Aurduino UNO:
//For


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
#define CE_PIN   9
#define CSN_PIN 10

//Address of NRF24L01 Receiver
const byte address[6] = "00001";
RF24 radio(CE_PIN, CSN_PIN);

struct DataPackage {
  byte firestate = 0;
    //0 (N), 1(F)
  byte movestate = 0;
    //0 (N), 1(R), 2(L), 3(U), 4(D)
  byte active = 1;
};

DataPackage wranglerData;

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
  //Logic for message
  if(!digitalRead(fire)){
    //F
    wranglerData.firestate = 1;
  }else{
    wranglerData.firestate = 0;
  }
  if(!digitalRead(right)){
    //Serial.println("right");
    wranglerData.movestate = 1;
  }else if(!digitalRead(left)){
    //Serial.println("left");
    wranglerData.movestate = 2;
  }else if(!digitalRead(up)){
    //Serial.println("up");
    wranglerData.movestate = 3;
  }else if(!digitalRead(down)){
    //Serial.println("down");
    wranglerData.movestate = 4;
  }else{
    wranglerData.movestate = 0;
  }

  /*
    if(!digitalRead(fire)){
    message = "F";          //Fire
  }else{
    message = "N";
  }
  if(!digitalRead(right)){
    //Serial.println("right");
    message = message +"R";          //Right
  }else if(!digitalRead(left)){
    //Serial.println("left");
    message = message +"L";          //Left
  }else if(!digitalRead(up)){
    //Serial.println("up");
    message = message +"U";          //Up
  }else if(!digitalRead(down)){
    //Serial.println("down");
    message = message +"D";          //Down
  }
  */

  //Broadcast data
  radio.write(&wranglerData, sizeof(DataPackage));
  //Print data to serial for easy testing
  /*
  Serial.println(wranglerData.firestate);
  Serial.println(wranglerData.movestate);
  Serial.println("_____________________");
  */
  //5ms delay to allow for hardware to process
  delay(5);
}