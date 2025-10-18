class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key
class Tree:
    def __init__(self,r):
        self.root=r
        self.header = Node(None) #For splay()
    def insert(self,r,key):
        if self.root:
            if key < r.key:
                if r.left==None:
                    r.left=Node(key)
                else:
                    self.insert(r.left,key)
            if key > r.key:
                if r.right==None:
                    r.right=Node(key)                  
                else:
                    self.insert(r.right,key)
        else:
            self.root=r
    def retkey(self):
        return(self.root.key)
    def retroot(self):
        return(self.root)
            
    def splay(self, key):
        le = ri = self.header
        t = self.root
        self.header.left = self.header.right = None
        while True:
            if key < t.key:
                if t.left == None:
                    break
                if key < t.left.key:
                    y = t.left
                    t.left = y.right
                    y.right = t
                    t = y
                    if t.left == None:
                        break
                ri.left = t
                ri = t
                t = t.left
            elif key > t.key:
                if t.right == None:
                    break
                if key > t.right.key:
                    y = t.right
                    t.right = y.left
                    y.left = t
                    t = y
                    if t.right == None:
                        break
                le.right = t
                le = t
                t = t.right
            else:
                break
        le.right = t.left
        ri.left = t.right
        t.left = self.header.right
        t.right = self.header.left
        self.root = t
                    
    def printlist(self,r):
        if r.left:
            self.printlist(r.left)
        print(r.key)
        if r.right:
            self.printlist(r.right)
        
        




r=Node(10)
k=Tree(r)
k.insert(r,6)
k.insert(r,12)
k.insert(r,3)
k.insert(r,34)
k.insert(r,1)
k.insert(r,25)
k.printlist(r)
print("root before splay");
print(k.retkey())
k.splay(6)
print("root after splay")
print(k.retkey())
print("list of elements")
root=k.retroot()
k.printlist(root)
