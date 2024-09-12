from difflib import get_close_matches
import json
data=json.load(open("data.json"))
def translate(w):
    return data[w]
word=input("Enter word: ")
if word.upper() in data:
    y=translate(word.upper())
    if type(y)==list:
        for i in y:
            print(i)
    else:
        print(y)
else:
    x=get_close_matches(word.upper(),data.keys(),cutoff=0.8)
    if(len(x)!=0):
        print("Are u looking for",x[0],"??(y/n)")
        a=input()
        if(a=='y'):
            print(translate(x[0]))
        elif(a=='n'):
            print("The word doesn't exist....Please double check....")
        else:
            print("We didn't understand your query")
    else:
        print("Word not in dictionary")