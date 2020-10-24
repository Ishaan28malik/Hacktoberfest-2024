#include<stdio.h>
#include<conio.h>
int top=-1,size;
void push(int arr[])
{
    int num;
    if(top==size-1)
        printf("Stack Overflow!!!");
    else
    {
        printf("Enter a Number for insertion=");
        scanf("%d",&num);
        top++;
        arr[top]=num;
        printf("Element Inserted Successfully!!!");
    }
}
void pop(int arr[])
{
    if(top==-1)
        printf("Stack UnderFlow!!!");
    else
    {
        int x;
        x=arr[top];
        top--;
        printf("Deleted Element=%d",x);
    }
}
void display(int arr[])
{
    int i;
    printf("Stack Status:\n");
    for(i=0;i<=top;i++)
    {
        printf("%d\t",arr[i]);
    }
}
int main()
{
    int x,arr[50];
    char ch;
    clrscr();
    printf("----------Stack As An Array----------\n");
    printf("Enter the maximum number of elements=");
    scanf("%d",&size);
    do
    {
        printf("\n\tPress 1 for Insertion\n\tPress 2 for Deletion\n\tPress 3 for Display\n\tEnter your choice=");
        scanf("%d",&x);
	//system("cls");
        switch(x)
        {
            case 1: push(arr);break;
            case 2:pop(arr);break;
            case 3:display(arr);break;
            default:printf("\nWrong Choice!!! Enter Again!!!");break;
        }
        printf("\nDo You Want To Continue(Y/N)=");
        ch=getch();
    }while(ch=='Y'||ch=='y');
}
