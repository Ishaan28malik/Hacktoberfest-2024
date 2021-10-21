package Ds.Recursion;

public class first_practice {

	static int stepCount = 0;
	public static void main(String[] args) {
		
//    System.out.println(sum(5));
//    System.out.println(fastpow(3,10));
//    System.out.println("steps: "+stepCount);
		System.out.println(path(1,200));
	}
	
	static int sum(int n) {
		if(n==1) {
			return 1;
		}
		return n+sum(n-1);
	}
	static int fastpow(int a,int b) {
		stepCount++;
		if(b==0) {
			return 1;
		}
		if(b%2==0) {
			return fastpow(a*a,b/2 );
		}
		return fastpow(a , b-1)*a;
	}
	static int path(int n , int m) {
		if(n==1 || m==1) return 1;
		
		return path(n, m-1 )+path(n-1, m);
	}

}
