package Ds.Queue;

import java.util.Stack;

public class queueStack {
     
//	public class que{
	   Stack<Integer> s1 = new Stack();
	   Stack<Integer> s2 = new Stack();
	   
	 public void push(int x) {
		   s1.push(x);
	   }
	   public int pop() {
		   if(s1.empty() && s2.empty()) {
			   System.out.println("Queue is empty");
			   return -1;
		   }
		   if(s2.empty()) {
			   while(!s1.empty()) {
				   s2.push(s1.peek());
				   s1.pop();
			   }
		   }
		   int top = s2.peek();
		   s2.pop();
		   return top;
	   }
	   boolean isEmpty() {
		   if(s1.empty() && s2.empty()) {
			   return true;
		   }
		   return false;
	   }
//	};
	public static void main(String[] args) {
		 queueStack q = new queueStack();
//		que i = new que();
		q.push(1);
		q.push(2);
		q.push(3);
		q.push(4);
		
		System.out.println(q.pop());
		System.out.println(q.pop());	
		System.out.println(q.pop());	
		System.out.println(q.pop());
		
		System.out.println(q.pop()); 
	}
}
