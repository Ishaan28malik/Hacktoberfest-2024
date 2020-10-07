class BinaryTree:
    """
        A Binary Tree is a node-based binary tree data structure having atmost 2 child nodes in each parent node
        The left subtree of a node contains only nodes with keys lesser than the node’s key.
        The right subtree of a node contains only nodes with keys greater than the node’s key.
        The left and right subtree each must also be a binary tree.
        In this class,
        The right subtree of a node contains nodes with keys greater or equal to the node’s key.
    """

    def __init__(self, key:int):
        '''
        Create a parent node of no child
        '''
        self.key = key
        self.leftNode = None
        self.rightNode = None

    def smallestElement(self):
        '''
        Returns the smallest key of the tree
        '''
        if self.leftNode is None:
            return self.key #base condition for recursion
        else:
            return self.leftNode.smallestElement()

    def largestElement(self):
        '''
        Returns the largest key of the tree
        '''
        if self.rightNode is None:
            return self.key #base condition for recursion
        else:
            return self.rightNode.largestElement()

    def addKey(self,key:int):
        '''
        Add a key element in the binary tree
        '''
        if key<self.key: #move to left tree
            if self.leftNode is None:
                self.leftNode = BinaryTree(key)
            else:
                self.leftNode.addKey(key)
        else: #move to right tree
            if self.rightNode is None:
                self.rightNode = BinaryTree(key)
            else:
                self.rightNode.addKey(key)

    def removeKey(self,key:int):
        '''
        removes a key from the tree. Returns the removed tree and status(boolean)
        if removal is success:
            return (True,Tree)
        else:
            return (False,Tree)
        '''

        status = False
        retValue = self

        if key<self.key and self.leftNode is not None:#move and update left Tree
            (status,self.leftNode) = self.leftNode.removeKey(key)
        elif key>self.key and self.rightNode is not None:#move and update right Tree
            (status,self.rightNode) = self.rightNode.removeKey(key)
        elif self.key==key:#this node has to be removed
            status=True
            if self.leftNode is None and self.rightNode is None:#no child
                retValue = None
            elif self.leftNode is None:#has only right child
                retValue = self.rightNode
            elif self.rightNode is None:#has only left child
                retValue = self.leftNode
            else:#has 2 childs.
                #copy the smallestElement of right tree and remove that node
                self.key = self.rightNode.smallestElement()
                self.rightNode = self.rightNode.removeKey(self.key)
                retValue=self
        else:#no node found
            status = False

        return (status,retValue)

    def search(self,key:int,rootLevel=0):
        '''
        Searches for the key int the binary tree.
        Return a tuple of state(boolean) and rootLevel
        eg:
            upon finding the element
            returns (True,rootLevel)

            upon not finding the element
            return (False,-1)
        '''
        if key == self.key:#found the element
            return (True,rootLevel)
        elif key>self.key and self.rightNode is not None:
            #move to the right sub tree
            return self.rightNode.search(key,rootLevel+1)
        elif key<self.key and self.leftNode is not None:
            #move to the left sub tree
            return self.leftNode.search(key,rootLevel+1)
        else: #no such element
            return (False,-1)

    def inOrderTraversal(self):
        '''
        Traversal takes place as :left tree -> current node-> right tree
        '''
        if self.leftNode is not None:
            self.leftNode.inOrderTraversal()

        print(f"{self.key} ",end='')

        if self.rightNode is not None:
            self.rightNode.inOrderTraversal()

    def preOrderTraversal(self):
        '''
        Traversal takes place as :current -> left tree-> right tree
        '''
        print(f"{self.key} ",end='')

        if self.leftNode is not None:
            self.leftNode.inOrderTraversal()

        if self.rightNode is not None:
            self.rightNode.inOrderTraversal()

    def postOrderTraversal(self):
        '''
        Traversal takes place as :left tree -> right tree -> current
        '''
        if self.leftNode is not None:
            self.leftNode.inOrderTraversal()

        if self.rightNode is not None:
            self.rightNode.inOrderTraversal()

        print(f"{self.key} ",end='')

    def treePrint(self,level=1):
        '''
        Prints a Binary tree as

        node1 -> node2 -> null
        |        null
        node3 -> null
        null

        where:  left(node1)=node2  and right(node1)=node3
                left(node2)=right(node2)=left(node3)=right(node3)=null
                ie, no childs for node2 and node3
        '''

        print("%-4d -> "%(self.key),end='')

        if self.leftNode is None:
            print("null")
        else:
            self.leftNode.treePrint(level+1)

        print("|       "*(level-1),end='')

        if self.rightNode is None:
            print("null")
        else:
            self.rightNode.treePrint(level)





#Input from user as a list
listIn = list(map(int,input('Enter the space separated element to tree : ').strip().split()))

#creating binayr Tree
BST = BinaryTree(listIn[0]) #New binary tree created
for n in listIn[1::]:
    BST.addKey(n) #adding rest of the input elements

#Print the smallest and largest element
print(f"Smallest element is {BST.smallestElement()}")
print(f"Largest element is {BST.largestElement()}")

#Binary tree traversal
print("InOrderTraversal : ",end='')
BST.inOrderTraversal()
print("\nPreOrderTraversal : ",end='')
BST.preOrderTraversal()
print("\nPostOrderTraversal : ",end='')
BST.postOrderTraversal()

#removing a element
rmKey = int(input('\n\nEnter a key to remove : '))
(status,BST) = BST.removeKey(rmKey)
if status:
    print(f"Element {rmKey} is removed")
else:
    print(f"Could not remove {rmKey}. Element not found")

#Print the tree
BST.treePrint(1)


#searching an element
searchKey = int(input('\n\nEnter a key to search : '))
(status,level) = BST.search(searchKey,0) #assume root level as 0
if status:
    print(f"Found element {searchKey} at the level {level}")
else:
    print("Not found")
