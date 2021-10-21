package Ds.Recursion;

public class recursion5 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

//		hanoi(3,'a','c','b');
		System.out.println(remove("aaabbbccdddee "));
	}
   static void hanoi(int n,char src, char dest , char help) {
	if(n==0) {
		return;
	}
	   
	   hanoi(n-1,src,help,dest);
	System.out.println("move from "+src+" to "+dest);
	hanoi(n-1,help ,dest,src);
}
   static String remove(String s) {
	  if(s.length()==0) {
		  return "";
	 }
	  char ch=s.charAt(0);
	  String ans=remove(s.substring(1));
	  
	  if(ch==ans.charAt(0)) {
		  return ans;
	  }
	  return (ch+ans);
   }
}
