package Jobsheet15;

public class Node {
    int m;
    Node prev, next;
    
    Node(Node prev, int data,Node next){
        this.prev = prev;
        this.m = data;
        this.next = next;
    }
    
}
