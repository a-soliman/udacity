from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC7ddfb58ef87318e44389a783b6359a77"
# Your Auth Token from twilio.com/console
auth_token  = "884936f797b39ae23847d636d4be69f2"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+14152614213", 
    from_="+14159367747",
    body="Hello from Python!")

print(message.sid)