#include <stdio.h>
#include <stdlib.h>
struct Stack{
  int top;
  int N;
  int *arr;
};
struct Stack *create_stack(){
  struct Stack *n=(struct Stack*)malloc(sizeof(struct Stack));
  n->top=-1;
  printf("Enter capacity of Stack\n");
  scanf("%d",&n->N);
  n->arr=malloc((n->N)*sizeof(n->arr));
  return n;
}
int isFull(struct Stack *a){
  return a->top==a->N-1;
}
int isEmpty(struct Stack *a){
  return a->top==-1;
}
void push(struct Stack *a,int num){
  if(isFull(a)){
    printf("Stack is full\n");
    return;
  }
  else
  a->arr[++a->top]=num;
}
void pop(struct Stack *a){
  if(isEmpty(a)){
    printf("\nEmpty stack\n");
    return;
  }
  else{
    printf("\nDeleted element=%d\n",a->arr[a->top]);
    a->top=a->top-1;
  }
}
int main() {
  /* code */
  struct Stack *st=create_stack();
  while(1){
    int item;
    printf("\nEnter a number to be pushed into stack\n");
    scanf("%d",&item);
    push(st,item);
    char ch;
    printf("Press 0 to exit or any other key to continue pushing numbers in stack\n");
    ch=getche();
    if(ch=='0'){
    break;
  }
  }
  while(1){
    char ch;
    printf("\nPress 0 to exit or any other key to continue popping numbers in stack\n");
    ch=getche();
    if(ch=='0'){
    break;
  }
    pop(st);
  }
  printf("\nThe final stack frame\n");
  for(int i=0;i<=st->top;i++){
    printf("%d ",st->arr[i]);
  }
  return 0;
}
