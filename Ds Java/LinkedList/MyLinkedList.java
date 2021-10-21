package Ds.LinkedList;

public class MyLinkedList<E> {
 
    Node<E> head;
   public void add(E data) {
    	Node toAdd = new Node(data);
    	
    	if(isEmpty()) {
    		head = toAdd;
    		return;
    	}
    	Node<E> temp = head;
    	while (temp.next != null) {
    		temp = temp.next;
    	}
    	temp.next = toAdd;
    }
    void print() {
    	Node<E> temp = head;
    	while (temp != null) {
    		System.out.print(temp.data+" ");
    		temp = temp.next;
    	}
    }
    public E removeLast() throws Exception {
    	Node<E> temp = head;
    	if(temp==null) {
    		throw new Exception ("no element");
    	}
    	if(temp.next==null) {
    	 Node toRemove = head;
    		head= null;
    		return (E) toRemove.data;
    	}
    	
    	while (temp.next.next != null) {
    		temp = temp.next;
    	}
    	Node toRemove = temp.next;
    	temp.next=null;
    	return  (E) toRemove.data;
    }
    
	public boolean isEmpty(){
		if(head==null) {
			return true;
		}else {
			return false;
		}
	}
	public E getLast() throws Exception{
		Node<E> temp = head;
    	if(temp==null) {
    		throw new Exception ("cannot peek no element");
    	}    	
    	while (temp.next != null) {
    		temp = temp.next;
    	}
    	
    	return  temp.data;
	}
	
	public static class Node<E> {
    	public E data;
    	public Node<E> next;
    	
    	public Node (E data) {
    		this.data = data;
    		next = null;
    	}
    }
	
}
