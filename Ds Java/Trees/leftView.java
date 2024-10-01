package Ds.Trees;

import java.util.LinkedList;
import java.util.Queue;

public class leftView {

	static void left(Node root) {
		if(root==null) {
			return;
		}
		Queue<Node> q = new LinkedList<>();
		q.add(root);
		
		while(!q.isEmpty()) {
			int n = q.size();
			for(int i = 1; i<=n ; i++) {
				Node temp = q.peek();
				q.poll();
				
				if(i==1) {
					System.out.print(temp.data+" ");			
				}
				if(temp.left !=null) {
					q.add(temp.left);
				}
				if(temp.right !=null) {
					q.add(temp.right);
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
		
        left(root);
	}

}
