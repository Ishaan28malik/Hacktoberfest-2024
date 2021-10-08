package com.company;


import java.util.ArrayList;
import java.util.LinkedList;

public class HashingUsingChaining {
    static class myHash{
    ArrayList<LinkedList<Integer>> table;
    int BUCKET;

    myHash(int b){
        BUCKET = b;
        table = new ArrayList<LinkedList<Integer>>();
        for (int i=0; i<b;i++){
            table.add(new LinkedList<Integer>());
        }
    }

    void insert(int k){
        int i = k % BUCKET;
        table.get(i).add(k);
    }

    boolean search(int k){
        int i = k % BUCKET;
        return table.get(i).contains(k);
    }

    void delete(int k){
        int i = k % BUCKET;
        table.get(i).remove((Integer) k);
    }

    void print(){
        for(LinkedList<Integer> x : table){
            System.out.print(x+ " ");

        }
    }
    }

    public static void main(String[] args) {
        myHash mh = new myHash(7);
        mh.insert(10);
        mh.insert(20);
        mh.insert(15);
        mh.insert(7);
        mh.print();
        System.out.println(" ");

        System.out.println(mh.search(10));
         mh.delete(15);

        mh.print();
        System.out.println(" ");

        System.out.println(mh.search(15));


    }

    }

