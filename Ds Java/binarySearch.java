package Ds;

public class binarySearch {

	static int binarySearch(int a[] , int key) {
		int low =0, high = a.length-1;
		while(low <= high) {
			int mid = (low+high)/2;
			if(a[mid] == key) {
				return mid;
			}
			else if(key > a[mid]) {
				low = mid+1;
			}
			else {
				high = mid-1;
			}
		}
		return -1;
	}
	static int binaryS(int a[] , int key , int low , int high) {
		if(low > high) return -1;
		int mid = (low+high)/2;
		if(a[mid]==key) {
			return mid;
		}
		if(key> a[mid]) return binaryS(a , key , mid+1 , high);
		return binaryS(a , key , low, high-1);
	}
	public static void main(String[] args) {
		int b [] = {-4 , -1 , 3 , 7 , 10 ,11};
		System.out.println(binaryS(b , 3 , 0 ,5));
	}

}
