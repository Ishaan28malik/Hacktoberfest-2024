package com.company;

public class DoublyLinkedListPushInsert {
    public static class DoublyLinkedList{
        Node head;
        class Node{
            int data;
            Node prev;
            Node next;

            Node(int d){
                this.data=d;
            }
        }

//        adding at front
    public void push(int newData){
            Node newNode = new Node(newData);

            newNode.next = head;
            newNode.prev=null;

            if (head!=null){
                head.prev=newNode;
            }

            head=newNode;
    }

    //add node before given node
        public void insertBefore(Node nextNode, int newData){
            if (nextNode == null){
                System.out.println("The given node can't be null");
                return;
            }

            Node newNode = new Node(newData);
            newNode.prev=nextNode.prev;
            nextNode.prev=newNode;
            newNode.next=nextNode;

            if (newNode.prev != null){
                newNode.prev.next = newNode;
            }else {
                head = newNode;
            }

        }


        //insert after
        public void InsertAfter(Node prevNode, int newData){
            if (prevNode==null){
                System.out.println("The given previous node cannot be NULL ");
                return;
            }

            Node newNode= new Node(newData);
            newNode.next=prevNode.next;
            prevNode.next=newNode;
            newNode.prev=prevNode;

            if (newNode.next!=null){
                newNode.next.prev=newNode;
            }
        }

        //add at end
        public void append(int newData){
            Node newNode = new Node(newData);
            Node last = head;

            newNode.next=null;
            if (head==null){
                newNode.prev=null;
                head=newNode;
                return;
            }

            while (last.next!= null){
                last=last.next;
            }

            last.next=newNode;
            newNode.prev=last;
        }

        //print the DLL
        public void printList(Node node){
            Node last = null;
            System.out.println("Forward traversal");
            while (node.next!=null){
                System.out.print(node.data+ " ");
                last = node;
                node=node.next;
            }

            System.out.println();
            System.out.println("Traversal in reverse");
            while (last!=null){
                System.out.print(last.data+" ");
                last=last.prev;
            }
        }



    }
    public static void main(String[] args) {
        DoublyLinkedList dll = new DoublyLinkedList();
        dll.append(6);
        dll.push(7);
        dll.push(1);
        dll.append(4);
        dll.InsertAfter(dll.head.next, 8);
        dll.insertBefore(dll.head.next.next,5);

        dll.printList(dll.head);



    }
}
