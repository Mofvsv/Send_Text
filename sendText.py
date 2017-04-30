from twilio.rest import TwilioRestClient

# Your Account SID from twilio.com/console
account_sid = "ACcec3737e92b8193a8142ada1da63fc3f"
# Your Auth Token from twilio.com/console
auth_token  = "528145bdb27e233912c407c4c27c31a9"

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    to="+16158702675", 
    from_="+12062022102",
    body="Hello from Python!")

print(message.sid)
