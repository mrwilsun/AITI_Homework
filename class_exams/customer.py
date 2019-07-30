from datetime import datetime
from datetime import timedelta

class Customer:
    def __init__(self,first_name,last_name,email,phone_number,twitter_handle,cars):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.phone_number=phone_number
        self.twitter_handle=twitter_handle
        self.cars=cars

    def wash_car(car):
        now = datetime.datetime.now()
        date=now.strftime("%d-%m-%Y")
        time_in=datetime.now.time()
        time_done=time_in+timedelta(minutes=20)
        