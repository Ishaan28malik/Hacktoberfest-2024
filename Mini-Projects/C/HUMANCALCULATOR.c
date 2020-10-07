//simple game testing calculation skills
#include<stdio.h>
#include <stdlib.h>
#include<conio.h>
void medium();
void easy();
void start();
int sum1=0;
int sum2=0;
int main()
{int d=0;
printf("HUMAN CALCULATOR\n\n\n");
	printf("\nWelcome to the game of maths meant for kids of age(0-12)\nLets see if you are a human calculator or not");
	start();
	printf("\n\nLEVEL 1\n\nNow time for set of easy problems\nlets see how your brain works\n\n");
	printf("Press any key to start.\n");

    getch();
	easy();
	printf("\n\nLEVEL 2\n\nNow,time for some tough level questions!!\nHere the fun begins let's Start\n\n");
	printf("Press any key to start.\n");

    getch();
	medium();
	d=sum1+sum2;
	if(d<=3)
	{
		printf("\n\nYOUR TOTAL SCORE IS %d[LEVEL 1+ LEVEL 2]\n\nYou are very weak in Calcultions\nGo back home and practice\n",d);
	}
	else if(d>3&&d<=6)
	{
		printf("\n\nYOUR TOTAL SCORE IS %d[LEVEL 1+ LEVEL 2]\n\nYou are average !! still needs to work on your calculations\n",d);
	}
	else if(d>6)
	{
		printf("\n\nYOUR TOTAL SCORE IS %d[LEVEL 1+ LEVEL 2]\n\nYou are great,Keep Going\n",d);
	}
	else
	{
		printf("Awesome!!\nFull marks");
	}
}
void start()
{ char w[100];
	char s[100];
	int age;
	printf("\nEnter your name\n");
	gets(s);
	printf("\nEnter your gaming nickname\n");
	gets(w);
	printf("\nHey %s Enter your age\n",w);
	scanf("%d",&age);
	if(age<=12)
	printf("HELLO, %s YOU ARE WELCOME TO THE GAME [HUMAN CALCULATOR]\n",w);
	else
	{
	
	printf("Sorry %s, this game is meant for kids (0-12)",w);
	exit(0);}
}
void easy()
{int i,j=2;
int n,s=0,right=0,wrong=0;
	for(i=0;i<5;i++)
	{
		printf("(%d+(%d+3)*%d)",i,i+2,j+7);
		s=0;
		s=(i+((i+2)+3)*(j+7));
		printf("\nEnter your answer:\n");
		scanf("%d",&n);
		if(n==s)
		{
			printf("\nWOW! you got your Question No. %d Correct\n",i+1);
			
			right++;
		}else
		{
		
			printf("\nI am afraid!\nYour Question No. %d is wrong the correct answer is %d\n",i+1,s);
			wrong++;
		}
		j++;
}
		printf("\n\nRESULT[LEVEL 1]\n\n");
		printf("RIGHT\t\tWRONG\n%d\t\t%d",right,wrong);
	
	sum1=right;
	
}
void medium()
{int j=3,k=50,i;
int ans,s=0,right=0,wrong=0;
	for(i=10;i<20;i++)
	{
		printf("\nThe question is\n%d*%d+(%d*%d)-%d\n",i+2,j*2,k,i,j+1);
	s=(((i+2)*(j*2))+(k*i)-(j+1));
	printf("\nEnter your answer:\n");
	scanf("%d",&ans);
	if(ans==s)
		{
			printf("\nWOW! you got your Question No. %d Correct\n",i-9);
			right++;
		}
		else
		{
			printf("\nI am afraid!\nYour Question No. %d is wrong  wrong the correct answer %d",i+1,s);
			wrong++;
		}
		j++;
		k--;
	}
		printf("\nRESULT[LEVEL 2]\n\n");
		printf("RIGHT\t\tWRONG\n%d\t\t%d",right,wrong);
	sum2=right;
}

	
	
	
	
	
	
	
	
	
	
	
