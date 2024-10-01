package Ds.Trees;

public class height {

	static int height(Node root) {
		if(root==null) {
			return 0;
		}
		
		int lheight = height(root.left);
		int rheight = height(root.right);
		
		return Math.max(lheight , rheight)+1;
	}
	static int diameter(Node root) {
		if(root == null) {
			return 0;
		}
		
		int lheight = height(root.left);
		int rheight = height(root.right);
		int currDia = lheight + rheight +1;
		
		int ldia = diameter(root.left);
		int rdia = diameter(root.right);
		return Math.max(currDia, Math.max(ldia, rdia));
	}
	static int Diameter(Node root , int height) {
		if(root == null) {
			height = 0;
			return 0;
		}
		int lh=0 , rh = 0;
		int ld = Diameter(root.left , lh);
		int rd = Diameter(root.right , rh);
		
		int currDia = lh + rh +1;
		height = Math.max(lh, rh)+1;
		return Math.max(currDia, Math.max(ld, rd));
	}
	
	public static void main(String[] args) {
		Node root = new Node(1);
		root.left = new Node(2);
		root.right = new Node(3);
		root.left.left = new Node(4);
		root.left.right = new Node(5);
		root.right.left = new Node(6);
		root.right.right = new Node(7); 
		
		int height = 0;
		System.out.println(Diameter(root , height));

	}

}
