#include<conio.h>
#include<stdio.h>
#include<process.h>
#include<stdlib.h>
typedef struct Node
{
	int val;
       struct Node *next;
       struct node *prev;
}node;
node *getnode(int num)
{
	node *newnode;
	newnode=(node *)malloc(sizeof(node));
	newnode->val=num;
	newnode->next=NULL;
	newnode->prev=NULL;
	return newnode;
}
void addbeg(node **start)
{
	node *p,*nn;
	int num;
	p=*start;
	printf("\n enter the data");
	scanf("%d",&num);
	nn=getnode(num);
	if(*start==NULL)
	{
		*start=nn;
	}
	else
	{
		nn->next=p;
		p->prev=nn;
	       *start=nn;
	}
}
void addlast(node **start)
{
	node *p,*nn;
	int num ;
	p=*start;
	printf("\n enter the data");
	scanf("%d",&num);
	nn=getnode(num);
	if(*start==NULL)
	{

		*start=nn;
		(*start)->prev=NULL;
		(*start)->next=NULL;
		p=*start;
	}
	else
	{
	p=*start;
		while(p->next!=NULL)
		{
		p=p->next;
		}

		nn->next=p->next;
		nn->prev=p;
		p->next=nn;
	}
}
void deletepos(node **start)
{
       node *p,*temp;
       int num;
       p=*start;
       printf("\n enter the data to be deleted");
       scanf("%d",&num);
	if(*start==NULL)
	{
		printf("\n node is empty\n");
	return;
	}
	       if((*start)->val==num)
	       {
		temp=*start;
		*start=(*start)->next;
		(*start)->next->prev=NULL;
		free(temp);
		}
		else
		{
			p=*start;
			while(p->next!=NULL&&p->next->val!=num)
			{
			       p=p->next;
			}
				temp=p->next;
				p->next=p->next->next;
				if(p->next==NULL)
				p->next->prev=p;
				free(temp);

		}
}
void order_list(node **start1,int n)
{
	node *nn,*p;
	int num;
	p=*start1;
       /*	printf("\n enter the number");
	scanf("%d",&num);     */
	nn=getnode(n);
	if(*start1==NULL)
	{
		*start1=nn;
	}
	else if((*start1)->val>nn->val)
	{	nn->next==*start1;
		(*start1)->prev=nn;
		*start1=nn;
	}
	else
	{
		p=*start1;
		while(p->next!=NULL&&p->next->val<nn->val)
		{
			p=p->next;
		}
		       nn->next=p->next;
		       nn->prev=p;
		       if(p->next!=NULL)
		       {
			nn->next->prev=nn;
			p->next=nn;
			}
	}
}
void display(node **start)
{
	node *p;
	p=*start;
	while(p!=NULL)
	{
		printf("\n %d",p->val);
		p=p->next;
	}
}
void main()
{
	 node *start=NULL,*start1=NULL;
	 int ch,n;
	 clrscr();
	while(1)
	{
		printf("\n menu ");
		printf("\n1 add at begining\n2 add at last\n3delete by position\n4 order list \n5 display\n6 exit");
		printf("\n enter choice");
		scanf("%d",&ch);
		switch(ch)
		{
		   case 1:
				addbeg(&start);
				break;
		   case 2:
				addlast(&start);
				break;
		   case 3:
				deletepos(&start);
				 break;
		   case 4:     printf("\n enter value to insert in first list");
				scanf("%d",&n);
				order_list(&start1,n);
				display(&start1);
				break;
		   case 5:	display(&start);
				break;
		   case 6:	 exit(0);
		}
	}getch();
}