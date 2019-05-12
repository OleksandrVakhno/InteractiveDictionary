import json
from difflib import get_close_matches

def printList(list):
    if (len(list) > 1):
        for i in list:
            print(i)
    else:
        print(list[0])

def translate(word):
    word = word.lower()
    if word in data:
        printList(data[word])
    elif word.title() in data:
        word=word.title()
        printList(data[word])
    elif word.upper() in data:  # in case user enters words like USA or NATO
         word = word.upper()
         printList(data[word])
    else:
        close = get_close_matches(word, data, n=1)
        if(close!=[]):
            q = input("Did you mean %s ? Please enter Y or N. " %close[0])
            if(q.lower()=='y'):
                translate(close[0])
            elif (q.lower()=='n'):
                print("Couldn't find the word. Please double check")
            else:
                print("Couldn't understand your response")
        else:
            print ("The word is not in dictionary")






data = json.load(open("data.json"))

user_input = input("Please enter a word: ")

translate(user_input)
