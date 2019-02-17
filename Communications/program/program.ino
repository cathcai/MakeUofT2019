 /*the sonar will watch the door. If it detects something, the 
 * bus' transceiver will be activated and search for an emission.
 */

#include <SPI.h>
#include "RF24.h"

//transceiver
RF24 radio(7, 8);

//sonar
const int trigPin = 3;
const int echoPin = 4;

//transceiver
char number[20] = "";

//sonar
long duration;
double distance;
double previousDistance = 120;
double debounceDistance;
unsigned long lastDebounceTime = 0;
unsigned long debounceDelay = 50;

int busDoorLength = 120;

const byte address[6] = "00001";

void setup()
{
  //sonar
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  Serial.begin(9600);
  delay(1000);

  //transceiver
  radio.begin();
  radio.setPALevel(RF24_PA_MIN);
  radio.setDataRate(RF24_2MBPS);
  radio.setChannel(124);
  radio.openReadingPipe(0, address);
  radio.startListening();
}

void loop()
{
  //this assumes the sonar is placed on the door, perpendicular
  //to passengers.
  passiveSonarDetection();
  delay(10);
}

void passiveSonarDetection()
{
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);

  distance = duration*0.034/2;
  
  if(abs(previousDistance - distance) > 20)
  {
    lastDebounceTime = millis();
    debounceDistance = distance;
  }

  if(((millis() - lastDebounceTime) > 50) && (abs(previousDistance - distance)<20))
  {
    if(distance < (busDoorLength - 5))
    {
      //leaving room for error
      activateTransceiver();
    } 
  }
  previousDistance = distance;
}

void activateTransceiver()
{
  unsigned long phone1;
  unsigned long phone2;
  bool success = false;
  long currentTime = millis();

  int counter = 0;
  while(((millis() - currentTime) < 3000)){
    if(radio.available())
    {
      radio.read(&number, sizeof(number));
      success = true;
    }
  }
  if(success){
    Serial.println(number);
  }
}
