package Ds.Trees;

public class preAndIn {

	static int search(int inorder[], int start,int end , int curr) {
		for(int i=start; i<= end; i++) {
			if(inorder[i]==curr) {
				return i;
			}
		}
		return -1;
	}
	 static void  inorderPrint(hello root) {
		 if(root==null) {
			 return;
		 }
		 inorderPrint(root.left);
		 System.out.print(root.data +" ");
		 inorderPrint(root.right);
	 }
	
	  static hello buildTree(int preorder[], int inorder[], int start,int end) {
		int idx =0;
		if(start>end ) {
			return null;
		}
		
		int curr = preorder[idx];
		idx++;
		hello he = new hello(curr);
		if(start==end) {
			return he;
		}
		
		int pos = search(inorder , start , end ,curr);
		he.left = buildTree(preorder , inorder ,start , pos-1);
		he.right = buildTree(preorder ,inorder , pos+1 , end);
		return he;
	}
	  
	
	static hello buildTree2(int [] postorder , int inorder [] , int start , int end ) {
		  int  idx =4;
		 if(start > end) {
			 return null;
		 }
		 
		 int val = postorder[idx];
		 idx--;
		 hello curr = new hello(val);
		 if(start == end) {
			 return  curr;
		 }
		 int pos = search(inorder , start , end , val);
		 curr.right = buildTree2(postorder , inorder , pos+1 , end);
		 curr.left = buildTree2(postorder , inorder , start , pos-1);
		 return curr;
	 } 
	 
	public static void main(String[] args) {
		int preorder []= {1 , 2, 4,3,5};
		int postOrder [] = {4 ,2,5,3,1};
        int inorder [] = {4,2,1,5,3};
        
        hello root = buildTree(preorder , inorder, 0 , 4);
        inorderPrint(root);
        
	}

}
