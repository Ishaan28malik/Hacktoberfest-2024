#define max 20
#include<stdio.h>
#include<conio.h>
#include<process.h>
typedef struct stack
{
	int operand[max];
	int top;
}stack;
void push(stack *s,int opnd)
{
	if(s->top==max-1)
	{
		printf("\n stack overflow");
	return;
	}
	(s->top)++;
	s->operand[s->top]=opnd;

}
int pop(stack *s)
{
	int opnd;
	if(s->top==-1)
	{
		printf("\n stack underflow");
	return -1;
	}
	opnd=s->operand[s->top];
	s->top--;
	return opnd;
}
int isopt(char opt)
{
	switch(opt)
	{
	case'+':
	case'-':
	case'*':
	case'/':
	case'%':
	case'^':
	 return 1;
	 }
return 0;
}
int eval(int lop,int rop,char opt)
{
	int res;
	switch(opt)
	{
		case'+':
			res=(lop+rop);
			return res;
		case'-':
			res=(lop-rop);
			return res;
		case'*':
			res=(lop*rop);
			return res;
		case'/':
			res=(lop/rop);
			return res;
		case'^':
			res=(lop^rop);
			return res;
		default: printf("\n invalid choice");
		}
}
void main()
{
	stack s;
	int lop,rop,i=0,opnd,res;
	char c,postfix[max];
	s.top=-1;
	clrscr();
	printf("\n enter valid postfix expression");
	scanf("%s",postfix);
	while(postfix[i]!='\0')
	{
		if(isdigit(postfix[i]))
		push(&s,postfix[i]-48);
		else if(postfix[i]=='+'||postfix[i]=='-'||postfix[i]=='*'||postfix[i]=='/'||postfix[i]=='^')
		{
			rop=pop(&s);
			lop=pop(&s);
			res=eval(lop,rop,postfix[i]);
			push(&s,res);

			}i++;
	}printf("\n result of postfix expression is %d",pop(&s));
getch();
}