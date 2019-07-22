def get_input():
    print("Hello, let's tell a story about yourself.\n Please follow the prompts: ")
    name=input("Tell us your name >>>")
    gender=input("What is your gender? >>>")
    age=input("How old are you? >>>")
    location=input("Where do you live? >>>")
    occupation=input("What do you want to be in future? >>>")
    school=input("Which school do you attend? >>>")
    details=[name,age,location,school,gender,occupation]   
    return details
    

def make_sentence(name,age,location,school,gender,occupation):
    print(f"Hello, welcome to my story./n ")
    print(f"My name is {name}. I am a {gender}, {age} years of age. I live at {location}. I want to be a {occupation} in future. That\'s why i\'m attending {school}. That's where I fell in love with Python programming.")


details=get_input()
make_sentence(*details)