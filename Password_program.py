from tkinter import *
import os
import sqlite3

root = Tk()
root.title("QWRTY")

def Generate_pass():
	message = ""
	
	try:
		#Generating password
		passw = str(os.urandom(12))

		#Connecting to the database
		conn = sqlite3.connect('Passwords.db')
		c = conn.cursor()

		#Creating the database
		c.execute('CREATE TABLE IF NOT EXISTS Passwords(Password TEXT, Description TEXT)')
	
		#Add password and description to the database
		c.execute('INSERT INTO Passwords VALUES(?, ?)',
			(passw, Pass_desc_box.get()))
		conn.commit()

		#Closing connection to the database
		c.close()
		conn.close()

		message = "Password generated sucessfully!"
	
	except:
		message = "Password not generated sucessfully!"

	#label to display message
	Message_label = Label(root, text = message, fg = 'yellow', bg = 'black')
	#Displaying the label
	Message_label.grid(row = 1, column = 2)

def Get_pass():
	#Connecting to the database
	conn = sqlite3.connect('Passwords.db')
	c = conn.cursor()

	#Selecting passwords to display
	data = c.execute('SELECT Password, Description FROM Passwords')

	#Saving passwords in a variable
	line = ""
	for column in data:
		line += "Password: " + column[0] + "\n" + "Description: " + column[1] + "\n\n"

	#Closing database connection
	c.close()
	conn.close()

	#Label to display message
	pass_display_label = Label(root, text = line, fg = "yellow", bg = "black")
	#Displayng the label
	pass_display_label.grid(row = 2, column = 0)

#Creating password description textbox
Pass_desc_box = Entry(root)
Pass_desc_box.insert(0,"Enter password description")

#Creating buttons
generate_button = Button(root, command = Generate_pass, text = 'Generate Password', fg = 'yellow', bg = 'black', height = 8, width = 20)
get_pass_button = Button(root, command = Get_pass, text = 'Get Passwords', fg = 'yellow', bg = 'black', height = 8, width = 20)

#Displaying buttons
get_pass_button.grid(row = 1, column = 1)
generate_button.grid(row = 1, column = 0)

#Displaying textbox
Pass_desc_box.grid(row = 0, column = 0)

root.mainloop()