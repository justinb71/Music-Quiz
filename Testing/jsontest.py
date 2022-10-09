import json
import random



#Loads all the songs into data
data = json.load(open("List.json"))


#Loads the catagories into variables
seventies = data["70s"]
eighties = data["80s"]


#Linear Search function
def linearSearch(list,item):
   
    for i in list:

        if item == i:
            return True
    return False

#A list that holds the values of songs that have already been used
usedNumbers =[]



for i in range(0,10):
    #Creates random number
    randomNumber = random.randint(0,9)

    #This checks if the random number has been used before
    contains = linearSearch(usedNumbers,randomNumber)

    #If it has then pick a new number and check again
    while contains == True:

        randomNumber = random.randint(0,9)
        contains = linearSearch(usedNumbers,randomNumber)


    #Grabs the songs data
    currentSong = seventies[randomNumber]

    #Grabs the song from the list
    name = currentSong["Title"]
    print(name + "\n")
    #Adds the random number to the list of used numbers
    usedNumbers.append(randomNumber)
    
print(usedNumbers)
