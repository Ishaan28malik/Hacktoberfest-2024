from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None   

class Solution:
    def hasCycle(self,head:Optional[ListNode])->bool:

        #if no linkedlist or a single node linkedlist
        if head is None or head.next is None:
            return False
        
        slow=head
        fast=head
    
        while slow!=fast:
            if fast is None or fast.next is None:
                return False
            
            slow=slow.next #goes to next node
            fast=fast.next.next #goes to next to next node
        
        return True
    
# Create some nodes for a linked list
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)

# Link the nodes together
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

# Optionally create a cycle
# Uncomment the line below to create a cycle
node6.next = node3

# Create an instance of the Solution class
solution = Solution()

# Check if the linked list has a cycle
result = solution.hasCycle(node1)

# Print the result
print("Cycle detected!" if result else "No cycle detected")
