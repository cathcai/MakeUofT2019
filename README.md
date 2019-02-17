# MakeUofT2019

Idea:
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
