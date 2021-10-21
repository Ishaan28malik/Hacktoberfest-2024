package Ds.Hashmaps;

import java.util.*;

public class soln{
	public static List<List<String>> groupAna(String[] strs){
//		Map<String , List<String>> map = new HashMap<>();
//		for(String s: strs) {
//			char charA [] = s.toCharArray();
//			Arrays.sort(charA);
//			String sort = new String(charA);
//			
//			if(!map.containsKey(sort)){
//				map.put(sort, new LinkedList<String>());
//			}
//			map.get(sort).add(s);
//		}
//		return new LinkedList<> (map.values());
		
		HashMap<HashMap<Character , Integer> , ArrayList<String>> big = new HashMap();
		for(String str: strs) {
			HashMap<Character , Integer> fmap = new HashMap();
			for(int i = 0 ; i<str.length(); i++) {
			char ch = str.charAt(i);
			fmap.put(ch, fmap.getOrDefault(ch, 0)+1);
		}
			if(big.containsKey(fmap) == false) {
				ArrayList<String> list  = new ArrayList<>();
				list.add(str);
				big.put(fmap, list);
	   }
	  }
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		String[] arr = new String[N];
		for(int i = 0 ; i<N ; i++) {
			arr[i] = sc.next();
		}
		List<List<String>> ana = groupAna(arr);
		for(List<String> st : ana) {
			Collections.sort(st);
		}
		ana.sort(new ListComparator());
		display(ana);
	}
}
