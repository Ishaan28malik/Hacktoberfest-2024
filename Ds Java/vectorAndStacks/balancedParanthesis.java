package Ds.vectorAndStacks;

import java.util.Stack;

public class balancedParanthesis {
     static boolean isValid(String s) {
    	 int n = s.length();
    	 Stack<Character> st = new Stack();
    	 boolean ans= true;
    	 for(int i= 0; i < n ; i++) {
    		  if(s.charAt(i)=='{' || s.charAt(i)=='(' || s.charAt(i)=='[' ) {
    			  st.push(s.charAt(i));
    		  }
    		  else if(s.charAt(i)==')') {
    			  if(!st.empty() && st.peek()=='(') {
    				  st.pop();
    			  }else {
    				  ans = false;
    				  break;
    			  }
    		  } else if(s.charAt(i)=='}') {
    			  if(!st.empty() && st.peek()=='{') {
    				  st.pop();
    			  }else {
    				  ans = false;
    				  break;
    			  }
    		  } else if(s.charAt(i)==']') {
    			  if(!st.empty() && st.peek()=='[') {
    				  st.pop();
    			  }else {
    				  ans = false;
    				  break;
    			  }
    		  }
    	 }
    	 if(!st.empty()) {
    		 return false;
    	 }
    	 return ans;
     }
	
	public static void main(String[] args) {
		 String s = "{([])})";
		if(isValid(s)) {
			System.out.println("valid string");
		}else {
			System.out.println("invalid string");
		}
	}
}
