#include<stdio.h>
#include<stdlib.h>
int front=0, rear=-1, i, n;
void enqueue(int a[100], int element)
{
	if((rear!=-1 && ((rear+1)%n)==front))
	{
		printf("-2\n");
		return;
	}
	else
	{	

		if(rear==n-1)
		{
			rear=-1;
		}
		rear++;
		a[rear]=element;
		return;
	}
}
int dequeue(int a[100])
{
	int num2;
	if(front==0 && rear==-1)
	{
		num2 = -1;
		return num2;
	}
	else if(front==rear)
	{
		num2 = a[front];
		front=0;
		rear=-1;
		return num2;
	}
	else
	{		
		num2 = a[front];
		front++;
		if(front==n)
			front=0;
		return num2;
	}	
}
void print_queue(int a[100]);
int main()
{
	int num, num2, a[100];
	scanf("%d", &n);
	char ch;
	label:ch = getchar();
	switch(ch)
	{
		case 'e' : scanf("%d", &num);
			enqueue(a, num);			
			break;
			 
		case 'd' : num2 = dequeue(a);
			printf("%d\n", num2);
			break;		
		case 'p' : print_queue(a);
			printf("\n");
			break;		 	
	}
	if(ch!='s')
		goto label;
	return 0;
}
void print_queue(int a[100])
{
	if((front==0 && rear==-1))
	{
		printf("-1");
		return;
	}
	for(i=front;;i++)
	{
		if(i==n)
			i=0;
		printf("%d ", a[i]);
		if(i==rear)
			break;	
	}
}
