from datetime import datetime
from datetime import timedelta
import send_sms
import send_email

class Attendant:
    def __init__(self,name):
        self.name=name

    def wash_car(self,car):
        pass

    def send_sms(message):
        text = send_sms.client.messages \
                    .create(
                        body=message.text,
                        from_='+18587990296',
                        to=f'+233{message.recepient_number}'
                    )
        print(f'Message: \"{text._properties["body"]}\" has been sent to: {text._properties["to"]}')

    def send_email(message):
        send_email.send_email("AITI_KACE Car wash",message.text,message.recepient_email)

class Message:
    def __init__(self,text,category,customer):
        self.text=text
        self.category=category
        self.recepient_number=customer.phone_number
        self.recepient_handle=customer.twitter_handle
        self.recepient_email=customer.email
        
    def send_sms(self):
        pass        

