// Author : Ankush.S.Shetkar
// Github id : lifeLessCoder 

#include <stdio.h>
#include <stdlib.h>
#define STACK_MAX 25

typedef struct 
{
	char arr[STACK_MAX];
	int top;
}Stack;

int isEmpty(Stack * stack){
	if(stack->top == -1)
		return 1;
	return 0;
}

int isFull(Stack * stack){
	if(stack->top == STACK_MAX - 1)
		return 1;
	return 0 ;
}

void initStack(Stack * stack){
	stack->top = -1;
}

void push(Stack * stack, char c){
	if(isFull(stack)){
		printf("Stack full!\n");
		return;
	}
	stack->arr[++stack->top] = c;
}

char pop(Stack * stack){
	if(isEmpty(stack))
		return '\0';
	return stack->arr[stack->top--];
}

char peek(Stack * stack){
		if(isEmpty(stack))
		return '\0';
	return stack->arr[stack->top];
}

int isOpnd(char c){
	if((c >= '0' && c <= '9') || (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'))
		return 1;
	return 0;
}

int isOperator(char c){
	switch(c){
		case '+':
		case '-':
		case '*':
		case '/':
		case '^':
		case '%':return 1;
		default:return 0;
	}
}

int prcd(char c){
	switch(c){
		case '^':return 2;
		case '*':
		case '/':
		case '%':return 1;
		case '+':
		case '-':return 0;
	}
}

int main()
{
	Stack * stack = (Stack *)malloc(sizeof(Stack));
	initStack(stack);
	char arr[STACK_MAX], preExp[STACK_MAX];
	int i = -1,j = -1,size;
	printf("Enter an infix expression :");
	while((arr[++i] = getchar()) != '\n');
	--i;
	while(i >= 0){
		if(isOpnd(arr[i])){
			preExp[++j] = arr[i];
		}else if(isOperator(arr[i])){
			if(isEmpty(stack) || peek(stack) == ')'){
				push(stack, arr[i]);
			}
			else{
				while(prcd(arr[i]) < prcd(peek(stack))){
					preExp[++j] = pop(stack);
				}
				push(stack,arr[i]);
			}
		}else if(arr[i] == ')'){
			push(stack, arr[i]);
		}else if(arr[i] == '('){
			while(peek(stack) != ')'){
				preExp[++j] = pop(stack);
			}
			pop(stack); 
		}
		--i;
	}
	while(!isEmpty(stack)){
		preExp[++j] = pop(stack);
	}
	printf("The prefix expression is : ");
	for(int i = j; i >= 0; i--)
	printf("%c", preExp[i]);
	printf("\n");
	return 0;
}