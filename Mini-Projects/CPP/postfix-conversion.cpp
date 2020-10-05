#include<iostream>


using namespace std;

int top=-1;
char st[20];

void push(char c)
{

    top=top+1;
    st[top]=c;

}

char pop()
{
   char data;
    if(top==-1)
    {
        return -1;
    }
    else
    {
        data=st[top];
        top=top-1;
       return data;
    }
}

int priority(char c)
{
    if(c=='(')
        return 0;
    if(c=='+'||c=='-')
        return 1;
    if(c=='*'||c=='/')
        return 2;

}

int main()
{
char exp[20];
char *e,x;
char c;

cout<<"Enter the Expression : ";
cin>>exp;
e=exp;
while(*e!='\0')
{
    if(isalnum(*e))
        cout<<*e;
    else if(*e=='(')
        push(*e);
    else if(*e==')')
    {
        while((x=pop())!='(')
                cout<<x;
    }
    else
    {
        while(priority(st[top])>=priority(*e))
                    cout<<pop();
            push(*e);

    }

e++;
}
while(top!=-1)
{
     cout<<pop();

}
}
