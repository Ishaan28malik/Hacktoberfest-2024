package Ds.vectorAndStacks;

import java.util.Stack;


public class infixToPost {

	static int prec(char c) {
		if(c=='^') {
			return 3;
		}
		else if(c=='*' || c== '/') {
			return 2;
		}
		else if(c=='+'||c=='-') {
			return 1;
		}
		else {
			return -1;
		}
	}
	
	static String infixP( String s) {
		Stack <Character> st= new Stack();
		String res=" ";
		
		for(int i=0; i<s.length();i++) {
			if((s.charAt(i)>='a' && s.charAt(i)<='z') || (s.charAt(i)>='A' && s.charAt(i)<='Z')) {
				res += s.charAt(i);
			}
			else if(s.charAt(i)=='(') {
				st.push(s.charAt(i));
			}
			else if(s.charAt(i)==')') {
				while(!st.empty() && st.peek()!='(') {
					res+= st.peek();
					st.pop();
				}
				if(!st.empty()) {
					st.pop();
				}
			}
			else {
				while(!st.empty() && prec(st.peek())>prec(s.charAt(i))) {
					res +=st.peek();
					st.pop();
				}
				st.push(s.charAt(i));
			}
		}
		while(!st.empty()) {
			res +=st.peek();
			st.pop();
		}
		return res;
	}
	
	public static void main(String[] args) {
		System.out.println(infixP("(a-b/c)*(a/k-l)"));
//		String exp = "A+B*(C^D-E)";
//        System.out.println("Infix Expression: " + exp);
//        System.out.println("Postfix Expression: " + infixP(exp));

	}

}
