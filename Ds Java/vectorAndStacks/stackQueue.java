package Ds.vectorAndStacks;

import java.util.LinkedList;
import java.util.Queue;

//import java.util.*;
public class stackQueue {

	int n;
	Queue <Integer> q1  = new LinkedList();
	Queue <Integer> q2 = new LinkedList();
	
	public stackQueue(){
		n=0;
	}
	
	void push(int val) {
	    q2.add(val);
	    n++;
	    while(!q1.isEmpty()) {
	    	q2.add(q1.peek());
	    	q1.poll();
	    }
	    Queue <Integer> temp = q1;
	    q1=q2;
	    q2=temp;
	    
	}
	void pop() {
		q1.poll();
		n--;
	}
	int top() {
		return q1.peek();
	}
	int size() {
		return n;
	}
	public static void main(String[] args) {
		stackQueue st = new stackQueue();
        st.push(1);
        st.push(2);
        st.push(3);
        
        System.out.println(st.top());
	}

}
