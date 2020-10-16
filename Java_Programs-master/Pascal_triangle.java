package pascal_triangle;
import java.util.*;

public class Pascal_triangle {
		static int binomialcoff(int a,int b) {
			int res =1;
			if (b>a-b)
				b=a-b;
			for(int i=0;i<b;i++) {
				res *=(a-i);
				res /=(i+1);
			}
			return res;
		}
	public static void main(String[] args) {
		Scanner sc =new Scanner(System.in);
		int n= sc.nextInt();
		for(int line=0;line<n;line++) {
			for(int i=0;i<=line;i++) 
				System.out.print(binomialcoff(line,i)+" ");
				System.out.println();
		}
	}

}
