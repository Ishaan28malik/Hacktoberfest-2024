package Solution;

public class ToggleCases {

	
	// given a string with some small and some capital letters, toggle them such that small are capital and capital
	// are small now
	// we can do one thing for sure here, 'char' - 'a' = 'CHAR' - 'A'
	// so we use this algebr only to convert cases
	
	public static String toggle(String str) {
		StringBuilder sb = new StringBuilder(str);
		for(int i = 0;i<sb.length();i++) {
			char ch = sb.charAt(i);
			if(ch>='a' && ch<='z')
				ch = (char)(ch-'a'+'A');
			else 
				ch = (char)(ch-'A'+'a');
			sb.setCharAt(i, ch);
		}
		return sb.toString();
		
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		String str = "aBCdFgH";
		String ans = toggle(str);
		System.out.println(ans);
	}

}
