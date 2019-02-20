
import os
import time
import datetime
import twilio
from twilio.rest import Client


#twilio API
account_sid = 'place account sid here'
auth_token = 'place auth token here'
client = Client(account_sid, auth_token)


# this section can be ignored
numbersList = []
def Remove(duplicate):
    numbersList = []
    for num in duplicate:
        if num not in numbersList:
            numbersList.append(num)
    return numbersList

#this will continously loop and open the txt file
while True:
    #named the txt file number.txt
    f = open("number.txt", "r")

    #will count the total number of lines in the txt file
    listOfLines = f.readlines()
    f.close()

    #opens the file and iterates through each of the lines
    f = open("number.txt", "r")
    for line in listOfLines:
        linesplit = line.split("\n")
        phoneNumber = str(linesplit[0])
        if phoneNumber not in numbersList:
            numbersList.append(phoneNumber)

            #creates a date/time stamp
            ts = time.time()
            dt = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            bodystring = "{\n \"timestamp\": " + "\"" + str(dt) + "\"," + "\n\"number\"" + ": \"" + str(phoneNumber) + "\"\n}"
            print(str(dt) + " " + phoneNumber)

            #this sends a SMS to the user
            message = client.messages.create(
                                          from_='your number',
                                          body= str(dt) + " " + 'You have been charged $3.25 at St. Georges Bus Station. Thank you for riding with the TTC',
                                          to=phoneNumber
                                      )

            #this sends an SMS to the database (nodejs) and stores the data on that end
            print(message.sid)
            message = client.messages.create(
                                        from_='your number',
                                        body= '%s' % bodystring,
                                        to='server n umber'
                                    )

            print(message.sid)

        #file must be closed to receive updates in next txt file update
        f.close()
#    f = open("number.txt","w")
#    f.close()
#    os.remove("number.txt")
