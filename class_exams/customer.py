from datetime import datetime
from datetime import timedelta

class Customer:
    def __init__(self,first_name,last_name,email,phone_number,twitter_handle):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.phone_number=phone_number
        self.twitter_handle=twitter_handle
        self.cars_list=[]
        self.alert_time=""

    def wash_car(self):
        now = datetime.datetime.now()
        date=now.strftime("%d-%m-%Y")
        time_in=datetime.now.time()
        time_done=time_in+timedelta(minutes=20)
        self.alert_time=time_done+timedelta(hours=1)
        add_car(customer,car)

    def add_car(self,car):
        for i in self.cars_list:
            if i==car:
                break
                self.cars_list.append(car)
        
    def show_time(self):
        print("the alert time is " + self.alert_time)
