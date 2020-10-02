#include<iostream>
#include<string.h>
using namespace std;
#define size 50
class stack
{
public:
	char s[size];
	int t;
	stack ()
	{
		t=-1;
	}
	void push(char x)
	{
		t++;
		s[t]=x;
	}
	char top ()
	{
		return s[t];
	}
	void pop()
	{
		t--;
	}
	bool isempty ()
	{
		if (t==-1)
			return true;
		return false;
	}
	bool isfull ()
	{
		if (t==size-1)
			return true;
		return false;
	}
};
bool check(char x[],int n)
{
	stack S3;
	int open=0,close=0,count=0;
		for (int i=0;i<n;i++)
		{
			if (x[i]=='(')
			{
				count++;
				S3.push(x[i]);
				open++;	
			}
			if (x[i]==')')
			{
				count--;
				char z=S3.top();
				S3.pop();
				{
					if (z=='(')
					{
						close++;
					}
				}
			}
		}
		if (count == 0 && open == close && S3.isempty())
		{
			return true;
		}
		return false;
}
int checkprecedence(char x)
{
	if (x=='+'||x=='-')
		return 1;
	else if (x=='*'||x=='/')
		return 2;
}
float solve(char x[],int n)
{
	stack temp;
	float result;
	for (int i=0;i<n;i++)
	{
		if (x[i]!='+'&&x[i]!='-'&&x[i]!='*'&&x[i]!='/')
		{
			temp.push(x[i]);
		}
		else
		{
			int a,b;
			a=temp.top()-'0';
			temp.pop();
			b=temp.top()-'0';
			temp.pop();
			switch (x[i])
			{
				case '+': {result=(float)a+(float) b; temp.push(result+'0'); break;}
				case '-': {result=(float)b-(float) a; temp.push(result+'0'); break;}
				case '*': {result=(float)a*(float) b; temp.push(result+'0'); break;}
				case '/': {result=(float)b/ a; temp.push(result+'0'); break;}
			}
		}
	}
	result = temp.top()-'0';
	return result;
}
int main()
{
	char in[50],post[50];
	int n;
	do
	{
		cout<<"Enter a valid well parentesized infix expression"<<endl;
		cin.getline(in,50);
		n=strlen(in);
	}while (!check(in,n));
	stack S1;
	int posti=0;
	for(int count=0;count<n;count++)
	{
		if (in[count]!='+'&&in[count]!='-'&&in[count]!='*'&&in[count]!='/'&&in[count]!='('&&in[count]!=')')
		{
			post[posti]=in[count];
			posti++;
		
		}
		else if (in[count]=='(')
		{
			S1.push('(');
		}
		else if (in[count]==')')
		{
			while (S1.top()!='(')
			{
				post[posti]=S1.top();
				S1.pop();
				posti++;
			}
			S1.pop();
		}
		else
		{
			if (!S1.isempty()&&S1.top()!='(')
			{
				int a,b;
				char temp=S1.top(),op=in[count];
				a=checkprecedence(temp);
				b=checkprecedence(op);
				if (b<=a)
				{
					post[posti]=temp;
					posti++;
					S1.pop();
					S1.push(op);
				}
				else if (b>a)
				{
					S1.push(op);
				}
			}
			else
			{
				S1.push(in[count]);
			}
		}
		
	}
	while (!S1.isempty())
	{
		post[posti]=S1.top();
		posti++;
		S1.pop();
	}
	n=posti;
	cout<<"The equivalent postfix expression is "<<endl;
	for (int i=0;i<n;i++)
	{
		cout<<post[i];	
	}
	cout<<endl;
	cout<<"The result = "<<solve(post,n)<<endl;
}
/*
Enter a valid well parentesized infix expression
(1+2)*3+4/(1+2*2)+9
The equivalent postfix expression is 
12+3*4122*+/9++
The result = 18
*/
