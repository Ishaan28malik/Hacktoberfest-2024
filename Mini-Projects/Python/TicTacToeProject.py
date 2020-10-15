# Copyright 2019
#
# Author : Geetansh Atrey
#
# Python code to make a Tic Tac Toe a.k.a. X and 0s.
#

import os

def drawGrid(gridValues):
    i=0
    j=0
    c=0
    print("\n\n")
    for j in range(0,3):
        for i in range(0,3):
            if i==1:
                print("\t\t {0} | {1} | {2} ".format(gridValues[c],gridValues[c+1],gridValues[c+2]))
                c=c+3
            else:
                print("\t\t   |   |   ")
            i=i+1
        if j is not 2:
            print("\t\t-----------")
        j=j+1

winner=0
ch='y'
f=0
alist=[]
blist=[]
solutionList=[[0,1,2],[0,3,6],[0,4,8],[1,4,7],[2,5,8],[2,4,6],[3,4,5],[6,7,8]] 
currentPlayer=1
gridValues=[' ',' ',' ',' ',' ',' ',' ',' ',' ']

print("\n\n\t\tWELCOME TO THE TIC TAC TOE !\n")
while ch=='Y' or ch=='y':
    winner=0
    f=0
    alist=[]
    blist=[]
    solutionList=[[0,1,2],[0,3,6],[0,4,8],[1,4,7],[2,5,8],[2,4,6],[3,4,5],[6,7,8]] 
    currentPlayer=1
    gridValues=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
    name1=raw_input("Player 1:\t")
    print("\n")
    name2=raw_input("Player 2:\t")
    print("\n")
    dec=raw_input("Are you ready to play?   ")
    if dec=='Yes' or dec=='yes':
        p=raw_input("\nPlayer 1 ! Do you want to be X or 0 ???  ")
        if p=='x' or p=='X':
            p='X'
            m='O'
        else:
            p='O'
            m='X'
        os.system("cls")
        while winner==0 and len(alist)+len(blist)<9:
            if currentPlayer == 1 :
                if len(alist)+len(blist)==0:
                    drawGrid(gridValues)
                x=int((raw_input("\n\nPlayer 1 ! Enter the position for {0} : ".format(p))))
                os.system("cls")
                gridValues[x-1]=p
                alist.append(x-1)
                alist.sort()
                drawGrid(gridValues)
                length=len(alist)
                if length >= 3:
                    k=0
                    while k<8:
                        l1=solutionList[k][0]
                        l2=solutionList[k][1]
                        l3=solutionList[k][2]
                        if alist.count(l1)==1 and alist.count(l2)==1 and alist.count(l3)==1:
                            winner=currentPlayer
                            f=1
                            break
                        k=k+1
                if f==0:
                    currentPlayer=2
                else:
                    break
            elif currentPlayer==2:
                y=int(raw_input("\n\nPlayer 2 ! Enter the position for {0} : ".format(m)))
                os.system("cls")
                gridValues[y-1]=m
                blist.append(y-1)
                blist.sort()
                drawGrid(gridValues) 
                length=len(blist)
                if length >= 3:
                    k=0
                    while k<8:
                        k1=solutionList[k][0]
                        k2=solutionList[k][1]
                        k3=solutionList[k][2]
                        if blist.count(k1)==1 and blist.count(k2)==1 and blist.count(k3)==1:
                            winner=currentPlayer
                            f=1
                            break
                        k=k+1
                if f==0:
                    currentPlayer=1
                else:
                    break
        if winner == 1:
            print("\n\n\t    WINNER IS {0} ! \n".format(name1))
        elif winner == 2:
            print("\n\n\t    WINNER IS {0} ! \n".format(name2))
        else:
            print("\nDRAW !\n")
        ch=raw_input("\n\nWant a new match (Y/N) ?  ")
        os.system("cls")
