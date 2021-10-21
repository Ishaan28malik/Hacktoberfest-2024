package Ds.Trees;

import java.util.LinkedList;
import java.util.Queue;

public class RightView {

	static void right(Node root) {
		if(root==null) {
			return ;
		}
		
		Queue<Node> q = new LinkedList<>();
		q.add(root);
		
		while(!q.isEmpty()) {
			
			int n = q.size();
			for(int i = 0; i<n ; i++) {
			    Node curr = q.peek();
				q.poll();
				
				if(i==n-1) {
					System.out.print(curr.data+" ");
				}
				if(curr.left !=null) {
					q.add(curr.left);
				}
				if(curr.right !=null) {
					q.add(curr.right);
				}
			}
		}
	}
	
	
	public static void main(String[] args) {
		Node root = new Node(1);
		root.left = new Node(2);
		root.right = new Node(3);
		root.left.left = new Node(4);
		root.left.right = new Node(5);
		root.right.left = new Node(6);
		root.right.right = new Node(7); 
		
		right(root);

	}

}
