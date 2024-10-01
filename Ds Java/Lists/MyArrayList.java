package Ds.Lists;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class MyArrayList {

	public static void main(String[] args) {
		
		List<String> fruits = new ArrayList();
		List<String> vegetables = new LinkedList();
		
		fruits.add("Apple");
//		fruits.add(23);
		vegetables.add("Alu");
		vegetables.add("Tomotato");
		
		fruits.addAll(vegetables);
		
		System.out.println(fruits);
		pairClass<String , Integer> p1 = new pairClass("aryan",69);
        pairClass <Boolean , String> p2 = new pairClass( true,"hila" );
        
        System.out.println(fruits.get(2));
    
        List<String> toRemove = new ArrayList();
        toRemove.add("Apple");
        
        fruits.removeAll(toRemove);
        
//        fruits.remove(1);
        System.out.println(fruits);
//        
//        p1.getDescription();
//        p2.getDescription();
        
        String temp[]= new String[fruits.size()];
        fruits.toArray(temp);
        
        for(String e : temp) {
        System.out.print(e+" ");
        }
//        System.out.println(fruits.contains("Alu"));
	}

}
