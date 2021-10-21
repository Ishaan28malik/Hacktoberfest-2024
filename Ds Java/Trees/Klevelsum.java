package Ds.Trees;

import java.util.LinkedList;
import java.util.Queue;

public class Klevelsum {

	static int sumAtK(Node root , int k) {
		if(root ==null) {
			return -1;
		}
		Queue<Node> q = new LinkedList<>();
		q.add(root);
		q.add(null);
		int level=0;
		int sum = 0;
		
		while(!q.isEmpty()){
			Node node = q.peek();
			q.poll();
			if(node != null) {
               if(level == k) {
            	   sum += node.data;
               }
               if(node.left != null) {
            	   q.add(node.left);
               }
               if(node.right !=null) {
					q.add(node.right);
				}
			}
			else if(!q.isEmpty()){
				q.add(null);
				level++;
			}
		}
		return sum;
	}
	
	public static void main(String[] args) {
		Node root = new Node(1);
		root.left = new Node(2);
		root.right = new Node(3);
		root.left.left = new Node(4);
		root.left.right = new Node(5);
		root.right.left = new Node(6);
		root.right.right = new Node(7);
		
		System.out.println(sumAtK(root, 2));
	}

}
