package Ds.Trees;

public class distTree {

	static Node Lca(Node root, int n1 , int n2) {
		if(root==null) {
			return null;
		}
		if(root.data == n1|| root.data ==n2) {
			return root;
		}
		Node left = Lca(root.left , n1 , n2);
		Node right = Lca(root.right , n1, n2);
		
		if(left!= null && right !=null) {
			return root;
		}
		if (left == null && right== null) {
			return null;
		}
		if(left !=null) {
			return Lca(root.left , n1 , n2);
		}
			return  Lca(root.right , n1, n2);
		
	}
	
	static int findDist(Node root , int k , int dist) {
		if(root == null) {
			return -1;
		}
		if(root.data ==k) {
			return dist;
		}
		int left = findDist(root.left , k , dist+1);
		if(left != -1) {
			return left;
		}
		return findDist(root.right , k, dist+1);
	}
	
   static int dist(Node root , int n1 , int n2) {
		Node lca = Lca(root , n1 , n2);
		int d1 = findDist(lca ,n1 , 0);
		int d2 = findDist(lca , n2 , 0);
		
		return d1+d2;
	}
	
	public static void main(String[] args) {
		Node root = new Node(1);
		root.left = new Node(2);
		root.right = new Node(3);
		root.left.left = new Node(4);
		root.right.right = new Node(5);
		 
		
		System.out.println(dist(root , 4 , 5));

	}

}
