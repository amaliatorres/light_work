from twilio.rest import Client
# Download the Python helper library from twilio.com/docs/python/install
import os
account_sid = 'AC97f210240f46bdae5059ba499df3a98a'
auth_token = 'adf108baa898bf54178b59167700fd05'
client = Client(account_sid, auth_token)

conversation = client.conversations \
                     .conversations('CHa8655591d89941179d4e60ab4e5d29fe') \
                     .participants \
                     .create(
         messaging_binding_address='<+18455488520>',
         messaging_binding_proxy_address='<+18452092205>'
     )

print(participant.sid)


# IS915b6fb097c44759a40b3675c7eefb96
# CHa8655591d89941179d4e60ab4e5d29fe
