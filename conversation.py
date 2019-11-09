from twilio.rest import Client

account_sid = 'AC3b9bda4723be316e90ed657a40130d5b'
auth_token = 'c826e7ec7ba59cea0025b8c1aca0621d'
client = Client(account_sid, auth_token)

conversation = client.conversations \
                     .conversations \
                     .create(friendly_name='My First Conversation')

print(conversation.sid)
