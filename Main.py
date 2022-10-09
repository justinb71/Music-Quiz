# Importing libraries

import random 
from tkinter import *
import tkinter
from tkinter import messagebox
from turtle import screensize, window_height
from functools import partial
import json 
import time


#Asigning global variables

signedIn = False
signinTries = 0
score = 0
tries = 0
end = False
start = False
seventiesFinished = False
eightiesFinished = False
songInformation = []


#Login validation function
def validateLogin(username, password):
    global signinTries
    global signedIn

    password = password.get()
    username = username.get()
    if signinTries <3:

        if username == "John" and password == "1234":
            signedIn = True
            SigninWindow.destroy()

        elif username == "John" and password != "1234":
            validationLabel.configure(text = "Incorrect Password")

        elif password == "1234" and username != "John":
            validationLabel.configure(text="Incorrect Username")

        else:
            validationLabel.configure(text="Incorrect Login")
        signinTries = signinTries + 1

    else:
        validationLabel.configure(text="Too many Attempts")
        SigninWindow.update()
        time.sleep(3)
        SigninWindow.destroy()

    return



	
#Sign in window
SigninWindow = Tk()
SigninWindow.title('Signin')

validationLabel = Label(SigninWindow,text="",fg="Red")
validationLabel.grid(row=0,column=1,sticky=N)


usernameLabel = Label(SigninWindow, text="User Name").grid(row=1, column=0)

username = StringVar()
usernameEntry = Entry(SigninWindow, textvariable=username)
usernameEntry.grid(row=1, column=1)  

#password label and password entry box
passwordLabel = Label(SigninWindow,text="Password")
passwordLabel.grid(row=2, column=0)  
password = StringVar()

passwordEntry = Entry(SigninWindow, textvariable=password, show='*')
passwordEntry.grid(row=2, column=1)  

validateLogin = partial(validateLogin, username, password)

loginButton = Button(SigninWindow, text="Login", command=validateLogin)
loginButton.grid(row=4, column=0,sticky=N) 

while signedIn  == False:
    SigninWindow.update()



#Initiate the window

window = Tk()
window.title("Music Quiz")
window.config(bg="white")
window.geometry("355x555")
window.resizable(False,False)

#Creates the title for the window
title = Label(window, text = "Music Quiz",height =1,background="white",font=SOLID)
title.grid(column=0,row=0,padx=10,sticky=N)


#Creates the Score box
scoreLabel = Label(window,text=("Score:"+str(score)),height =1,background="white",font=SOLID)
scoreLabel.grid(column=0,row=0,sticky=W)


#Creates the tries box
triesLabel = Label(window,text=("Tries:"+str(tries)+"      "),height =1,background="white",font=SOLID)
triesLabel.grid(column=0,row=0,sticky=E)


#Creates a bar between the results box and everything above
spacer = Frame(window,height = 4,width = "360",border=0,background="light grey")
spacer.grid(row=1,column=0)


#Creates the output box
resultsBox = Text(window,height = 28,width = "40",font=("Arial",12),background="#e8e8f0",border=0)
resultsBox.grid(row=2,column=0)
resultsBox.insert(INSERT,"\n")
resultsBox.config(state='disabled')


#Creates the guess entry box
entryBox = Entry(window, width = "60")
entryBox.grid(row=3,column=0)



#Loads all the songs into data from the json file
data = json.load(open("List.json"))

#Loads the catagories into variables from the json file
seventies = data["70s"]
eighties = data["80s"]




#Function that leaves the text only with letters and no spaces
def unformat(text):
    
    string1 = text.lstrip("()")
    string2 = string1.lstrip("'")
    string3 = string2.split("'")
    string4 = ("".join(string3)).split()
    string5 = "".join(string4)
    string6 = string5.lower()

    return string6

    
#Add text to the results box function
def addText(text):
    resultsBox.config(state='normal')
    resultsBox.insert(INSERT,text)
    resultsBox.see(END)
    resultsBox.config(state='disabled')



#Linear Search function
def linearSearch(list,item):

    for i in list:

        if item == i:
            return True
    return False

#A list that holds the values of songs that have already been used
usedNumbers =[]

#Afunction that gets a random song from the json file
def getRandomSong(category):

    

    randomNumber = random.randint(0,9)

    #This checks if the random number has been used before
    contains = linearSearch(usedNumbers,randomNumber)
    

    #If it has then pick a new number and check again
    while contains == True:

        randomNumber = random.randint(0,9)
        contains = linearSearch(usedNumbers,randomNumber)
    

    #Grabs the songs data
    currentSong = category[randomNumber]

    #Grabs the song from the list
    name = currentSong["Title"]
    hint = currentSong["Hint"]
    Artist = currentSong["Artist"]

    #Adds the random number to the list of used numbers
    usedNumbers.append(randomNumber)
    #Returns the name, hint and artist of that song in an array
    return name,hint,Artist


#Function that displays the author and hint to the screen
def HintAndAuthor():


    #This allows the variables to be eddited in the function
    global seventiesFinished
    global eightiesFinished
    global end

    #this if statement determines whether a message saying the end of catagory should be displayed
    if len(usedNumbers) == 10 and  seventiesFinished != True:
        addText("-----------------SEVENTIES FINISHED-------------------\n\n")
        usedNumbers.clear()
        seventiesFinished = True
    elif len(usedNumbers) == 10 and  eightiesFinished != True:
        addText("-----------------EIGHTIES FINISHED-------------------\n\n")
        usedNumbers.clear()
        eightiesFinished = True

        end = True
        addText("---------------------------Quiz Over------------------------------\n")
        addText("Your Score Is: "+str(score))
        

    #The if statement determines which catagory should the song be picked from
    if seventiesFinished == False:

        #Displays the hint and Artist to the screen
        songInformation = getRandomSong(seventies)
        songName = songInformation[0]
        hint = songInformation[1]
        artist = songInformation[2]

        addText("Artist: "+ artist+ "\n")
        addText("Your Hint Is:\n"+hint+ "\n\n")

    elif seventiesFinished == True and eightiesFinished != True:
        
        #Displays the hint and Artist to the screen
        songInformation = getRandomSong(eighties)
        songName = songInformation[0]
        hint = songInformation[1]
        artist = songInformation[2]

        addText("Artist: "+ artist+ "\n")
        addText("Your Hint Is:\n"+hint+ "\n\n")
    
    
    #This returns the random songs information 
    return songInformation   


def GuessingSystem():

    #This allows the variables to be eddited in the function
    global score
    global songInformation
    global tries
    global end 

    #if the game is not over do this else do nothing
    if end == False and start == True:

        #Gets all the required song information
        songName = songInformation[0]
        resultsBox.config(state='normal')
        guess = entryBox.get()
        strippedGuess = guess.lstrip("!£$%^&*()_+-=#~:;@<>?[]{}")

        entryBox.delete(0,END)

        #This validates the users input
        if guess.isspace():
            
            messagebox.showerror("Error","INVALID INPUT")
        elif strippedGuess:
            
            addText("Guess: " + strippedGuess + "\n")

    
            #This removes any unnecessary characters from the input and name of song
            unformatedGuess = unformat(guess)
            unformatedNameOfSong = unformat(songName)
        
            #If the input maches the name then they get points or the game ends
            if unformatedGuess == unformatedNameOfSong:
                
            

                if tries == 0:
                    score = score + 3
                elif tries == 1:
                    score = score + 1


                scoreLabel.configure(text=("Score:"+str(score)))
                addText("Correct\n\n")
                songInformation = HintAndAuthor()

                tries = 0
                triesLabel.configure(text="Tries:"+str(tries)+"      ")
                
            else:
                if tries <=0:
                    tries = tries + 1
                    addText("Incorrect\n\n")
                    triesLabel.configure(text="Tries:"+str(tries)+"      ")
                else:
                    addText("---------------------------Quiz Over------------------------------\n")
                    addText("Your Score Is: "+str(score))
                    end = True
                    tries = tries + 1
        
#Function that handles the start
def startQuiz():

    global songInformation
    global start

    input = entryBox.get()

    if input == "1":
        start = True
        songInformation = HintAndAuthor()


    entryBox.delete(0,END)

#Function that handles all inputs
def input(i):
    if start == False:
        startQuiz()

    elif start == True:
        GuessingSystem()
    

addText("Enter 1 To Start\n\n")


entryBox.bind("<Return>",input)




while signedIn == True:
    window.update()
print("Yes")