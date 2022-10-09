
from cProfile import label
import random 
from tkinter import *
import json 
import time
from functools import partial


def validateLogin(username, password):

    password = password.get()
    username = username.get()

    if username == "John" and password == "1234":
        return True
    elif username == "John" and password != "1234":
        validationLabel.text = "Incorrect Password"
    elif password == "1234" and username != "John":
        validationLabel.text=text="Incorrect Username"
    else:
        validationLabel.text="Incorrect Login"
    return



	

SigninWindow = Tk()
SigninWindow.title('Signin')

validationLabel = Label(SigninWindow,text="").grid(row=0,column=0)
validateLogin.config(text="Hello")

usernameLabel = Label(SigninWindow, text="User Name").grid(row=1, column=0)

username = StringVar()
usernameEntry = Entry(SigninWindow, textvariable=username).grid(row=1, column=1)  

#password label and password entry box
passwordLabel = Label(SigninWindow,text="Password").grid(row=2, column=0)  
password = StringVar()
passwordEntry = Entry(SigninWindow, textvariable=password, show='*').grid(row=2, column=1)  

validateLogin = partial(validateLogin, username, password)

loginButton = Button(SigninWindow, text="Login", command=validateLogin).grid(row=4, column=0,sticky=N)  


SigninWindow.mainloop()