//Steven Naliwajka
//TF2 Turret Proj
//Code on the slave turret Componenet
//On An Aurduino UNO:
//See Attached Aurduino PNG for pinout


//Transmittal Code and implementation of NRF24L01
//based from 
/*
https://forum.arduino.cc/t/simple-nrf24l01-2-4ghz-transceiver-demo/405123
Robin2's
*/

//Libs for the NRF24L01
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include <Wire.h>

// *** YOU MUST UPDATE THIS VALUE IF DIFFERENT ***
int maxXDegree = 270;
int maxYDegree = 180;


//Single Degree Values for calculating Live Position Data from
//the X and Y Servos
float singleDegreeY;
float lowestrawY;
float singleDegreeX;
float lowestrawX;


//NRF24L01 Radio Pins
#define CE_PIN   9
#define CSN_PIN 10
//Servo Poteometer Analog feedback pins
int pos1 = A0;
int pos2 = A1;
//Feedback from hardware switch
int hardwareSwitch = 6;
//RelayControl
int servoState = 4;
int fireState = 5;
//wranglerstatus
int wranglerStatus = 2;

int listenpin = 7;
int broadcastpin = 8;
//Create Array to hold radio data
int myData [7] = { 0};

//Address of NRF24L01 Receiver.. Itself
const byte address[6] = "00001";
RF24 radio(CE_PIN, CSN_PIN);

struct DataPackage {
  byte firestate = 5;
    //0 (N), 1(F)
  byte movestate = 5;
    //0 (N), 1(R), 2(L), 3(U), 4(D)
  byte active = 1;
};

DataPackage wranglerData;

void setup() {

  //Start Serial
  Serial.begin(9600);
  //Init pins
  //pinMode(10, OUTPUT);
  pinMode(hardwareSwitch, INPUT_PULLUP);
  pinMode(servoState, OUTPUT);
  pinMode(fireState, OUTPUT);
  pinMode(wranglerStatus, OUTPUT);
  pinMode(listenpin, INPUT);
  pinMode(broadcastpin, OUTPUT);


  //Start NRF24L01
  radio.begin();
  //Begin listening for messages sent to the address
  radio.openReadingPipe(0, address);
  //Set Volume level.. I think this only affects broadcasting
  radio.setPALevel(RF24_PA_MIN);
  //Listen
  radio.startListening();

  digitalWrite(broadcastpin, LOW);
  //Set the Aurduino to be listening to I2C with the 'name':0x55
  Wire.begin(0x55);
  //If I2C request is made, call requestEvent method
  Wire.onRequest(requestEvent);

  //Wait till signal from master that is time for
  while(!digitalRead(broadcastpin)){
    //empty
  }
  Serial.println("Calibrating NOW");
  calibrateServoCordinates();
  digitalWrite(broadcastpin, HIGH);

}

void calibrateServoCordinates(){
  float tempX = analogRead(pos2);
  float tempY = analogRead(pos1);
  float lowX = 10000;
  float lowY = 10000;
  float highX = 0;
  float highY = 0;
  bool run = true;
  int counter = 0;
  while (run){
    tempY = analogRead(pos1);
    tempX = analogRead(pos2);
    if(lowX < tempX){
      lowX = tempX;
      counter = 0;
    } else if(highX > tempX){
      highX = tempX;
      counter = 0;
    } else{
      counter++;
    }

    if(lowY < tempY){
      lowY = tempY;
      counter = 0;
    } else if(highY > tempY){
      highY = tempY;
      counter = 0;
    } else{
      counter++;
    }

    if(counter <= 10){
      if(!digitalRead(broadcastpin)){
        run = false;
      }
    }
  }
  //Calculate the values
  lowestrawX = lowX;
  lowestrawY = lowY;
  singleDegreeY = ((highY-lowY)/maxYDegree);
  singleDegreeX = ((highX-lowX)/maxXDegree);

  Serial.print("singledegreeY :");
  Serial.println(singleDegreeY);

  Serial.print("singledegreeX :");
  Serial.println(singleDegreeX);
}


void loop() {
  //Updating the hardware relay to
  if(!digitalRead(hardwareSwitch)){
    digitalWrite(servoState, LOW);
    digitalWrite(fireState, LOW);
  }else{
    digitalWrite(servoState, HIGH);
    //PIN fireState is switch
    digitalWrite(fireState, HIGH);
  }
  //Testing
  //2 points of data to transfer, 0-270. Bits only handle up to 250. So there are going to be 4 bits.

  /*
  Serial.print("YPOS ");
  Serial.println(analogRead(pos1));
  Serial.print("XPOS ");
  Serial.println(analogRead(pos2));
  Serial.println("-------------------");
  delay(1000);
  */
  int yPos = (analogRead(pos1)-lowestrawY)/singleDegreeY; ///singleDegreeY;
  int xPos = (analogRead(pos2)-lowestrawX)/singleDegreeX; ///singleDegreeX;
  /*
  Serial.print("X Pos: ");
  Serial.print(xPos);
  Serial.print(" Y Pos: ");
  Serial.println(yPos);
  */
  if(xPos < 0){
    myData[0] = 0;
    myData[1] = 0;
  }else if (xPos >255){
    myData[1] = xPos-255;
    myData[0] = 255;
  }else{
    myData[0] = xPos;
    myData[1] = 0;
  }
  if (yPos < 0){
    myData[2] = 0;
    myData[3] = 0;
  }else if (yPos >255){
    myData[3] = yPos-255;
    myData[2] = 255;
  }else{
    myData[2] = yPos;
    myData[3] = 0;
  }
  //Configuring the NRF24L01
  //radio.startListening();

  if (radio.available()) {
    //Intake message, sets message = to received data
    radio.read(&wranglerData, sizeof(DataPackage));
    /*
    Serial.println(wranglerData.firestate);
    Serial.println(wranglerData.movestate);
    Serial.println("__________________");
    */
    //Moves message into an array
    myData[4] = wranglerData.firestate;
    myData[5] = wranglerData.movestate;
    myData[6] = 1;
    digitalWrite(wranglerStatus, HIGH);
    /*
    Serial.println(myData[4]);
    Serial.println(myData[5]);
    Serial.println("------");
    */
    delay(15);
  }else{
   myData[4] = 0;
   myData[5] = 0;
   myData[6] = 0;
   digitalWrite(wranglerStatus, LOW);
  }
  /*
  Serial.println(myData[4]);
  Serial.println(myData[5]);
  Serial.println("------");
  */
  //Close out of the radio
  //radio.stopListening();
}

void requestEvent(){
  /*
  // Used for debugging and seeing what data gets sent through I2C
  // I2C WILL NOT WORK IF THESE LINES ARE UNCOMMENTED!!!
  // ONLY WORKS IF wire.write(...s...) is the only code being executed in event
  // From what I understand, this is due to the I2C request timing out before
  // The calculations can be done. Only enough time to JUST send data.
  Serial.print("Y Pos: ");
  Serial.print(analogRead(pos1)/2.207407);
  Serial.print(" X Pos: ");
  Serial.println(analogRead(pos2)/3.1722222);
  byte* byteData = (byte*)myData;
  for (size_t i = 0; i < sizeof myData; i++) {
    Serial.print("Byte ");
    Serial.print(i);
    Serial.print(": ");
    Serial.println(byteData[i]); // Print each byte in hexadecimal format
  }
  */


  //Write data to I2C..
  Wire.write((byte *) myData, sizeof myData);
}