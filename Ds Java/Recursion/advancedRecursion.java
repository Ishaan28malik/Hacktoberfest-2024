package Ds.Recursion;

public class advancedRecursion {

	public static void main(String[] args) {
		int a[][]= {{1,1,1,1,1,1,1,1},
				   {1,1,1,1,1,1,0,0},
				   {1,0,0,1,1,0,1,1},
				   {1,2,2,2,2,0,1,0},
				   {1,1,1,2,2,0,1,0},
				   {1,1,1,2,2,2,2,0},
				   {1,1,1,1,1,2,1,1},
				   {1,1,1,1,1,2,2,1},};
     floodFill(a, 0 , 0,3,1 );
     printMatrix(a);
	}
	static void floodFill(int a[] [] , int r , int c , int toFill, int prevFill) {
		 int rows=a.length;
	     int cols=a[0].length;
	     
	     if(r<0 || r>=rows || c<0 || c>=cols) {
		return;
	     }
	     if(a[r][c] != prevFill) {
	    	 return;
	     }
	     a[r][c]= toFill;
	     floodFill(a ,r-1 , c,toFill, prevFill);
	     floodFill(a ,r , c-1,toFill, prevFill);
	     floodFill(a ,r+1 , c,toFill, prevFill);
	     floodFill(a ,r , c+1,toFill, prevFill);
	}
	static void printMatrix(int arr[][]) {
		for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr[0].length; j++) {
				System.out.print(arr[i][j]+" ");
			}
			System.out.println();
		}
	}
}

