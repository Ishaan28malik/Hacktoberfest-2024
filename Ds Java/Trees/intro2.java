package Ds.Trees;

class hello extends preAndIn {
	int data;
	hello left;
	hello right;
	
	public hello(int val) {
		data = val;
		left = null;
		right =null;
	}
}

public class intro2 {

	public static void main(String[] args) {
		hello root = new hello(1);
		root.left = new hello(2);
		root.right = new hello(3);
		
		root.left.left = new hello(4);
		root.right.right = new hello(5);

	}

}
