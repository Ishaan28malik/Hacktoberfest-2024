#include <stdio.h>
 
#define MAXSIZE 7
#define TRUE 1
#define FALSE 0 
 
struct Stack {
    int top;
    int array[MAXSIZE];
} st;
 

void initialize() {
 st.top = -1;
}
 

int isFull() {   
    if(st.top >= MAXSIZE-1)
        return TRUE;
    else
        return FALSE;
}
 

int isEmpty() {
 if(st.top == -1)
     return TRUE;
 else
     return FALSE;
}

void push(int num) {
    if (isFull())
        printf("Stack is Full...\n");
    else {
        st.array[st.top + 1] = num;
        st.top++;
    }
}
 

int pop() {
    if (isEmpty())
        printf("Stack is Empty...\n");
    else {
     st.top = st.top - 1;
        return st.array[st.top+1];
    }
}
 

void printStack(){
 if(!isEmpty()){
     int temp = pop();
     printStack();
     printf(" %d ", temp);
     push( temp);
    }
}
void insertAtBottom(int item) {
    if (isEmpty()) {
        push(item);
    } else {
  
      
        int top = pop();
        insertAtBottom(item);
  
       
        push(top);
    }
}
 
void reverse() {
    if (!isEmpty()) {
        
        int top = pop();
        reverse();
  
        
        insertAtBottom(top);
    }
}


int getSize(){
 return st.top+1;
}
 
int main() {
    initialize(st);
    push(1);
    push(2);
    push(3);
    push(4);
    push(5);
    printf("Original Stack\n");
    printStack();
    reverse();
    printf("\nReversed Stack\n");
    printStack();
    return 0;
}
