# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC09e88c16f9f40f21e7eb6369e5cb132e'
auth_token = '2c737fa6ccb9b85b8c6c14619088c40c'
client = Client(account_sid, auth_token)

# def send_sms(message):
#     message = client.messages \
#                     .create(
#                         body=self.text,
#                         from_='+18587990296',
#                         to=f'+233{self.recepient_number}'
#                     )
#     print(f"Message: {self.text} . Sent to: {self.recepient_number}")
