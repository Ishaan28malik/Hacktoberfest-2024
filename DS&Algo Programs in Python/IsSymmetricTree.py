# -*- coding: utf-8 -*-


class TreeNode():
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution():
    def isSymmetric(self, root):
        
        if root is None:
            return True   #tree with no node is also symmetric
        
        def check(left, right):
            
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            
            return (left.val == right.val 
                    and check(left.right, right.left)
                    and check(left.left, right.right))
        
        return check(root.left, root.right)
    
    
'''   #Example for not symmetric
root = TreeNode(1,TreeNode(2), TreeNode(2))
root.left = TreeNode(2, None, TreeNode(3))
root.right = TreeNode(2, None, TreeNode(3))
'''
       #Example for symmetric
root = TreeNode(1, TreeNode(2), TreeNode(2))
root.left = TreeNode(2, TreeNode(3), TreeNode(4))
root.right = TreeNode(2, TreeNode(4), TreeNode(3))

s = Solution()
symmetric = s.isSymmetric(root)
print("The given tree is symmetric: ", symmetric)
