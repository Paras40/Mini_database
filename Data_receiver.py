class Info():
    
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    def create_file(self):
        with open ("data.txt","a") as file:
            file.write(f"Hey, I am {self.name} of {self.age} and my contact is {self.phone}.\n")


name = input("Enter your name : ").strip()
age = input("Enter your age : ").strip()
phone = input("Enter your mobile number : ").strip()

obj1 = Info(name, age, phone)
obj1.create_file()

print("Thanks! your information has been saved.")