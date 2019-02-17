# RideOn

## MakeUofT 2019

### Our Project
Transportation passes are another addition to the many devices, apps, and cards that people hold on to on a daily basis.
RideOn strives to make this process paper-free, card-free, and hands-free by integrating this technology into our phones.

#### How it works
A person with their phone can board any form of transportation, for example, a bus, without the need to take out a transportation pass, card, nor cash. This occurs due to a two-factor authentication service that detects the individual physically boarding the bus and an RFID transceiver that receives ID and payment data automatically sent from their phone. This data is then sent to a database that records the information, allowing the transaction to take place. Once the transaction has been completed, the individual will receive a message in the form of an SMS text confirming the time of purchase, stop location, and payment amount.

As a prototype, this system functions using Arduino Wireless Single-directional Communications between two RFID transceivers. T



#### Hardware
* Arduino Uno (2)
* nRF24 Transceiver (2)
* capacitors 100 microFarads (2)
* breadboard (2)
* Ultrasonic Distance Sensor HC-SR04 (1)

#### Software
* Python 3
* C
* Twilio Cloud Communications
* Arduino IDE
* Realterm
* MongoDB


### Next Steps






### Past Notes
- Communication between the Arduino Uno and the Qualcomm Dragonboard
- Simulate a phone with RFID technology
- Automated transactions for public transportation and for other applications
- Extra: Add twilio to send phone SMS to confirm transaction

Communication Method:
- Active RFID

Arduino Uno: simulate the components on a bus
Qualcomm Dragonboard: simulate a phone using Andriod OS 5.1

Uno 1: Motion Sensor and RFID transceiver
Uno 2: Passport


public key/id (transmitted to the bus - always transmitting the RFID)
        email(for charging), phone #(to send SMS), bus only cares about the public key/id (checksum to see if actual Id requested is authenticated)
        this is sent to the bus
  this is stored and sent to the system as a transaction request
    there is a database of people using the service - asks the host system (TTC, YRT) to ask to confirm the information


Two factor authentication
  the sonar


pgp - potential encryption
