import json
from difflib import get_close_matches
from tkinter import *
from tkinter import messagebox

def clearGrid():
    for label in window.grid_slaves():
        if int(label.grid_info()["row"]) > 0:
            label.grid_forget()

def createLabel(text):
    clearGrid()
    l2 =Label(window, text= "Your definition is: ")
    l2.grid(row=1, column = 0)
    l3 = Label(window, text=text, fg="green")
    l3.grid(row=1, column=1)

def notFound(text):
    clearGrid()
    l4 = Label(window, text = text, fg="red")
    l4.grid(row=1, column=1)



def translate(value):
    word = value.lower()
    if word in data:
        createLabel("\n".join(data[word]))
    elif word.title() in data:
        word=word.title()
        createLabel("\n".join(data[word]))
    elif word.upper() in data:  # in case user enters words like USA or NATO
         word = word.upper()
         createLabel("\n".join(data[word]))
    else:
        close = get_close_matches(word, data, n=1)
        if(close!=[]):
            q = messagebox.askquestion ('No word found',"Did you mean %s ?  " %close[0],icon = 'warning')
            if(q=='yes'):
                translate(close[0])
            else:
                notFound("Couldn't find the word. Please double check")
        else:
            notFound ("The word is not in dictionary")




if __name__== "__main__":
    data = json.load(open("data.json"))

    window = Tk()

    l1 = Label(text="Please enter a word: ")
    l1.grid(row=0, column=0)

    e1_value = StringVar()
    e1 = Entry(window, textvariable=e1_value)
    e1.grid(row=0, column=1)

    b1 = Button(text='Submit', command=lambda: translate(e1_value.get()))
    b1.grid(row=0, column=2)

    window.mainloop()
