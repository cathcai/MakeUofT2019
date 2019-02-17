# SMS_Newsfeed
# using Coffee 'n Code Tutorial

import twilio

from twilio.rest import Client

account_sid = 'ACf1fe98543ca5b3b3839ff8722feedd5e'
auth_token = '8e62021cffc51059b66cc855656900a5'
client = Client(account_sid, auth_token)

#message = client.messages.create(to="+12048190137", from="+16476397556", body="This is the body text.")
#print(message.sid)
message = client.messages.create(
                              from_='+12048190137',
                              body='body',
                              to='+16476397556'
                          )

print(message.sid)
