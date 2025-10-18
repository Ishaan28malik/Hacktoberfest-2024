#function definition for initialization screen

def init():
    print('\r')
    print("-"*60)
    print("  Welcom to the ATM machine with cash deposite facility")
    print("-"*60)
    print('\r')
    print("Press 1 for check balance")
    print('\r')
    print("Press 2 for Deposite amount")
    print('\r')
    print("Press 3 for Withdraw amount")
    print('\r')
    global q
    q = float(input("Enter your choice = "))  # for input from user
    return q
global c
c=2000
#e=init()
init() #calling function for main screen view
#e = float(input("Enter your choice = ")) #for input from user
while True:
        if (q==1):  #case 1 for checking balance
            print("Your available Balance is = ",c)
            j = input("Do u want to explore more?.....(yes/no)")
            if (j == "Yes" or j=="yes" or j == "YES"):
                init()
                #e = float(input("Enter your choice = "))  # for input from user
            else:
                print("----Thanks For using this ATM-CUM-DEPOSITE Machine----")
                print('\r')
                quit()

        elif(q==2): #case 2 for deposite money
            a = int(input("Enter amount to deposite = "))
            c=a+c
            print('\r')
            print("You have successfully Deposited Rs. ",a," in your account.")
            print('\r')
            print("Do you want to chech your Total Available Balance")
            y=(input("Enter Y/N = "))
            if(y=='Y'or y=='y'):
                print("Your available Balance is ", c)
                print('\r')
                j = input("Do u want to explore more?.....(yes/no)")
                if (j == "Yes" or j == "yes" or j == "YES"):
                    init()
                    #e = float(input("Enter your choice = "))  # for input from user
                else:
                    print("----Thanks For using this ATM-CUM-DEPOSITE Machine----")
                    quit()
            elif (n == "NO" or n=="no" or n == "No"):
                j = input("Do u want to explore more?.....(yes/no)")
                if (j == "Yes" or j == "yes" or j == "YES"):
                    init()
                    #e = float(input("Enter your choice = "))  # for input from user
                else:
                    print("----Thanks For using this ATM-CUM-DEPOSITE Machine----")
                print('\r')
                quit()

        elif(q==3):#case 3 for withdraw
            b = int(input("Enter the amount to withdraw = "))
            if(b<=c):

                c=c-b
                print("You have withdrawn Amount = ",b," Successfully from Your account.")
                print("       Available balance in your accout is = ", c)
                j = input("Do u want to explore more?.....(yes/no)")
                if (j == "Yes" or j == "yes" or j == "YES"):
                    init()
                    #e = float(input("Enter your choice = "))  # for input from user
                elif (j== "no" or j == "No" or j == "NO"):
                    print("----Thanks For using this ATM-CUM-DEPOSITE Machine----")
                    print("          Thank you visit again           ")
                    quit()
                else:
                    quit()
            else:
                print("...You dont have enogh balance in your account...")

                print('\r')
                j=input("Do u want to explore more?.....(yes/no)")
                if (j == 'Yes', 'yes', 'YES'):
                    init()
                    #e = float(input("Enter your choice = "))  # for input from user
                else:
                    print("----Thanks For using this ATM-CUM-DEPOSITE Machine----")
                    print("          Thank you visit again           ")
                    quit()

        else:
            print("You have entered wrong input")
            init()
            #e = float(input("Enter your choice = "))
