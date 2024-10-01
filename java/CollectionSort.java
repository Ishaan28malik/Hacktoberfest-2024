package com.company;

import java.util.ArrayList;
import java.util.Collections;

public class CollectionSort {
    public static void main(String[] args) {
        ArrayList<Integer> l = new ArrayList<Integer>();
        l.add(5);
        l.add(55);
        l.add(15);
        l.add(22);
        l.add(18);
        Collections.sort(l);
        System.out.print(l);
        System.out.println("");
        Collections.sort(l,Collections.reverseOrder());
        System.out.print(l);

    }

}
