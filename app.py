

import sys
from databasehelper import DatabaseHelper


class RegistrationSystem:
    def __init__(self):
    #Once the object of RegistrationSystem is created then the init function is called automatically.

        #Make connection to database
        self.DB = DatabaseHelper()
        #Shows menu
        self.Menu() 

    def Menu(self):
        userInput = input("Enter 1 to register\nEnter 2 to login\nEnter anything else to exit\n")
        if userInput=="1":
            self.register()
        elif userInput=="2":
            self.Login()
        else:
            sys.exit(1000)
        
    def register(self):
        name = input("Enter name__")
        email = input("Enter email__")
        password = input("Enter password__")
        response = self.DB.Register(name,email,password)
        if response:
            print("Registration Sucessful\n")
            print("You can now login!")
            self.Login()
        else:
            print("Registration Unsucessful")
            self.register()

    def Login(self):
        email = input("Enter email__")
        password = input("Enter password__")
        data = self.DB.SearchForLoginCredentials(email,password)
        if len(data)==0:
            print("Incorrect email/password")
            self.Login()
        else:
            print(f"Hello {data[0][1]}, you're logged in!")

obj1 = RegistrationSystem()
