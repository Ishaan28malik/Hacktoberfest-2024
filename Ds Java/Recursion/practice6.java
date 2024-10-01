package Ds.Recursion;

public class practice6 {

	public static void main(String[] args) {
//		System.out.println(moveX("abxxchxxix"));
		Subseq("AB","");
		System.out.println();
	}
	static String moveX(String s) {
		
		if(s.length()==0) {
			return "";
		}
		char ch=s.charAt(0);
		String ans = moveX(s.substring(1));
		
		if(ch=='x') {
			return ans+ch;
		}
		return ch+ans;
	}
	static void subseq(String s , String ans) {
		if(s.length()==0) {
			System.out.println(ans);
			return;
		}
		
		char ch=s.charAt(0);
		String ros=s.substring(1);
		
		subseq(ros,ans);
		subseq(ros,ans+ch);
	}
	static void Subseq(String s , String ans) {
		if(s.length()==0) {
			System.out.println(ans);
			return;
		}
		char ch=s.charAt(0);
		int code = ch;
		String ros=s.substring(1);
		
		Subseq(ros , ans);
		Subseq(ros , ans+ch);
		Subseq(ros , ans + Integer.toString(code));
	}

}
