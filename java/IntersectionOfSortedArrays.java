package com.company;

public class IntersectionOfSortedArrays {
    public static void main(String[] args) {
        int[] a = {1,1,3,4,5,6,6,7,8,9};
        int[] b = {1,2,2,4,6,8};
        IntersectionFind(a,b);
    }

    public static void IntersectionFind(int[] a, int[] b) {
        for (int i = 0;i<a.length;i++){
            if (i>0 && a[i]==a[i-1]){
                continue;
            }

            for (int j = 0; j<b.length;j++){
                if (a[i]==b[j]){
                    System.out.print(a[i]+" ");
                    break;
                }
            }
        }
    }
}
