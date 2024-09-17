# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next'

class Node:
    
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    
class SinglyLinkedList:
    
    def __init__(self):
        self.head = None
        
    def print(self):
        
        temp = self.head
        
        while(temp != None):
            print(temp.val," ->",end=" ")
            temp = temp.next
        print('NULL\n')

    def addTwoNumbers(self, l1, l2):
        result = temp = Node(0)
        carry = 0
        
        while(l1 or l2 or carry):
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0 
            
            carry, out = divmod(val1 + val2 + carry, 10)
            temp.next = Node(out)
            temp = temp.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return result.next
    
if __name__ == "__main__":
    
    l1 = SinglyLinkedList()
    l1.head = Node(1)
    second = l1.head.next = Node(2, Node(3))       
    third = second.next = Node(3, Node(8))
    fourth = third.next = Node(8, Node(5))
    
    l1.print()
    
    l2 = SinglyLinkedList()
    l2.head = Node(6)
    second = l2.head.next = Node(7, Node(8))       
    third = second.next = Node(8, Node(9))
    fourth = third.next = Node(9, Node(10))
    
    l2.print()
    
    s = SinglyLinkedList()
    result_node =  s.addTwoNumbers(l1.head,l2.head)
    
    s.head = result_node
    print(s.print())
