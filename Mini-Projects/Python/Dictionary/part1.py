import sys 

dict={}
def main():
    try:
        file=open("words.txt","r")
        load(file)
        print("file loaded sucessfully")
        file.close()
    except:
        print("something went wrong when loading files")

    while True:
        cmd=str(input("\npress \nw to write \ns to search\nd to delete\nsh to show all the words and meanings\nq to exit\n"))

        if cmd=="w":
            word=str(input("\nenter a word : "))
            meaning=str(input("enter the meaning : "))
            try:
                writter(word,meaning)
                print(f"{word} sucessfully inserted")
        
            except:
                print("\nsomething went wrong")
                

        elif cmd=="s":
            word=str(input("\nenter the word : "))
            try:
                meaning=search(word)
                print(meaning)
            except:
                print("something went wrong")
            

        elif cmd=="d":
            word=str(input("\nenter the word u want to delete : "))
            try:
                delete(word)
                print(f"\n{word} succesfully deleted")
            except KeyError:
                print("\nword not in the dictionary")
            except:
                print("\nsomething went wrong")
        
        elif cmd=="sh":
            show()

        elif cmd=="q":
            sys.exit()

        else:
            print(f"\n{cmd} is not a valid command")
        input("\npress enter to continue")


def load(file):
    for line in file:
        words=line.split("-")
        dict[words[0]]=words[1]

def show():
    print("\nword \t  meaning")
    for word,meaning in dict.items():
        print(f"{word} \t= {meaning}")
    print("\n")

def writter (word,meaning):
    dict[word]=meaning
    file=open("words.txt","a")
    file.write(f'{word}-{meaning}\n')
    file.close()


def search(word):
    meaning = dict[word]
    return meaning

def delete(word):
    dict.pop(word)
    file=open("words.txt","r+")
    lines=file.readlines()
    file.close()
    new_file=open("words.txt","w")
    for line in lines:
        line_words=line.split('-')

        if line_words[0]!=word:
            new_file.write(line)
        else:
            pass
    new_file.close()

main()
