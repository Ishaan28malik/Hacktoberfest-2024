package Ds.vectorAndStacks;

public class stack {

	private static final int n = 100;
	int [] arr;
	int top;
	
	public stack() {
	arr= new int[n];
	top=-1;
	}	
		
	void push(int x ) {
 	if (top==n-1) {
		System.out.println("stack overflow");
		return;
 	}
 	top++;
 	arr[top]=x;
  }
	void pop() {
		if(top==-1) {
			System.out.println("no element to pop");
			return;
		}
		top--;
	}
	 int Top() {
		if(top==-1) {
			System.out.println("no element in stack");
			return -1;
		}
		
		return arr[top];
	}	
	 boolean empty() {
		 return top==-1;
	 }
}
