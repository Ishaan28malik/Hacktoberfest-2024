package Ds.Recursion;

public class practice4 {

	public static void main(String[] args) {
		
       reverse("Binod");
		replacePi("pippppiiiipi");
	}
    static void reverse(String s) {
	 if(s.length()==0) {
		 return;
	 }
	 
	 String ros= s.substring(1);
	 reverse(ros); 
	 System.out.print(s.charAt(0));
 }
    static void replacePi(String s) {
    	if(s.length()==0) {
    		return;
    	}
    	if(s.charAt(0)=='p' && s.charAt(1)=='i') {
    		System.out.print("3.14");
    		replacePi(s.substring(2));
    	}else {
    		System.out.print(s.charAt(0));
    		replacePi(s.substring(1));
    	}
    	
    }
}
