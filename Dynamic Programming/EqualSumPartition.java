package dp;

public class EqualSumPartition {

	static boolean isEqualSumPart(int[] a){
		int sum=0;
		for (int i = 0; i < a.length; i++) {
			sum+=a[i];
		}
		if(sum%2!=0) return false;
		else return SubsetSum.isSubsetSum(a, sum/2, 0);
	}
	
	public static void main(String[] args) {
		int[] a={1,5,11,5};
		System.out.println(isEqualSumPart(a));
	}
}
