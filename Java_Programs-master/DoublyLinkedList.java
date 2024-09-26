import java.util.Scanner;

class Node
{
    protected int data;
    protected Node next,prev;
    
    public Node()
    {
        next = null;
        prev = null;
        data = 0;
    }
    
    public Node(int d, Node n, Node p)
    {
        next = n;
        prev = p;
        data = d;
    }
    
    public void setLinkNext(Node n)
    {
        next = n;
    }
    
    public void setLinkPrev(Node p)
    {
        prev = p;
    }
    
    public Node getLinkNext()
    {
        return next;
    }
    
    public Node getLinkPrev()
    {
        return prev;
    }
    
     public void setData(int d)
    {
        data = d;
    }
    
    public int getData()
    {
        return data;
    }
}

class linkedList
{
    protected Node start;
    protected Node end;
    public int size;
    
    linkedList()
    {
        start = null;
        end = null;
        size = 0;
    }
    
    public boolean isEmpty()
    {
        return start==null;
    }
    
    public int getSize()
    {
        return size;
    }
    
    public void insertAtStart(int val)
    {
        Node nptr = new Node(val, null, null);
        if(start == null)
        {
            start = nptr;
            end = start;
        }
        else
        {
            start.setLinkPrev(nptr);
            nptr.setLinkNext(start);
            start = nptr;
        }
        size++;
    }
    
    public void insertAtEnd(int val)
    {
        Node nptr = new Node(val, null, null);
        if(start == null)
        {
            start = nptr;
            end = start;
        }
        else
        {
            nptr.setLinkPrev(end);
            end.setLinkNext(nptr);
            end = nptr;
        }
        size++;
    }
    
    public void insertAtPos(int val, int pos)
    {
        Node nptr = new Node(val, null, null);
        if(pos == 1)
        {
            insertAtStart(val);
            return;
        }
        Node ptr = start;
        for(int i=2; i<=size; i++)
        {
            if(i==pos)
            {
                Node tmp = ptr.getLinkNext();
                ptr.setLinkNext(nptr);
                nptr.setLinkPrev(ptr);
                nptr.setLinkNext(tmp);
                tmp.setLinkPrev(nptr);
            }
        }
        size++;
    }
    
    public void deleteAtFront()
    {
        if(start == null)
        {
            System.out.println("Cannot perform delete operation.");
        }
        else if(size == 1)
        {
            start = null;
            end = null;
            size = 0;
            return;
        }
        else
        {
            start = start.getLinkNext();
            start.setLinkPrev(null);
            size--;
        }
        return;
    }
    
    public void deleteAtEnd()
    {
        if(start == null)
        {
            System.out.println("Cannot perform delete operation.");
        }
        else if(size == 1)
        {
            start = null;
            end = null;
            size = 0;
            return;
        }
        else
        {
           end = end.getLinkPrev();
           end.setLinkNext(null);
           size--;
        }
    }
    
    public void deleteAtPos(int pos)
    {
      if(start == null)
      {
        System.out.println("Cannot perform delete operation.");
      }
      else
      {
        Node ptr = start.getLinkNext();
        for(int i=2; i<=size;i++)
        {
            if(i == pos)
            {
                Node p = ptr.getLinkPrev();
                Node n = ptr.getLinkNext();
                p.setLinkNext(n);
                n.setLinkPrev(p);
                size--;
                return;
            }
            ptr = ptr.getLinkNext();
        }
      }
    }
    
    public void display()
    {
        System.out.print("\nDoubly Linked List is ");
        if(size == 0)
        {
            System.out.print("Empty\n");
            return;
        }
        if(start.getLinkNext() == null)
        {
            System.out.println(start.getData());
            return;
        }
        Node ptr = start;
        System.out.print(start.getData()+"<->");
        ptr = start.getLinkNext();
        while(ptr.getLinkNext() != null)
        {
            System.out.print(ptr.getData()+"<->");
            ptr = ptr.getLinkNext();
        }
        System.out.print(ptr.getData()+"\n");
    }
}

public class doublylinkedlist
{
	public static void main(String[] args)
	{
		Scanner scan = new Scanner(System.in);
		linkedList list = new linkedList();
		System.out.println("Doubly Linked List\n");
		char ch;
		do
		{
		    System.out.println("\n___Doubly Linked List Operations___");
		    System.out.println("1.Insert at beginning");
		    System.out.println("2.Insert at end");
		    System.out.println("3.Insert at position");
		    System.out.println("4.Delete at front");
		    System.out.println("5.Delete at end");
		    System.out.println("6.Delete at position");
		    System.out.println("\nEnter your choice: ");
		    int choice = scan.nextInt();
		    switch(choice)
		    {
		        case 1:
		            System.out.println("\nEnter integer element to insert:");
		            list.insertAtStart(scan.nextInt());
		            break;
		        case 2:
		            System.out.println("\nEnter integer element to insert:");
		            list.insertAtEnd(scan.nextInt());
		            break;
		        case 3:
		            System.out.println("\nEnter integer element to insert:");
		            int num = scan.nextInt();
		            System.out.println("\nEnter position:");
		            int pos = scan.nextInt();
		            if( pos<1 || pos>list.getSize() )
		              System.out.println("Invalid position\n");
		            else
		              list.insertAtPos(num,pos);
		            break;
		        case 4:
		            list.deleteAtFront();
		            break;
		        case 5:
		            list.deleteAtEnd();
		            break;
		        case 6:
		            System.out.println("\nEnter position");
		            int p = scan.nextInt();
		            if( p<1 || p>list.getSize() )
		              System.out.println("Invalid position\n");
		            else
		              list.deleteAtPos(p);
		            break;
		        default :
		            System.out.println("Enter correct choice\n");
		            break;
		    }
		    //Displaying the Linked List
		    list.display();
		    System.out.println("\nDo you want to continue(Type y for Yes OR n for No)");
		    ch = scan.next().charAt(0);
		}while(ch=='y' || ch=='Y');
	}
}
