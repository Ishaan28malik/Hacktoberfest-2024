#include <iostream>
using namespace std; 

class StackUsingArray {
    int *data;
    int nextIndex; 
    int capacity; 

    public: 
    StackUsingArray(int totalsize) {
        data=new int[totalsize];
        nextIndex=0; 
        capacity=totalsize;
    }


bool isEmpty() {
    if(nextIndex==0)
        return true; 

    else
        return false; 

}

int size() {
    return nextIndex;
}

void push(int element) {
    if(nextIndex==capacity) {
        cout<<"Stack is full";
        return;
    }

    data[nextIndex]= element; 
    nextIndex++;
}

int pop() {
    if(isEmpty()){
        cout<<"Stack is empty"; 
        return 0;
    }

    nextIndex--; 
    return data[nextIndex];
}

int top() {
    return data[nextIndex -1];
}
};
int main() {
    StackUsingArray s(4); 
    s.push(10); 
    s.push(20); 
    s.push(30);
    s.push(40);
    cout<<endl;
    cout<<s.isEmpty();
    cout<<endl;
    cout<<s.size();
    cout<<endl;
    cout<<s.top();
    cout<<endl;
    cout<<s.pop();

    return 0;
}