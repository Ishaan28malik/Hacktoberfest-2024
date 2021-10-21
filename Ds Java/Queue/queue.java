package Ds.Queue;

import java.lang.reflect.Array;
import java.util.ArrayList;

public class queue {
	private static final int n = 20;
	
	  int [] arr;
	  int front;
	  int back;
	  int size;
	  
	  public queue () {
		arr = new int [n]; 
		front = -1;
		back = -1;
	  }
	  
	  void push(int x) {
		  if(back == n-1) {
			  System.out.println("Queue overflow");
			  return;
		  }
		  back++;
		  arr[back]= x;
		  size++;
		  
		  if(front == -1) {
			  front++;
		  }
	  }
	  void pop() {
		  if(front == -1 || front> back) {
			 System.out.println("No elements in queue");
			  return;
		  }
		  size--;
		  front++;
		  
	  }
	  public void show() {
			System.out.println("The number of elements are: ");
			for(int i=0; i < size; i++) {
				System.out.println(arr[front+ i]+ " ");
			}
		}
	 int peek() {
		  if(front == -1 || front> back) {
				 System.out.println("No elements in queue");
				  return -1;
			  }
		  return arr[front];
	  }
	 boolean empty() {
		 if(front == -1 || front> back) {
			  return true;
		  }
		 return false;
	 }
	 public static void main (String [] args) {
			queue q = new queue();
			q.push(1);
			q.push(2);
			q.push(3);
			q.push(4);
			
		   q.pop();
			q.show();
//			System.out.println(q.peek());
//			q.pop();
		}	
		
	

}
