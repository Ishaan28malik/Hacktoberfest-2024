 package Ds.vectorAndStacks;

import Ds.LinkedList.MyLinkedList;

public class myStack <E>{
     
	private MyLinkedList<E> ll = new MyLinkedList();
	
	void push(E e) {
		ll.add(e);
	}
	E pop() throws Exception {
		if(ll.isEmpty()) {
			throw new Exception("error");			
		}
		return ll.removeLast();
	}
	E peek() throws Exception {
		if(ll.isEmpty()) {
			throw new Exception("error");			
		}
		return ll.getLast();
	}
	
}
