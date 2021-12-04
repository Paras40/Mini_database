class Person():
	def __init__(self,firstname,lastname,city):
		self.firstname = firstname
		self.lastname = lastname
		self.city = city
	def template(self):
		with open ("data.txt","a") as file:
			file.write(f"Hey, I am {self.firstname} {self.lastname} from {self.city}.\n")

pwd = ""

while pwd != "Paras@123":
	
	pwd = input("Enter the password : ")

	if pwd == "Paras@123":
		print("Successful!")
		firstname = input("Enter your first name : ").strip().title()
		lastname = input("Enter your last name : ").strip().title()
		city = input("Enter your city : ").strip().title()

		p1 = Person(firstname, lastname, city)
		p1.template()
		print("Thanks!! your info has been saved :-)")

	else:
		print("Sorry! try again")
