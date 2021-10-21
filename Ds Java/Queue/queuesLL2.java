package Ds.Queue;
import java.util.*;

import Ds.LinkedList.MyLinkedList.Node;
public class queuesLL2  {
	   
	class node{
		public int data;
		public Node next;	
		
		node(int val){
			data = val;
			next=null;
		}
	}
	class queue{
		Node front;
		Node back;
		
		public queue(){
			front = null;
			back = null;
		}
		void push(int x) {
			
			Node n = new Node(x);
			if(front==null) {
				back=n;
				front=n; 
				return; 
			}
			back.next = n;
			back=n;
		}
		void pop() {
			if(front==null) {
          System.out.println("queue underflow");
           return;
		}
			Node toDelete = front;
			front= front.next;
	}
	  int peek() {
			if(front==null) {
				System.out.println("No element in queue");
				return -1;
			}
			return (int) front.data;
		}
	  boolean empty() {
		  if(front==null) {
			  return true;
		  }
		  return false;
	  }
	  
	}
	public static void main(String[] args) {
//		queue q = new queue();
//		q.push(1);
//		q.push(2);
//		q.push(3);
//		
//		System.out.println(q.peek());
//		q.pop();
		
	}
	
}
