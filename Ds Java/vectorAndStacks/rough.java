package Ds.vectorAndStacks;

import java.util.*;

public class rough {

	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
       System.out.println("Enter a string:");
       
       String str = sc.nextLine();
       Stack<Character> st = new Stack<>();
       for(int i=0;i<str.length();i++) {
    	    st.push(str.charAt(i));
       }
       
       System.out.println("reverse of string:");
       
       while(!st.empty()) {
    	   System.out.print(st.pop());
       }
	}

}
