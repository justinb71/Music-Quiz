
from functools import partial
from tkinter import *

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return

#window
SigninWindow = Tk()  
#tkWindow.geometry('400x150')  
SigninWindow.title('Signin')

#username label and text entry box
usernameLabel = Label(SigninWindow, text="Username").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(SigninWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(SigninWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(SigninWindow, textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(SigninWindow, text="Login", command=validateLogin).grid(row=4, column=0,sticky=N)  

SigninWindow.mainloop()