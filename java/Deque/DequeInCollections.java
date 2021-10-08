package com.company;

import java.util.Deque;
import java.util.Iterator;
import java.util.LinkedList;

public class DequeInCollections {
    public static void main(String[] args) {
        Deque<Integer> d =new LinkedList<Integer>();
        d.addFirst(5);
        d.addLast(10);

        int size = d.size();
        int firstElement = d.poll();
        d.offer(9);

        d.add(8);
        d.add(18);
        d.add(28);
        d.add(83);

        System.out.print(d);
        System.out.println(" ");

        Iterator it = d.iterator();
        while (it.hasNext()){
            System.out.print(it.next()+" ");
        }
        System.out.println(" ");
        for (int x: d){
            System.out.print(x+ " ");
        }
    }
}
