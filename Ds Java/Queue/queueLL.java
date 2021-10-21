package Ds.Queue;

import java.util.*;

import Ds.LinkedList.MyLinkedList.Node;

public class queueLL<E> {
     
	private Node<E> head, rear;
    public void enqueue(E e) {
    	Node<E> toAdd = new Node(e);
    	if(head==null) {
    		head=rear= toAdd;
    		return;
    	}   	
    	rear.next = toAdd;
    	rear = rear.next;
    }
    public E dequeue(E e) {
    	if(head==null) {
    		return null;
    	}
    	Node<E> temp = head;
    	 head= head.next;
    	 if(head==null) {
    		 rear = null;
    	 }
    	 return temp.data;
    	
    }
}
