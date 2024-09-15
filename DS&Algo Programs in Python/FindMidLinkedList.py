# -*- coding: utf-8 -*-

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        print('\n Linked list: ')
        temp = self.head
        while temp != None:
            print(temp.val,end='')
            if temp.next != None:
                print('->',end='')
            temp = temp.next
        
    def findmid(self):
        
        slow = fast = self.head
        
        while(fast != None and fast.next!=None):
            
            slow = slow.next
            fast = fast.next.next
        
        return slow
        
        

if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.head = Node(1)
    second = ll.head.next = Node(2)
    third = second.next = Node(3)
    fourth = third.next = Node(4)
    fifth = fourth.next = Node(5)
    sixth = fifth.next = Node(6)
    seventh = sixth.next = Node(7)
    ll.print()
    
    mid = ll.findmid()
    print('\n\nThe middle of linked list is ',mid.val)
