import pandas as pd
import random
class bookCricket:
    def __init__(self):
        self.displayrules()
        x= input("Press any key to continue:\n")
        while True:
            print("press 1 to enter the players of team 1\n")
            print("press 2 to enter the players of team 2\n")
            print("press 3 to start the game for team 1\n")
            print("press 4 to start the game for team 2\n")
            print("press 5 to display scorecard\n")
            print("press 6 to exit\n")
            g = int(input())
            if g == 1:
                b1,d1 = self.takeInput1()
                y = input("Do you want to continue with these names? (y/n): ")
                if y != 'y':
                    b1,d1 = self.takeInput1()
            if g == 2:
                b2,d2 = self.takeInput2()
                y = input("Do you want to continue with these names? (y/n): ")
                if y != 'y':
                    b2,d2 = self.takeInput2()
            if g == 3:
                sc1 = self.player1(b1,d1)
            if g == 4:
                sc2 = self.player2(b2,d2)
            if g == 5:
                self.scorecard(sc1,sc2)
            if g== 6:
                break


    def displayrules(self):
        print("===== WELCOME TO THE VIRTUAL BOOK CRICKET =====\n\n")
        print("This game can be played by only two players\n")

    def takeInput1(self):
        print("Enter the details for team 1: \n")
        print("Enter the no. of players: \n")
        n1 = int(input())
        batsmenName1=[]
        for i in range (0,n1):
            print("\nEnter the name of ",i+1,"th player: \n")
            i= input()
            batsmenName1.append(i)
            print()
        df1 = pd.DataFrame(batsmenName1)
        df1.columns=["Batsman Name"]
        print(df1, "\n")
        return batsmenName1,df1
    
    def takeInput2(self):
        print("\nEnter the details for team 2: \n")
        print("Enter the no. of players: \n")
        n2 = int(input())
        batsmenName2=[]
        for i in range (0,n2):
            print("\nEnter the name of ",i+1,"th player: \n")
            i= input()
            batsmenName2.append(i)
            print()
        df2 = pd.DataFrame(batsmenName2)
        df2.columns=["Batsman Name"]
        print(df2, "\n")
        return batsmenName2,df2

    def player1(self,batsmenName1,df1):
        score =[]
        ball = []
        print("\n Team 1 wil play now \n")
        print(batsmenName1)
        for i in range (0,len(batsmenName1)):
            print("\n",batsmenName1[i]," will play now.\n")
            runs =0
            play = input("***Click 'p' button to play.***\n")
            balls = 0
            while play == 'p':
                j = random.choice([2,4,6,1,0])
                if (j ==2 or j == 4 or j == 6 or j== 1):
                    print(batsmenName1[i]," scored ",j," runs.\n")
                    runs = runs + j
                    balls = balls + 1
                if j ==0:
                    print("\n",batsmenName1[i]," got out!\n")
                    print("\n",batsmenName1[i]," scored ",runs," runs in",balls + 1," balls.\n")
                    balls = balls + 1
                    break
                play = input("***Click 'p' button to play.***\n")
            score.append(runs)
            ball.append(balls)
        df1['Runs']= score
        df1['Balls']= ball
        df1['Run-rate']= df1['Runs']/(df1['Balls'])/6
        print(df1)
        return df1    

    def player2(self,batsmenName2,df2):
        score =[]
        ball = []
        print("\n Team 2 wil play now \n")
        print(batsmenName2)
        for i in range (0,len(batsmenName2)):
            print("\n",batsmenName2[i]," will play now.\n")
            runs =0
            play = input("***Click 'p' button to play.***\n")
            balls = 0
            while play == 'p':
                j = random.choice([2,4,6,1,0])
                if (j ==2 or j == 4 or j == 6 or j== 1):
                    print(batsmenName2[i]," scored ",j," runs.\n")
                    runs = runs + j
                    balls = balls +1 
                if j ==0:
                    print("\n",batsmenName2[i]," got out!\n")
                    print("\n",batsmenName2[i]," scored ",runs," runs in ",balls," balls.\n")
                    balls = balls +1 
                    break
                play = input("***Click 'p' button to play.***\n")
            score.append(runs)
            ball.append(balls)
        df2['Runs']= score
        df2['Balls']= ball
        df2['Run-rate']= df2['Runs']/(df2['Balls']/6)
        print(df2)
        return df2            
    
    def scorecard(self,df1,df2):
        print("Team 1:\n")
        print(df1,"\n\n")
        print("Team 2:\n")
        print(df2,"\n\n")


b =bookCricket()
