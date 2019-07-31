import customer
import car
import attendant

Yorick=customer.Customer("Yorick","Wilson","wstellcie@gmail.com","0243004589","@hello_world")

Car1=car.Car("GR-0555-1516",Yorick)
print(Yorick.first_name)
print(Car1.__dict__)
Car1.show_car_info()

Yorick.add_car(Car1)
Yorick.show_time() 

attendant1=attendant.Attendant("Emmanuel Agyemfra")
message1=attendant.Message("Please your car has been washed and is ready","sms",Yorick)
# attendant.Attendant.send_sms(message1)

attendant.Attendant.send_email(message1)