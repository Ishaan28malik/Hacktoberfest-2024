package Ds.Heaps;

import java.util.Collections;
import java.util.PriorityQueue;

public class intro {

	public static void main(String[] args) {
		PriorityQueue <Integer> pq = new PriorityQueue(Collections.reverseOrder());
		int [] rank = {22,99,3,11,88,4,1};
		for(int val: rank) {
			pq.add(val);
		}

		while(pq.size()> 0) {
			System.out.println(pq.peek());
			pq.remove();
		}
	}

}
