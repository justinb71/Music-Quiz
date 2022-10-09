
#Guess function
def enterGuess():
    
    resultsBox.config(state='normal')
    guess = entryBox.get()
    strippedGuess = guess.lstrip("!£$%^&*()_+-=#~:;@<>?[]{}")
    
    entryBox.delete(0,tk.END)
    if guess.isspace():

        messagebox.showerror("Error","INVALID INPUT")
    elif strippedGuess:
        
        resultsBox.insert(tk.INSERT, "Guess: " + strippedGuess + "\n\n")
        resultsBox.config(state='disabled')
   
def unformat(text):
    
    string2 = text.lstrip("'")
    string3 = string2.split("'")
    string4 = ("".join(string3)).split()
    string5 = "".join(string4)
    print(string5)

unformat("Stayin' alive")

