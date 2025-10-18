/*
Let's display th elements of a Queue.

Now, you already know that we have to check for the condition if the queue has elements or 
it is already empty.

and the "isEmpty()" function, we have describe before.

*/


void display(){
	int element;
	int i;
	if(isEmpty()){
		printf("Queue is Empty!");
	}

	else{
		for(i=front; i<= rear; i++){
			printf("%d",queue[i]);
		}
	}
}

/**
We can also print the data in the reverse order i.e. from rear to front direction.
Just reverse the loop.

*/