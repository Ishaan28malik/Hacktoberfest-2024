class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList():
    def __init__(self):
        self.head=None
        
    def length(self):
        c=0
        curr=self.head
        while curr:
            c=c+1
            curr=curr.next
        return c
    
    def print_list(self):
        curr_node=self.head
        while curr_node:
            if curr_node.next==None:
                print(curr_node.data)
                break
            else:
                print(curr_node.data,end='-> ')
            curr_node=curr_node.next
        
    def add(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            last_node=self.head
            while last_node.next:
                last_node=last_node.next
            last_node.next=new_node
            
    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    
    def midpend(self,data,pos):
        new_node=Node(data)
        curr_node=self.head
        while curr_node.data!=pos:
            curr_node=curr_node.next
        new_node.next=curr_node.next
        curr_node.next=new_node
        
    def delete(self,data):
        if self.head==data:
            self.head=self.head.next
        else:
            curr_node=self.head
            while curr_node.next.data!=data:
                curr_node=curr_node.next
            curr_node.next=curr_node.next.next
            
    def swap(self,a,b):
        curr1=self.head
        prev1=None
        while curr1 and curr1.data!=a:
            prev1=curr1
            curr1=curr1.next
        curr2=self.head
        prev2=None
        while curr2 and curr2.data!=b:
            prev2=curr2
            curr2=curr2.next
        prev1.next=curr2
        temp=curr2.next
        curr2.next=curr1.next
        prev2.next=curr1
        curr1.next=temp
    
    def reverse(self):
        curr=self.head
        prev=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        self.head=prev
    
    def merge(self,b):
        p=self.head
        q=b.head
        if p.data<=q.data:
            s=p
            p=s.next
        else:
            s=q
            q=s.next
        newhead=s
        while p and q:
            if p.data<=q.data:
                s.next=p
                s=p
                p=s.next
            else:
                s.next=q
                s=q
                q=s.next
        if not p:
            while q:
                s.next=q
                s=q
                q=s.next
        if not q:
            while p:
                s.next=p
                s=p
                p=s.next
        return newhead
    
    def remove_duplicates(self):
        d={}
        curr_node=self.head
        prev_node=None
        while curr_node:
            if curr_node.data not in d:
                d[curr_node.data]=1
                prev_node=curr_node
                curr_node=curr_node.next
            else:
                curr_node=curr_node.next
                prev_node.next=curr_node
                
    def rotate(self,k):
        curr_node=self.head
        #p=None
        if k>2:
            while k:
                curr_node=curr_node.next
                if k==2:
                    p=curr_node
                k=k-1
            p.next=None
            q=curr_node
           # print(q.data)
            while curr_node.next:
                curr_node=curr_node.next
            curr_node.next=self.head
            self.head=q
        else:
            while curr_node.next:
                curr_node=curr_node.next
            curr_node.next=self.head
            p=self.head
            self.head=self.head.next
            p.next=None
            

a=LinkedList()
a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.add(3)
a.add(6)
a.remove_duplicates()
a.print_list()
#a.rotate(1)
a.rotate(4)
a.print_list()

        
    
