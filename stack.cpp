C++ Menu Driven Program for Stack Operations Using Arrays
What is Stack?
Stack is a LIFO (last in first out) structure. It is an ordered list of the same type of elements. A stack is a linear list where all insertions and deletions are permitted only at one end of the list.
When elements are added to stack it grow at one end. Similarly, when elements are deleted from a stack, it shrinks at the same end.
It involves various operations such as push,pop,stack empty,stack full and display.
Below is the source code for C++ Menu Driven Program for Stack Operations Using Arrays which is successfully compiled and run on Windows System to produce desired output as shown below :

SOURCE CODE : :
/*  C++ Menu Driven Program for Stack Operations Using Arrays  */


#include<stdio.h>
#include<iostream>

using namespace std;

class Stack
{
int top;
int arr[50];
public:
    Stack()
{
       top=-1;
}

    void push();
    void pop();
    void view();
    int isEmpty();
    int isFull();
};

int Stack::isEmpty()
{
    return (top==(-1)?1:0);
}

int Stack::isFull()
{
    return ( top == 50 ? 1 : 0 );
}

void Stack::push()
{
    if(isFull())
    {
        cout<<"\nSTACK IS FULL { OVERFLOW }";
    }
    else
    {
        int i;
        cout<<"\nEnter an element :: ";
        cin>>i;
        ++top;
        arr[top]=i;
        cout<<"\nInsertion successful.\n";
    }
}

void Stack::pop()
{
    int num;
    if(isEmpty())
    {
            cout<<"\n STACK IS EMPTY [ UNDERFLOW ] ";
    }
    else
    {
    cout<<"\nDeleted item is : "<<arr[top]<<"\n";
    top--;
    }
}

void Stack::view()
{
    if(isEmpty())
    {
            cout<<"\n STACK IS EMPTY [ UNDERFLOW ] ";
    }
    else
    {
    cout<<"\nSTACK :\n";
    for(int i=top;i>=0;i--)
    {
            cout<<arr[i]<<"\n";
    }
    }
}


int main()
{
    Stack s;
    int ch;
    ch=0;
    while(ch!=4)
    {
        cout<<"\n1. Push\n";
        cout<<"2. Pop\n";
        cout<<"3. Display\n";
        cout<<"4. Quit\n";
        cout<<"\nEnter your Choice :: ";
        cin>>ch;

        switch(ch)
        {
            case 1:
                s.push();
                break;

            case 2:
                s.pop();
                break;

            case 3:
                s.view();
                break;

            case 4:
                ch=4;
                cout<<"\nPress any key .. ";
                break;

            default:
                cout<<"\nWrong Choice!! \n";
                break;
        }
    }

    return 0;
}
OUTPUT ::
/*  C++ Menu Driven Program for Stack Operations Using Arrays  */

1. Push
2. Pop
3. Display
4. Quit

Enter your Choice :: 1

Enter an element :: 3

Insertion successful.

1. Push
2. Pop
3. Display
4. Quit

Enter your Choice :: 1

Enter an element :: 5

Insertion successful.

1. Push
2. Pop
3. Display
4. Quit

Enter your Choice :: 1

Enter an element :: 2

Insertion successful.

1. Push
2. Pop
3. Display
4. Quit

Enter your Choice :: 17

Wrong Choice!!

1. Push
2. Pop
3. Display
4. Quit

Enter your Choice :: 1

Enter an element :: 7

Insertion successful.

1. Push
2. Pop
3. Display
4. Quit

Enter your Choice :: 1

Enter an element :: 9

Insertion successful.

1. Push
2. Pop
3. Display
4. Quit

Enter your Choice :: 3

STACK :
9
7
2
5
3

1. Push
2. Pop
3. Display
4. Quit

Enter your Choice :: 2

Deleted item is : 9

1. Push
2. Pop
3. Display
4. Quit

Enter your Choice :: 2

Deleted item is : 7

1. Push
2. Pop
3. Display
4. Quit

Enter your Choice :: 2

Deleted item is : 2

1. Push
2. Pop
3. Display
4. Quit

Enter your Choice :: 2

Deleted item is : 5

1. Push
2. Pop
3. Display
4. Quit

Enter your Choice :: 2

Deleted item is : 3

1. Push
2. Pop
3. Display
4. Quit

Enter your Choice :: 2

 STACK IS EMPTY [ UNDERFLOW ]
1. Push
2. Pop
3. Display
4. Quit

Enter your Choice :: 4

Press any key ..

Process returned 0
