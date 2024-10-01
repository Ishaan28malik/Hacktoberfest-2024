import java.util.Stack;

public class LeafTraversal {
	
	

	public static boolean isSame(Node root1 , Node root2) {
		
		Stack<Node> s1 = new Stack<Node>();
		Stack<Node> s2 = new Stack<Node>();
		
		s1.push(root1);	
		s2.push(root2);
		
		while(!s1.empty()  || !s2.isEmpty()) {
			
			if(s1.empty() || s2.empty())
				return false;
			
			
			Node temp1 = s1.pop();
			while(temp1 != null && !temp1.isLeaf())
			{
				
				if(temp1.right != null) {
					s1.push(temp1.right);
				}
				if(temp1.left != null) {
					s1.push(temp1.left);
				}
				
				temp1 = s1.pop();
			}
			
			Node temp2 = s2.pop();
			
			while(temp2 != null && !temp2.isLeaf()) {
				
				if(temp2.right != null) {
					s2.push(temp2.right);
				}
				if(temp2.left != null) {
					s2.push(temp2.left);
				}
				
				temp2 = s2.pop();
			}
			
			if(temp1 == null && temp2!=null) {
				return false;
			}
			if(temp1 != null && temp2==null) {
				return false;
			}
			
			if(temp1 != null && temp2 != null) {
				if(temp1.data != temp2.data) 
					return false;
				
		}
		
		
			}
		return true;
		
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Node root1 = new Node(1);
        root1.left = new Node(2);
        root1.right = new Node(3);
        root1.left.left = new Node(4);
        root1.right.left = new Node(6);
        root1.right.right = new Node(7);
 
        Node root2 = new Node(0);
        root2.left = new Node(1);
        root2.right = new Node(5);
        root2.left.right = new Node(4);
        root2.right.left = new Node(6);
        root2.right.right = new Node(7);
 
        if (isSame(root1 , root2))
            System.out.println("Same");
        else
            System.out.println("Not Same");

	}

}

class Node
{
    int data;
    Node left, right;
    public Node(int x)
    {
        data = x;
        left = right = null;
    }
    public boolean isLeaf()
    {
        return (left == null && right == null);
    }
}