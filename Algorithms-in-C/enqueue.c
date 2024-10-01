/*
Queue is a type of Data Structure which follows the rule "FIFO" i.e. (First in First Out).
   Ex: A queue of people standing to buy a movie ticket. The first person enters to buy and will leave the 
        queue first.

Here insertion and deletion is done through two pointers called rear and front.
"Rear" is used for insertion.
"Front" is used for deletion.

Also once the first element gets inserted the front pointer will be fixed and
 more insertions will be done through rear.


*/


#include<stdio.h>
#include<stdlib.h>

#define max 100
int queue[max];

int front = -1; // Initializing the pointers to -1
int rear = -1;

void enqueue( int element){
	if(isFull()){
		printf("Queue is Full!");
	}
	else{
		rear++;
		queue[rear] = element;
	}
}

int isFull(){
	if(rear >= max-1){
		return 1;
	}
	elase{
		return 0;
	}
}

