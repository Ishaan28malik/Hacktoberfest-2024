package Ds.Queue;

public class arrayQueue {

	int queue[] = new int [5];
	int size;
	int front;
	int back;
	
	public void enQueue(int data) {
		if(!isFull()) {
		queue[back] = data;
		back = (back +1)%5;
		size++;
		}else {
			System.out.println("Queue is full"); 
		}
	}
	public int deQueue() {
		int data = queue[front];
		if(isEmpty()) {
		    front= (front + 1)%5;
		    size--;
		}else {
			System.out.println("queue is empty");
		}
		return data;
	}
	
	public void show() {
		System.out.println("The number of elements are: ");
		for(int i=0; i < size; i++) {
			System.out.println(queue[(front+ i)%5]+ " ");
		} 
	}
	public int getSize() {	
		return size;
	}
	public boolean isEmpty() {
		return getSize()==0;
	}
	public boolean isFull() {
		return getSize()==5;
	}
	public static void main(String[] args) {
		
		
	}

}
