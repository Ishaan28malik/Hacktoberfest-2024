/*package whatever //do not write package name here */
//Stock span problem solved using stack data structure 

import java.util.*;
import java.lang.*;
import java.io.*;

class gfg_stock_span_problem {
	public static void main (String[] args)throws IOException {
		//code
		int i,j,n,t;
            Scanner s = new Scanner(System.in);
	    t = s.nextInt();
          
	    while(t-->0)
	    {
	        int k =0,occr=0;
	        n = s.nextInt();
	        int arr[] = new int[n];
	        Stack<Integer> stack = new Stack<Integer>();
	        int index[] = new int[n];
	        for(i=0 ;i<arr.length ; i++)
	             arr[i] = s.nextInt();
	       int[] res = new int[n];
	        for(i=0 ; i<arr.length ; i++)
	        {
	            if(i==0)
	            {
	                index[i] = -1;
	                stack.push(i);
	            }
	            else
	            {
	                 
	                      while(!stack.isEmpty() && arr[stack.peek()] <= arr[i]) 
                              { 
                                     stack.pop();
                              }
                              if(!stack.isEmpty())
                              {
                                   index[i] = stack.peek();
                                   stack.push(i);
                              }
                              else
                              {
                                   stack.push(i);
                                   index[i] = -1;
                              }  
	                  }
	            }
                for(i=0 ; i<index.length ; i++)
                      System.out.print(i-index[i] + " ");
               System.out.println();
	    }
		
	}
}
