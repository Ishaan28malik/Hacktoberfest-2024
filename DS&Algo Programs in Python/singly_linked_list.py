
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def print_ll(start):
    if start:
        temp = start
        i=1
        while temp:
            print(f"Node at {i} is {temp.data}")
            i=i+1
            temp=temp.next
    else: print("No element in LL!!!")

start = None
def create_ll():
    start = None
    temp = None
    start = Node(input("Enter atleast one element: "))
    print("To exit stop entering elements enter bye")
    temp = start
    while True:
        data = input("Enter element: ")
        if data == 'bye':
            break
        temp.next = Node(data)
        temp = temp.next

    return start



def append_ll(start):
    if start:

        temp = start
        while temp.next:
            temp = temp.next
        temp.next = Node(input("Enter atleast one element: "))
        temp = temp.next
        print("To exit stop entering elements enter bye")
        while True:
            data = input("Enter element: ")
            if data == 'bye':
                return
            temp.next = Node(data)
            temp = temp.next
        
    else:
        print("No elements in list")


def search(start, key):
    
    temp = start
    i=1
    while temp:
        if temp.data==key:
            return i
        else:
            i=i+1
            temp = temp.next
    return
    
def delete_from_ll(start, key):
    temp = start
    prev = None
    while temp and temp.data != key:
        prev = temp
        temp = temp.next
    #print("p= ",prev.data,"c=",temp.data)
    if temp:
        if temp == start:
            start = temp.next
            print(f"Node with data {temp.data} deleted successfully!!!")
            temp.data = None
            temp.next = None
            return start
        prev.next = temp.next
        temp.next = None
        print(f"Node with data {temp.data} deleted successfully!!!")
        temp.data = None
        temp = None
        #print("p= ",prev.data,"c=",temp.data)
        return start
            
            
        
    print("No such element found")
    return start


def print_reverse(pos,node):
    if node:
        print_reverse(pos+1,node.next)
        print(f"Node at {pos} is {node.data}")

def reverse_ll(start):
    prev = None
    curr = start
    nextn = start.next

    while curr:
        curr.next = prev
        prev = curr
        curr = nextn
        if nextn:
            nextn = nextn.next
    start = prev
    print("LL Reversed!!!")
    return start


def options():
    start = None
    while True:
        print("="*40)
        n = int(input("1 - Create LL\n2 - Print LL\n3 - Append\n4 - Exit\
\n5 - Search\n6 - Delete node\n7 - Print reverse\n8 - Reverse LL\n"))
        if n ==1:
            start = None
            start = create_ll()
        elif n == 2:
            print_ll(start)
        elif n ==3 :
            append_ll(start)
        elif n ==4:
            print("Bye !!!")
            return
        elif n == 5:
            if start:
                key = input("Enter element to be searched")
                pos = search(start, key)
                if pos:
                    print(f"Element found at {pos}")
                else:
                    print("Element not found")
            else:
                print("Can't search! No elements in list.")
        elif n ==6:
            if start:
                key = input("Enter element to be deleted")
                start = delete_from_ll(start, key)
            else:
                print("Can't delete! No elements in list.")
        elif n == 7:
            if start:
                print_reverse(1, start)
            else:
                print("No elements in list!!!")
        elif n==8:
            if start:
                start = reverse_ll(start)
            else:
                print("Can't reverse! No elements in list.")
        else :
            print("Please select valid options!!!")
            

if __name__ =="__main__":
    options()
