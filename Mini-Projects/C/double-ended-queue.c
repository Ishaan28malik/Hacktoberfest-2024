//implementation of dequeue using 2 stacks
#include<stdio.h>
#include <stdio.h>
#include <stdlib.h>
 
void push1(int);
void push2(int);
int pop1();
int pop2();
void enqueue1();
void enqueue2();
void dequeue1();
void dequeue2();
void display();
void create();
 
int st1[10], st2[10];
int top1 , top2 ;
int count = 0;
 
int main()
{
    int ch;
 
    printf("\n1 - Enqueue element from front into queue");
    printf("\n2 - Enqueue element fron rear end of the queue");
    printf("\n3 - Dequeu element from front end of the  queue");
    printf("\n4 - Dequeu element from rear end of the  queue");
    printf("\n5 - Display from queue");
    printf("\n6 - Exit");
    create();
    while (1)
    {
        printf("\nEnter choice");
        scanf("%d", &ch);
        switch (ch)
        {
        case 1:
            enqueue1();
            break;
        case 2:
            enqueue2();
            break;
        case 3:
            dequeue1();
            break;
        case 4:
            dequeue2();
            break;
        case 5:
        	display();
        	break;
        case 6:
        	exit(0);
        default:
            printf("Wrong choice");
        }
    }
}
 
/*Function to create a queue*/
void create()
{
    top1 = top2 = -1;
}
 
/*Function to push the element on to the stack*/
void push1(int data)
{
    st1[++top1] = data;
}
 
/*Function to pop the element from the stack*/
int pop1()
{
    return(st1[top1--]);
}
 
/*Function to push an element on to stack*/
void push2(int data)
{
    st2[++top2] = data;
}
 
/*Function to pop an element from th stack*/
 
int pop2()
{
    return(st2[top2--]);
}
 
/*Function to add an element into the queue using stack*/
void enqueue1()
{
    int data, i;
 
    printf("Enter data into queue");
    scanf("%d", &data);
    push1(data);
    count++;
}
void enqueue2(){
	 int data, i;
 
    printf("Enter data into queue");
    scanf("%d", &data);
    for (i = 0;i <count;i++)
    {
        push2(pop1());
    }
    
    push2(data);
    count++;
    
    for (i = 0;i <count;i++)
    {
        push1(pop2());
    }
}

 
/*Function to delete an element from the queue using stack*/
 void dequeue1(){
 	int k=pop1();
 	count--;
 	printf("\nThe element deleted is %d\n",k);
 }
void dequeue2()
{
    int i,k;
 
    for (i = 0;i < count;i++)
    {
        push2(pop1());
    }
   k= pop2();
    count--;
    for (i = 0;i < count;i++)
    {
        push1(pop2());
    }
    printf("\nthe element deleted is %d\n",k);
}
 
/*Function to display the elements in the stack*/
 
void display()
{
    int i;
 
    for (i = top1;i >-1;i--)
    {
        printf(" %d ", st1[i]);
    }
}
