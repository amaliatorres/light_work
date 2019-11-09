from twilio.rest import Client

client = Client(account_sid, auth_token)

conversation = client.conversations \
                     .conversations \
                     .create(friendly_name='My First Conversation')

print(conversation.sid)
