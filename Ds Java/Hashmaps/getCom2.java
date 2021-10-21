package Ds.Hashmaps;

import java.util.HashMap;
import java.util.Scanner;

public class getCom2 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
        int n1  = sc.nextInt();
        int [] a1 = new int[n1];
        for(int i = 0; i<a1.length;i++) {
        	a1[i] = sc.nextInt();
        }
        int n2  = sc.nextInt();
        int [] a2 = new int[n2];
        for(int i = 0; i<a2.length;i++) {
        	a2[i] = sc.nextInt();
        }
        HashMap <Integer , Integer> fmap = new HashMap<>();
        for(int val: a1) {
        	if(fmap.containsKey(val)) {
        		int of = fmap.get(val);
        		int nf = of+1;
        		fmap.put(val,nf);
        	}else {
        		fmap.put(val, 1);
        	}
        }
        for(int val: a2) {
        	if(fmap.containsKey(val) && fmap.get(val) > 0) {
        	System.out.println(val);
        	int of = fmap.get(val);
    		int nf = of-1;
    		fmap.put(val,nf);
        	}
        }
		
	}

}
