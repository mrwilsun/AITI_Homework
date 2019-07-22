def get_groceries():
    print("Welcome, please follow the prompts, press x to exit >>>")
    grocery=""
    list=[]
    while grocery !="x":
        grocery = input("Please enter an item >>")
        if grocery != "x":
            list.append(grocery)
        print(f"Your current list is {list}")
    print(f"Your final list is {list}")

get_groceries()