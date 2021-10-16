class QueueUsing2Stacks:
    
    def __init__(self):
        self.__s1=[]
        self.__s2=[]
        
    def enqueue(self,val):
        self.__s1.append(val)
        
    def dequeue(self):
        if self.size()==0:
            print("NOTHING CANNOT DEQUEUED AS THE QUEUE IS EMPTY !!!")
        # pop(0) is not used as it takes o(n) time        
        else:
            while len(self.__s1)!=1:
                self.__s2.append(self.__s1[-1])
                self.__s1.pop()
            ele=self.__s1.pop()
            while len(self.__s2)!=0:
                self.__s1.append(self.__s2[-1])
                self.__s2.pop()          
            return ele
        
    def size(self):
        return len(self.__s1)
    
    def front(self):
        if self.size()==0:
            print("QUEUE AS NO FRONT END AND REAR END AS THE QUEUE IS EMPTY !!!")
        else:
            return self.__s1[0]       
    
    def rear(self):
        if self.size()==0:
            print("QUEUE AS NO FRONT END AND REAR END AS THE QUEUE IS EMPTY !!!")
        else:
            return self.__s1[-1]
    
    def isEmpty(self):
        if self.size()==0:
            return True
        else:
            return False
        
    def display(self):
        return print(self.__s1)

print('''QUEUE MENU :-
1.) ENTER 1 TO ENQUEUE A ELEMENT IN THE QUEUE
2.) ENTER 2 TO DEQUEUE A ELEMENT IN THE QUEUE
3.) ENTER 3 TO PRINT FRONT END OF THE QUEUE
4.) ENTER 4 TO PRINT REAR END OF THE QUEUE
5.) ENTER 5 TO PRINT SIZE OF THE QUEUE
6.) ENTER 6 TO CHECK WHETHER THE QUEUE IS EMPTY OR NOT
7.) ENTER 7 TO PRINT THE QUEUE
8.) ENTER 0 TO EXIT THE MENU''')
choice=int(input("ENTER YOUR CHOICE : "))
a=QueueUsing2Stacks()
while choice:
    if choice==1:
        data=int(input("ENTER THE VALUE OF ELEMENT TO BE ENQUEUED IN THE QUEUE : "))
        a.enqueue(data)
        choice=int(input("ENTER YOUR CHOICE : "))
    elif choice==2:
        print("THE ELEMENT DEQUEUED FROM THE QUEUE IS :",a.dequeue())
        choice=int(input("ENTER YOUR CHOICE : "))
    elif choice==3:
        print("THE ELEMENT AT THE FRONT END OF THE QUEUE IS :",a.front())
        choice=int(input("ENTER YOUR CHOICE : "))
    elif choice==4:
        print("THE ELEMENT AT THE REAR END OF THE QUEUE IS :",a.rear())
        choice=int(input("ENTER YOUR CHOICE : "))
    elif choice==5:
        print("THE SIZE OF THE QUEUE IS :",a.size())
        choice=int(input("ENTER YOUR CHOICE : "))
    elif choice==6:
        print(a.isEmpty())
        choice=int(input("ENTER YOUR CHOICE : "))
    elif choice==7:
        print("QUEUE IS : ",end="")
        a.display()
        choice=int(input("ENTER YOUR CHOICE : "))
    elif choice==0:
        exit()
    else:
        print("WRONG CHOICE SELECTED")
        choice=int(input("ENTER YOUR CHOICE : "))