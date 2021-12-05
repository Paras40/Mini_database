import json
import os
print("==========WELCOME TO JSON FORMATTER================")
print("-------------Press 'e' to exit--------------")
class writing():
	def __init__(self,id,firstname,lastname,city):
		self.id = id
		self.firstname = firstname
		self.lastname = lastname
		self.city = city
	def write(self):
		with open ("mydata.json","a") as file:
			file.write(f'''
	"id": "{self.id}",
	"firstname": "{self.firstname}",
	"lastname": "{self.lastname}",
	"city": "{self.city}"
	''')
def read():
	with open("mydata.json", "r") as read_file:
		obj = json.load(read_file)
		pretty_json = json.dumps(obj, indent=4)
		return(pretty_json)
def drop_last_character():
	with open('mydata.json', 'rb+') as filehandle:
		filehandle.seek(-1, os.SEEK_END)
		filehandle.truncate()
def add_main_characters():
	with open('mydata.json', 'a') as file:
		file.write(",{")
def close_json():
	with open('mydata.json', 'a') as file:
		file.write("}]")	

pwd = ""

while pwd != "paras":

	pwd = input("Enter the password : ")

	if pwd == "paras":
		print("Successful!")
		user = 'r'
		while user == "r" or user == "w":
			user = input("What do you wanna do now?\nFor 'read' Press 'r'\nFor 'write' Press 'w'\nFor 'exit' Press 'e'\n")
			if user == 'r':
				print(f"==========Here is all the data==========\n{read()}")
			elif user == 'w':
				id = input("Enter your id : ")
				firstname = input("Enter your first name : ").strip().title()
				lastname = input("Enter your last name : ").strip().title()
				city = input("Enter your city : ").strip().title()
				w1 = writing(id, firstname, lastname, city)
				drop_last_character()
				add_main_characters()
				w1.write()
				close_json()
				print("Thanks!! your information has been saved :-)")
			elif user.lower() == "e":
				print("Have a good day\nThanks for using json-formatter")
				break
			else:
				print("We didn't understand your query.")
				user = 'r'
			again = input("Do you want to use json-formatter again?\nPress 'Enter' to continue or 'e' to exit\n")
			if again.lower() == "e":
				print("Have a good day\nThanks for using json-formatter")
				break
	elif pwd.lower() == "e":
		print("It seems you don't know the password.\nYou can check the password in the file named 'password.txt'")
		break
	else:
		print("Sorry! try again")
