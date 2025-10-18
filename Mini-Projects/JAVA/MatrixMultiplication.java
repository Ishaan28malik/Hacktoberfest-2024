package arrays;

import java.util.Scanner;

public class MatrixMultiplication {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
          Scanner sc = new Scanner(System.in);
          
          int rows = sc.nextInt();
          int cols = sc.nextInt();
          
          
          int a[][] = new int[rows][cols];
          int b[][] = new int[rows][cols];
          
          
          for(int i = 0; i< rows; i++) {
        	  for(int j = 0; j < cols; j++) {
        		  a[i][j] = sc.nextInt();
        	  }
          }
          
          
          for(int i = 0; i < rows; i++) {
        	  for(int j  = 0; j < cols; j++) {
        		  b[i][j] = sc.nextInt();
        	  }
          }
          
          int c[][] = new int[rows][cols];
          
          for(int i = 0; i< rows; i++) {
        	  for(int j = 0;  j < cols; j++) {
        		if(a[j] ==b[i]) {
        			c[i][j]  =  a[i][j] * b[i][j];
        			
        		}
        	 }
         }
          
          
          
	}

}
