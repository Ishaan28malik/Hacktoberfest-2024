# -*- coding: utf-8 -*-


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
        
    def common(self, l1, l2):
        common_list = []
        s = set() #unique elements
        
        temp1 = l1.head 
        while(temp1 != None):
            s.add(temp1.val)
            temp1 = temp1.next
            
        temp2 = l2.head
        while(temp2 != None):
            if temp2.val in s:
                common_list.append(temp2.val)
            temp2 = temp2.next
        
        return common_list
        
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
    print('Common elements: ',s.common(l1,l2))
