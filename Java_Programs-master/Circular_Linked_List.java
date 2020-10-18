    public class SortList {  
    
      //Represents the node of list.  
      public class Node{  
        int data;  
        Node next;  
        public Node(int data) {  
        this.data = data;  
      }  
    }  
    
    //Declaring head and tail pointer as null.  
    public Node head = null;  
    public Node tail = null;  
    //This function will add the new node at the end of the list.  
    public void add(int data){  
      //Create new node  
      Node newNode = new Node(data);  
      //Checks if the list is empty.  
      if(head == null) {  
       //If list is empty, both head and tail would point to new node.  
      head = newNode;  
      tail = newNode;  
      newNode.next = head;  
    }  
    else {  
      //tail will point to new node.  
      tail.next = newNode;  
      //New node will become new tail.  
      tail = newNode;  
      //Since, it is circular linked list tail will points to head.  
      tail.next = head;  
      }  
    }  
    
    //This function sorts the list in ascending order  
    public void sortList() {  
      //Current will point to head  
      Node current = head, index = null;  
      int temp;  
      if(head == null) {  
      System.out.println("List is empty");  
    }  
    else {  
      do{  
      //Index will point to node next to current  
      index = current.next;  
      while(index != head) {  
      //If current node is greater than index data, swaps the data  
      if(current.data > index.data) {  
      temp =current.data;  
      current.data= index.data;  
      index.data = temp;  
      }  
      index= index.next;  
      }  
      current =current.next;  
      }while(current.next != head);  
      }  
    }  
    
    //Displays all the nodes in the list  
    public void display() {  
      Node current = head;  
      if(head == null) {  
      System.out.println("List is empty");  
    }  
    else {  
     do{  
      //Prints each node by incrementing pointer.  
      System.out.print(" "+ current.data);  
      current = current.next;  
      }while(current != head);  
      System.out.println();  
      }  
    }  
    
    public static void main(String[] args) {  
      SortList cl = new SortList();  
      //Adds data to the list  
      cl.add(70);  
      cl.add(90);  
      cl.add(20);  
      cl.add(100);  
      cl.add(50);  
      //Displaying original list  
      System.out.println("Original list: ");  
      cl.display();  
      //Sorting list  
      cl.sortList();  
      //Displaying sorted list  
      System.out.println("Sorted list: ");  
      cl.display();  
    }
    }  
