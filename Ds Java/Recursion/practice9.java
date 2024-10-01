package Ds.Recursion;

import java.util.Scanner;

public class practice9 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		int n = sc.nextInt();	
		int [] arr = new int [n];
		for(int i=0 ; i<n;i++) {
			arr[i]=sc.nextInt();
		}
     int x= sc.nextInt();
     int[] hi = arrIn(arr , 0 , x ,0);
     if(hi.length == 0) {
    	System.out.println("fok");
    	return ;
     }
     for(int i=0 ; i<hi.length ; i++) {
     System.out.print(hi[i]+ " ");
     }
	}
	static int lastIn(int [] arr , int idx , int x) {
		if(arr.length==idx) {
			return -1;
		}
		
		int small = lastIn(arr , idx+1 , x);
	   if(small==-1) {
		   if(arr[idx]==x) {
			   return idx;
		   }else {
			   return-1;
		   }
	   }else {
		   return small;
	   }
		
	}
	static int [] arrIn(int [] arr , int idx , int x , int fsf) {
		if(arr.length==idx) {
			return new int[fsf];
		}
		
		if(arr[idx]==x) {
			int [] indi = arrIn(arr , idx+1 , x , fsf+1);
			indi[fsf]=idx;
			return indi;
		  }else {
			  int [] indi = arrIn(arr , idx+1 , x , fsf);
			  return indi;
		  }
		  
	}
}
