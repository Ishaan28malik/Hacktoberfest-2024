package Ds.vectorAndStacks;

import java.util.Stack;

public class reverseStack {

	static void reverseSen(String s) {
	    
		Stack <String> st = new Stack();
	     for(int i=0; i<s.length();i++) {
			String word= "";
			while(s.charAt(i)!=' ' && i<s.length()) {
				word +=s.charAt(i);
				i++;
			}
			st.push(word);
		  }
	     while(!st.empty()) {
	    	System.out.print(st.peek() + " "); 
	    	st.pop();
	     }System.out.println();
	}
	
	public static void main(String[] args) {
	
       String s="hey, how are you doing?";
       reverseSen(s);
	}

}
