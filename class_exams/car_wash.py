import customer
import car

Customer1=customer.Customer("Yorick","Wilson","yw@gmail.com","0244419419","@hello_world")

Car1=car.Car("GR-0555-1516",Customer1)
print(Customer1.first_name)
print(Car1.__dict__)
Car1.show_car_info()

Customer1.add_car(Car1)
Customer1.show_time()