package Ds.Recursion;

import java.util.HashSet;
import java.util.Set;

public class advanceRecursion2 {

static 	Set<String> set = new HashSet<>();
	public static void main(String[] args) {
		
d("abcd",0,3);
	}
	static void d(String s,int l,int r) {
		if(l==r) {
			if(set.contains(s)) return;
			set.add(s);
			System.out.println(s);
			return;
		}
		for(int i=l; i<=r;i++) {
			s=interChangeChar( s , l ,i);
			d(s,l+1,r);
			s=interChangeChar(s,l,i);
		}
	}
static String interChangeChar(String s,int a,int b) {
	char array[]=s.toCharArray();
	char temp=array[a];
	array[a]=array[b];
	array[b]=temp;
	return String.valueOf(array);
}
}
