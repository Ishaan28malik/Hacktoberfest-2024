package Ds.Recursion;

public class practice7 {

	public static void main(String[] args) {
		 keypad("2","");
		
	}
	static String keypadArr[]= {"","","abc","def","ghi","jkl","mno","pqrs","tuvw","xyz"};
	 static void keypad(String s , String ans) {
		 if(s.length()==0) {
			System.out.println(ans);
			return;
		 }
		 
		 char ch=s.charAt(0);
		 String code=keypadArr[ch-'0'];
		 String ros=s.substring(1);
		 String [] str = new String [] {code};
		 
		 for(int i=0;i<code.length();i++) {
			 keypad(ros , ans+str[i]);
		 }
	 }

}
