Following  code  will  transform  an  infix  arithmetic  expression  into  Postfix  arithmetic expression. You will also see the Program which evaluates a Postfix expression.
// This program provides you the concepts that how an infix
// arithmetic expression will be converted into post-fix expression
 





// using STACK
// Conversion Infix Expression into Post-fix // NOTE: ^ is used for raise-to-the-power #include<iostream.h>
#include<conio.h>
#include<string.h>
int main()
{ int const null=-1;
char Q[100],P[100],stack[100];// Q is infix and P is postfix array int n=0; // used to count item inserted in P
int c=0; // used as an index for P
int top=null; // it assign -1 to top 
int k,i;
cout<<“Put an arithematic INFIX _Expression\n\n\t\t";
cin.getline(Q,99); // reads an infix expression into Q as string 
k=strlen(Q); // it calculates the length of Q and store it in k 
// following two lines will do initial work with Q and stack 
strcat(Q,”)”); // This function add ) at the and of Q 
stack[++top]='('; // This statement will push first ( on Stack 
while(top!= null)
{
for(i=0;i<=k;i++) 
{
switch(Q[i]) 
{
case '+': 
case '-': 
for(;;) 
{
if(stack[top]!='(' )
{ P[c++]=stack[top--];n++; } 
else
break; 
}
stack[++top]=Q[i]; 
break;
case '*': 
case '/': 
case '%': 
for(;;)
{if(stack[top]=='(' || stack[top]=='+' || stack[top]=='-') break;
else
{ P[c++]=stack[top--]; n++; } 
}
stack[++top]=Q[i]; 
break;
case '^': 
for(;;) 
{
if(stack[top]=='(' || stack[top]=='+' || 
stack[top]=='-' || stack[top]=='/' || 
stack[top]=='*' || stack[top]=='%') break; 
else
{ P[c++]=stack[top--]; n++; } 
}
stack[++top]=Q[i];
 





break;
case '(':
stack[++top]=Q[i]; 
break;
case ')': 
for(;;) 
{
if(stack[top]=='(' ) {top--; break;} 
else { P[c++]=stack[top--]; n++;} 
}
break;
default : // it means that read item is an oprand P[c++]=Q[i];
n++;
} //END OF SWITCH
} //END OF FOR LOOP
} //END OF WHILE LOOP
P[n]='\0'; // this statement will put string terminator at the // end of P which is Postfix expression
cout<<"\n\nPOSTFIX EXPRESION IS \n\n\t\t"<<P<<endl; } //END OF MAIN FUNCTION
