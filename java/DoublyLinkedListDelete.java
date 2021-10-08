package com.company;

public class DoublyLinkedListDelete {

    public static class DLL {
        Node head;

        class Node {
            int data;
            Node prev;
            Node next;

            Node(int d) { data = d; }
        }

        public void push(int newData)
        {
            Node newNode = new Node(newData);

            newNode.next = head;
            newNode.prev = null;

            if (head != null)
                head.prev = newNode;

            head = newNode;
        }


        public void printlist(Node node)
        {
            Node last = null;

            while (node != null) {
                System.out.print(node.data + " ");
                last = node;
                node = node.next;
            }

            System.out.println();
        }

        void deleteNode(Node del)
        {

            // Base case
            if (head == null || del == null) {
                return;
            }

            if (head == del) {
                head = del.next;
            }

            if (del.next != null) {
                del.next.prev = del.prev;
            }

            if (del.prev != null) {
                del.prev.next = del.next;
            }
            return;
        }


        public static void main(String[] args) {
            DLL dll = new DLL();
            dll.push(2);

            dll.push(4);

            dll.push(8);

            dll.push(10);

            System.out.print("Created DLL is: ");
            dll.printlist(dll.head);

            dll.deleteNode(dll.head);

            System.out.print("\nList after deleting first node: ");
            dll.printlist(dll.head);

            dll.deleteNode(dll.head.next);

            System.out.print("\nList after Deleting middle node: ");
            dll.printlist(dll.head);
        }
    }

}
