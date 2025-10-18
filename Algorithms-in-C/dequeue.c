/*
Here is the code of "Dequeue" that means deletion of elements from the
queue and before deletion we have to check whether the queue is empty or not.

Also deletion is done through "front" pointer.

*/

void dequeue(){
	int element;
	if(isEmpty()){
		printf("Queue is Empty!");
	}
	else{
		element = queue[front];
		front++;
		return element;
	}
}

int isEmpty(){                   // check condition for empty queue.
	if(rear < front){
		return 1;
	}
	else{
		return 0;
	}
}


