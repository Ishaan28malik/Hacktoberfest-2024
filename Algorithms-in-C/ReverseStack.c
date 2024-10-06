#include <stdio.h>

#define MAXSIZE 7
#define TRUE 1
#define FALSE 0

struct Stack {
    int top;
    int array[MAXSIZE];
} st;

// Function to initialize the stack
void initialize() {
    st.top = -1;
}

// Check if the stack is full
int isFull() {
    return st.top >= MAXSIZE - 1;
}

// Check if the stack is empty
int isEmpty() {
    return st.top == -1;
}

// Push element to the stack
void push(int num) {
    if (isFull()) {
        printf("Stack is Full...\n");
    } else {
        st.array[++st.top] = num; // Pre-increment and assign
    }
}

// Pop element from the stack
int pop() {
    if (isEmpty()) {
        printf("Stack is Empty...\n");
        return -1; // Return a dummy value when empty
    } else {
        return st.array[st.top--]; // Post-decrement and return
    }
}

// Print the stack recursively
void printStack() {
    if (!isEmpty()) {
        int temp = pop();
        printStack();
        printf(" %d ", temp);
        push(temp); // Restore the stack order
    }
}

// Insert element at the bottom of the stack
void insertAtBottom(int item) {
    if (isEmpty()) {
        push(item);
    } else {
        int temp = pop();
        insertAtBottom(item);
        push(temp);
    }
}

// Reverse the stack using recursion
void reverse() {
    if (!isEmpty()) {
        int temp = pop();
        reverse();
        insertAtBottom(temp);
    }
}

// Get the current size of the stack
int getSize() {
    return st.top + 1;
}

// Testing the functions
int main() {
    initialize(); // Initialize the stack
    
    // Pushing elements to the stack
    push(1);
    push(2);
    push(3);
    push(4);
    push(5);
    
    printf("Original Stack: \n");
    printStack(); // Print original stack
    
    reverse(); // Reverse the stack
    
    printf("\nReversed Stack: \n");
    printStack(); // Print reversed stack
    
    // Testing size
    printf("\nStack Size: %d\n", getSize());
    
    return 0;
}
