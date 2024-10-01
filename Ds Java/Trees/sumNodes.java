package Ds.Trees;

public class sumNodes {

	static int Nodes(Node root) {
		if(root==null) {
			return 0;
		}
		return Nodes(root.left)+ Nodes(root.right)+1 ;
	}
	
	static int sumNode(Node root) {
		if(root==null) {
			return 0;
		}
		return sumNode(root.left)+sumNode(root.right)+ root.data;
	}
	
	public static void main(String[] args) {
		Node root = new Node(1);
		root.left = new Node(2);
		root.right = new Node(3);
		root.left.left = new Node(4);
		root.left.right = new Node(5);
		root.right.left = new Node(6);
		root.right.right = new Node(7); 
		System.out.println(sumNode(root));

	}

}
