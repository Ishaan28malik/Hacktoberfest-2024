package Ds.Queue;

public class myDeque<E> {
	Node head , tail;
	public void addHead(E data) {
		Node <E> toAdd = new Node(data);
		if(head==null) {
			head = tail = toAdd;
			return;
		}
		head.next = toAdd;
		toAdd.previous = head;
		toAdd= head;
		
	}
	public E removeLast() {
		if(head==null) {
			return null;
		}
		Node<E> toRemove = tail;
		tail = tail.next;
		tail.previous = null;
		
		if(tail == null) {
			head = null;
		}
		return toRemove.data;
	}
	
	public static class Node<E>{
		E data;
		Node next , previous;
		
		public Node(E data) {
			this.data = data;
			this.next = this.previous = null;
		}
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
