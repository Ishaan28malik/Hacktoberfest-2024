package Ds.Queue;
import java.util.*;
public class Deque {

	public static void main(String[] args) {
		ArrayDeque<Integer> dq = new ArrayDeque();
	    dq.addFirst(12);
	    dq.addFirst(23);
	    dq.addFirst(42);
	    dq.pop();
	   
	    System.out.println(dq.peek());
		
	}

}
