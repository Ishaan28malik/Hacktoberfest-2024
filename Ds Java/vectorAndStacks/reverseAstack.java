package Ds.vectorAndStacks;

import java.util.Stack;

public class reverseAstack {
	
	static void reverse (Stack<Integer> st) {
		if(st.empty()) {
			return;
		}
		
		int ele = st.peek();
		st.pop();
		reverse(st);
		insertAtBottom(st,ele);
	}
	static void insertAtBottom(Stack<Integer> st , int ele) {
		if(st.empty()) {
			st.push(ele);
			return;
		}
		
		int top=st.peek();
		st.pop();
		insertAtBottom(st,ele);
		
		st.push(top);
	}
	
	public static void main(String[] args) {
		Stack<Integer> st = new Stack();
        st.push(1);
        st.push(2);
        st.push(3);
        st.push(4);
        st.push(5);
        
        System.out.println(st);
        reverse(st);
        while(!st.empty()) {
        	System.out.print(st.peek()+" ");
        	st.pop();
        }
	}

}
