def check(pl,count):
        if l[pl-1]=='X' or l[pl-1]=='O' or pl<1 or pl>9:
            print("Please Choose an available Slot")
            count-=1
        else:
            if (count)%2==0:
                l[pl-1]='X'
            else:
                l[pl-1]="O"
        return(count)        
def display(l,count):
    for i in range(0,9):
        if i==2 or i==5 or i==8:
            print(l[i])
        else:
            print(l[i],end=' ')
    play(l,count)    
def play(l,count):
    if count==9:
        print("Draw")
        exit()
    for i in range(0,9):
     if (l[0]==l[1] and l[1]==l[2]) or (l[3]==l[4] and l[4]==l[5]) or (l[6]==l[7] and l[7]==l[8]) or (l[0]==l[3] and l[3]==l[6]) or (l[1]==l[4] and l[7]==l[4]): 
            count=(-1)
            name=l[i]
            break
    if count%2==0:
        pl=int(input("Select the Position to Place X:"))
        count=check(pl,count)
    elif count==-1:
        print(name,"Wins.")
        exit()
    else:
        pl=int(input("Select the Position to Place O:"))
        count=check(pl,count)
    count+=1    
    display(l,count)    
print("TIC TAC TOO")
l=['1','2','3','4','5','6','7','8','9','nil','nil','nil','nil']
l=l*10000
count=0
display(l,count)
