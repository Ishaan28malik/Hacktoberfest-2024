import java.util.Scanner;

public class break_in_string {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.next();
		int ans=-1;
		char c = sc.next().charAt(0);
		for (int i=0;i<s.length();i++){
			if (s.charAt(i)==c){
				ans= i;
				break;
			}
		}
		System.out.print(ans);
	}
}