package com.company.Day;

public class BinarySearchD3 {
        public static int binarySearch(int arr[], int l, int r, int x)
        {
            if (r >= l) {
                int mid = l + (r - l) / 2;

//                System.out.println("l= "+ l+ " r = "+ r +" mid = "+ mid);


                if (arr[mid] == x)
                    return mid;

                if (arr[mid] > x) {
                    return binarySearch(arr, l, mid - 1, x);
                }
                return binarySearch(arr, mid + 1, r, x);
            }
            return -1;
        }


        public static void main(String[] args)
        {
            int[] arr = { 2, 3, 4, 10, 14,25,65,98,135,227,322 };
            int n = arr.length;
            int x = 227;
            int result = binarySearch(arr, 0, n - 1, x);
            if (result == -1)
                System.out.println("Element absent");
            else
                System.out.println("Element found at index " + result);
        }
    }


