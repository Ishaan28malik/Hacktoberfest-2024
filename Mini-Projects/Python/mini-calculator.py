def addition():
    n = float(input("Enter the number: "))
    t=0
    ans=0
    while n!=0:
        ans+=n
        t+=1
        n = float(input("Enter another number: "))
        return [ans,t]

def substraction():
    n=float(input("Enter the number"))
    t=0
    ans=0
    while n!=0:
        ans=ans-n
        t+=1
        n=float(input("Enter another number"))
        return [ans,t]

def multiplication():
    n=float(input("Enter the number: "))
    t=0
    ans=1
    while n!=0:
        ans=ans*n
        t+=1
        n=float(input("Enter another number: "))

    return [ans,t]

def average():
    an=[]
    an=addition()
    t=an[1]
    a=an[0]
    ans=a/t
    return [ans,t]

while True:
    list=[]
    print("Enter 'a' for addition: ")
    print("Enter 'b' for substraction: ")
    print("Enter 'c' for multiplication: ")
    print("Enter 'v' for average: ")
    print("Enter q to quit")
    s=input(" ")
    if s!='q':
        if s=='a':
            list=addition()
            print(list[0],list[1])

        elif s=='b':
            list=substraction()
            print(list[0],list[1])

        elif s=='c':
            list=multiplication()
            print(list[0],list[1])

        elif c=='v':
            list=average()
            print(list[0],list[1])

        else:
            print("Sorry, invalid input")

        else:
            break


