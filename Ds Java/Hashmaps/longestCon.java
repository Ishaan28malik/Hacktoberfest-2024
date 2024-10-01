package Ds.Hashmaps;

import java.util.HashMap;
import java.util.Scanner;

public class longestCon {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
        int n  = sc.nextInt();
        int [] a = new int[n];
        for(int i = 0; i<a.length;i++) {
        	a[i] = sc.nextInt();
        }
     
        HashMap <Integer , 	Boolean> map = new HashMap<>();
        for(int val: a) {
        	map.put(val, true);
        }
        for(int val:a) {
        	if(map.containsKey(val-1)) {
        		map.put(val, false);
        	}
        }
        int msp=0;
        int ml=0;
        for(int val:a) {
        	if(map.get(val)==true) {
        		int tl=1;
        		int tsp = val;
        		while(map.containsKey(tsp+ tl)) {
        			tl++;
        		}
        		if(tl>ml) {
        			msp=tsp;
        			ml=tl;
        		}

        	}
        }
        for(int i=0; i<ml ; i++) {
        	System.out.println(msp+i);
        }
	}

}
