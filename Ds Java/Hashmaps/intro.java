package Ds.Hashmaps;
import java.util.*;
public class intro {

	public static void main(String[] args) {
		HashMap <String , Integer> hm = new HashMap<String, Integer>();
		hm.put("India", 135);
		hm.put("Pakistan", 40);
		hm.put("China", 200);
		hm.put("USA", 20);
		hm.put("UK", 35);
		
		System.out.println(hm);
		System.out.println(hm.get("India"));
		System.out.println(hm.containsKey("USA"));
		
		Set <String> keys = hm.keySet();
		System.out.println(keys);
		
		for(String key: hm.keySet()) {
		    Integer val = hm.get(key);
		    System.out.println(key+" " + val);
		}
	}

}
