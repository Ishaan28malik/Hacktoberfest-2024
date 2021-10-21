package Ds.vectorAndStacks;

import java.util.Stack;
import java.lang.Math.*;
public class postfix {

	static int postfix(String s) {
		Stack<Integer> st = new Stack();
		for(int i =0;i<s.length() ; i++) {
			if(s.charAt(i)>='0'&& s.charAt(i)<= '9') {
				st.push(s.charAt(i)-'0');
			}else {
				int op2=st.peek();
				st.pop();
				int op1=st.peek();
				st.pop();
				
				switch(s.charAt(i)) {
				case '+':	
					  st.push(op1+op2);
					  break;
				   case '-':	
						  st.push(op1-op2);
						  break;  
				   case '*':	
						  st.push(op1*op2);
						  break;  
						  
				   case '/':	
						  st.push(op1/op2);
						  break;
				   case '^':	
						  st.push((int) Math.pow(op1, op2));
						  break;
					default:
						break;
				}
			}
		}
		return st.peek();
	}
	
	public static void main(String[] args) {
		System.out.println(postfix("46+2/5*7+"));

	}

}
