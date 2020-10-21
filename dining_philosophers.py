n=int(input("Enter the number of philosophers: "))
state=[0]*n
while(1):
    p = int(input("Enter the philosopher :"))
    ac=int(input("Enter action 1-PICKUP 2-PUTDOWN 3-EXIT:"))
    if(ac==1):
        state[p]=1
        print("Philosopher "+str(p)+" is HUNGRY")
        if(state[(p+(n-1))%n]!=2 and state[p]==1 and state[(p+1)%n]!=2):
            state[p]=2
            print("Philosopher "+str(p)+" is EATING")
        else:
            print("Philosopher "+str(p)+" CANNOT EAT")
    elif(ac==2):
        state[p]=0
        print("Philosopher "+str(p)+" is THINKING")
        a=(p+(n-1))%n
        b=(p+1)%n
        if(state[(a+(n-1))%n]!=2 and state[a]==1 and state[(a+1)%n]!=2):
            state[a]=2
            print("Philosopher "+str(a)+" is EATING")
        else:
            print("Philosopher "+str(a)+" CANNOT EAT")
        if(state[(b+(n-1))%n]!=2 and state[b]==1 and state[(b+1)%n]!=2):
            state[b]=2
            print("Philosopher "+str(b)+" is EATING")
        else:
            print("Philosopher "+str(b)+" CANNOT EAT")
    else:
    	break
