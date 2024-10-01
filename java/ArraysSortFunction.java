package com.company;

import java.util.Arrays;

class point{
    public int a;
    public int b;
    public point(int a, int b){
        this.a=a;
        this.b=b;
    }

}
public class ArraysSortFunction {
    public static void main(String[] args) {
        int[] arr = { 8,7,6,4,2,1,98,34,32,6};
        int[] arr1 = { 'd','f','t','e','v','h','j','s','e',};

        Arrays.sort(arr);
        Arrays.sort(arr1);

        for(Integer x : arr){
            System.out.print(x+ " ");
        }
        System.out.println("\n--------------------------------------------\n");
        for (int i : arr1) {
            System.out.print(i + " ");
        }

        System.out.println("\n--------------------------------------------\n");

        int src = Arrays.binarySearch(arr,6);
        System.out.println(src);

        System.out.println("\n--------------------------------------------\n");

        point[] a = { new point(2,5), new point(4,7),new point(8,2),new point(4,6)};
        for (point p : a){
            System.out.print("("+p.a+", "+ p.b+")"+ " ");
        }
        System.out.println(" ");
//        Arrays.sort(a);
//        for (point p : a){
//            System.out.print("("+p.a+", "+ p.b+")"+ " ");
//        }



    }

}
