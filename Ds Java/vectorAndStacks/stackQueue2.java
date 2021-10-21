package Ds.vectorAndStacks;
import java.util.*;
public class stackQueue2 {

	int n;
	Queue <Integer> q1 = new LinkedList();
	Queue <Integer> q2 = new LinkedList();
	
	public stackQueue2(){
		n = 0 ;
	}
	void pop() {
		if(q1.isEmpty()) {
			return;
		}
		while(q1.size() !=1) {
			q2.add(q1.peek());
			q1.poll();
		}
		q1.poll();
		n--;
		
		Queue <Integer> temp = q1;
		q1 = q2;
		q2 = temp;
	}
	void push(int val) {
		q1.add(val);
		n++;
	}
	int top() {
		if(q1.isEmpty()) {
			return -1;
		}
		while(q1.size() !=1) {
			q2.add(q1.peek());
			q1.poll();
		}
		int ans = q1.peek();
		q2.add(ans);
		
		Queue <Integer> temp = q1;
		q1 = q2;
		q2 = temp;
		return ans;
	}
	int size() {
		return n;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
      stackQueue2 st = new stackQueue2();
      st.push(1);
      st.push(2);
      st.push(3);
      st.push(4);
      
      System.out.println(st.top());
      st.pop();
      
      System.out.println(st.top());
		System.out.println(st.size());
	}

}
