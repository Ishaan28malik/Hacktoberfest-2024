#include <iostream>
using namespace std; 

template <typename T>
class Node {
    public:
    T data;
    Node <T> *next;

    Node(T data) {
        this->data=data;
        next=NULL; 
    }
};

template <typename T> 
class Stack {
    public:
    Node <T> *head;
    int size;
    
    Stack() {
        head=NULL;
        size = 0;
    }


void push(T element) {
    Node <T> *newnode = new Node(element);
    newnode ->next = head;
    head = newnode;
    size++;
}

T pop() {
    if(head==NULL)
        return 0;

    T ans = head ->data; 
    Node <T> *temp = head; 
    head = head->next; 
    delete temp; 
    size--;
    return ans;
}
int getsize() {
    return size;
}

T top() {
    if(head = NULL) 
        return -1;
    
    else {
        return head->data;
    }
}
};