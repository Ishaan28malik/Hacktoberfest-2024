
import java.util.*;
import java.lang.*;
public  class LinkedList{
    public static class linkedList{
        public class Node{
            int data=0;
            Node next=null;   
        }
        private int size=0;
        private Node head=null;
        private Node tail= null;
        //basic===================================
        public int size(){
            return this.size;
        }
        public boolean isEmpty(){
            return this.size==0;
        }
        public void display(){
            Node node=this.head;
            while(node!=null){
                System.out.print(node.data+" ");
                node=node.next;
            }
            System.out.println();
        }
        //add=======================================
        public void addFirst(int data){
            if(this.size==0){
                Node node = new Node();
                node.data=data;
                tail=head=node;
                node.next=null;
                this.size++;
                return;
            }
            Node node= new Node();
            node.data=data;
            node.next=head;
            this.size++;
            head=node;
        }
        public void addAt(int data,int idx) throws Exception{
            if(idx<0 || idx>this.size) throw new Exception("Invalid Index");

            if(isEmpty()) addFirst(data);
            if(idx==this.size){
                addLast(data);
                return;
            }
            Node prev = getAt(idx-1);
            Node node = new Node();
            node.data=data;
            node.next=prev.next;
            prev.next=node;
            this.size++;
        }
        public void addLast(int data){
            if(this.size==0){
                Node node = new Node();
                node.data=data;
                tail=head=node;
                node.next=null;
                this.size++;
                return;
            }

            Node node = new Node();
            node.data=data;
            tail.next=node;
            tail=node;
            this.size++;
        }
        public void print(Node node){
            for(int i=0;i<this.size;i++){
                System.out.println(node.data);
            }
        }
        // remove=================================
        public void removeFirst() throws Exception{
            if(this.size==0){
                throw new Exception("Empty List");
            }
            if(this.size==1){
                head=tail=null;
                this.size--;
                return ;
            }
            Node node= head;
            head= head.next;
            node.next=null;
            this.size--;
        }
        public void removeLast()throws Exception{
            if(isEmpty()) throw new Exception("Empty ");
            else if(this.size==1){
                head=tail=null;
                this.size--;
                return ;
            }
            else{
                Node prev=getAt(this.size-2);
                System.out.println(prev.data);
                tail=prev;
                prev.next=null;
                // tail.next=null;
                this.size--;
            }
        }
        public  void  removeAt(int idx) throws Exception{
            if(isEmpty()) throw new Exception("Empty ");
            else if(idx==1) removeFirst();
            else if(idx==this.size-1) removeLast();
            else{
                Node prev= getAt(idx-1);
                prev.next=prev.next.next;
                this.size--;    
            }
        }

        // get=====================================
        public Node getFirst() throws Exception{
            if(this.size==0){
                throw new Exception("Empty List");
            }
            return head;
        }
        public Node getAt(int idx) throws Exception{
            if(isEmpty()) throw new Exception("Size is Empty");
            else if(idx<0 || idx>this.size) throw new Exception("invalidIndex");
            Node node= head;
            for(int i=0;i<idx;i++){
                node= node.next;
            }
            return node;
        }
        public Node getLast() throws Exception{
            if(this.size==0){
                throw new Exception("Empty List");
            }
            return tail;
        }
    }
    public static void main(String[] args)throws Exception{
        linkedList list= new linkedList();
        int k=0;
        for(int i=0;i<10;i++){
            list.addFirst(i*10);
        }
        list.addAt(120, 4);

        list.display();
    }
} 
