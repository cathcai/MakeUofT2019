
import os
import time
import datetime
import twilio
from twilio.rest import Client


account_sid = 'ACf1fe98543ca5b3b3839ff8722feedd5e'
auth_token = '8e62021cffc51059b66cc855656900a5'
client = Client(account_sid, auth_token)



numbersList = []
def Remove(duplicate):
    numbersList = []
    for num in duplicate:
        if num not in numbersList:
            numbersList.append(num)
    return numbersList

#while True:
#open the .txt file

f = open("number.txt", "r")
#while True:
listOfLines = f.readlines()
f.close()

f = open("number.txt", "r")
for line in listOfLines:
    linesplit = line.split("\n")
    phoneNumber = "+1" + str(linesplit[0])
    if phoneNumber not in numbersList:
        numbersList.append(phoneNumber)

        ts = time.time()
        dt = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

        print(str(dt) + " " + phoneNumber)
        #message = client.messages.create(
        #                              from_='+12048190137',
        #                              body= str(dt) + " " + 'You have been charged $3.25 at St. Georges Bus Station. Thank you for riding with the TTC',
        #                              to='+16476397556'
        #                          )

        #print(message.sid)



    f.close()

#    os.remove("number.txt")`
