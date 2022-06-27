import mysql.connector
import sys

class DatabaseHelper:
    def __init__(self):
        try:
            self.connection =  mysql.connector.connect(host="localhost",user="root",password="",database="crud-app-db")

            #This cursor object is used to interact with data in the database
            self.myCursor = self.connection.cursor()
        except:
            print("Could not connect to Database")
            sys.exit(0)
        else:
            print("Connected to Database crud-app-db ")

    def Register(self,name,email,password):
        try:
            self.myCursor.execute(f"""INSERT INTO `users` (`id`, `name`, `email`, `password`) VALUES (NULL, '{name}', '{email}', '{password}');""")
            self.connection.commit()
        except:
            return -1
        else:
            return 1
    
    def SearchForLoginCredentials(self,email,password):
        self.myCursor.execute(f"""SELECT * fROM users WHERE email LIKE '{email}' AND password LIKE '{password}' """)
        fetchedData = self.myCursor.fetchall()
        return fetchedData
    