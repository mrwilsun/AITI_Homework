class Car:
    def __init__(self, lincense_num,costumer):
        self.lincense_num=lincense_num
        self.owner_name= costumer.first_name +" "  + costumer.last_name

    def show_car_info(self):
        print(self.owner_name+" is the owner of car number "+self.lincense_num)
        
        