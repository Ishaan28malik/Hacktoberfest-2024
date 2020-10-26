//Author : Vaishnavi Janardhan
//Github id : vaishnavi-janardhan

#include<math.h>
#include <stdio.h>

#define MAX_SIZE 10

typedef struct
{
	int stack[MAX_SIZE];
	int top;
} opstack;

void push(opstack *p, int num){
	if(p -> top == MAX_SIZE){
		printf("Stack full\n");
	}
	(p -> top)++;
	p -> stack[p -> top] = num;
}

int pop(opstack *p){
	return(p -> stack[p -> top--]);
}

int isDigit(char x){
	if(x>='0' && x<='9')
		return 1;
	return 0;
}

int evaluate(char op, int op1, int op2){
	switch(op){
		case '+':
			return op1+op2;
		case '-':
			return op1-op2;
		case '*':
			return op1*op2;
		case '/':
			return op1/op2;
		case '%':
			return op1%op2;
		case '^':
			return pow(op1,op2);
	}

}

int main(int argc, char const *argv[])
{
	char exp[10];
	char x;
	int i = 0;
	printf("Enter a prefix expression: \n");
	while((x = getchar())!='\n'){
		exp[i++] = x;
	}
	opstack s;
	s.top = -1;
	for(int j = i-1; j>=0; j--){
		char ch = exp[j];
		if(isDigit(ch)){
			push(&s,ch-'0');
		}
		else{
			int op1 = pop(&s);
			int op2 = pop(&s);
			int value = evaluate(ch,op1,op2);
			push(&s,value);
		}
	}
	printf("The value is: %d\n",pop(&s));
	return 0;
}