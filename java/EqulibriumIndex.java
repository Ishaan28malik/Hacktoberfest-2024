package com.company.Day;

public class EqulibriumIndex {

/*
    strait forward method
    public static int equi(int[] arr, int n) {
        int i,j,leftSum,rightSum;

        for (i = 0; i < n; ++i) {
            leftSum=0;
            rightSum=0;
            for ( j = 0; j < i; j++) {
                leftSum+=arr[j];
            }
            for ( j = i+1; j < n; j++) {
                rightSum+=arr[j];
            }

            if (leftSum==rightSum){
                return i;
            }

        }
        return -1;
    }
*/

//    tricky solution(Time complexity: O(n))
    public static int equi(int[] arr, int n){
        int sum=0, leftSum=0;
        for (int i = 0; i < n; i++) {
            sum+=arr[i];
        }

        for (int i = 0; i < n; ++i) {
            sum -=arr[i];
            if (leftSum==sum){
                return i;
            }
            leftSum+=arr[i];
        }
        return -1;
    }


    public static void main(String[] args) {
        int[] arr =  {-7, 1, 5, 2, -4, 3, 0 };
        int arrSize = arr.length;
        System.out.println(EqulibriumIndex.equi(arr,arrSize));
    }



}
