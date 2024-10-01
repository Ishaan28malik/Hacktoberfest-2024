package Ds.Hashmaps;
import java.util.*;

import java.util.Map.Entry;
public class main {

	public static void main(String[] args) {
//		Map<String , Integer> num = new HashMap<>();
//        num.put("one", 1);
//        num.put("two", 2);
//        num.put("three", 3);
//        
//        System.out.println(num);
//		for(Entry<String , Integer> entry: num.entrySet() ) {
//			entry.setValue(entry.getValue() *100);
//		}
//		System.out.println(num);
		System.out.println(gethash("elephant"));
	}
	public static int gethash(String s) {
		int hash = 0;
		for(int i = 0 ; i<s.length(); i++) {
			hash +=s.charAt(i);
			
		}
		return hash;
	}

}
