public class SortedSearch {
    // Naive Approach
    // Time Complexity - O(n)
    // Space Complexity - O(1)
    public static int sortedNaive(int arr[], int x) {
        int n = arr.length;
        for (int i = 1; i < n; i++) {
            if (arr[i] == x) {
                return i;
            }
        }
        return -1;
    }

    // Iterative Approach
    // Time Complexity - O(logn)
    // Space Complexity - O(n)
    public static int sortedIterative(int arr[], int n, int x) {
        int low = 0, high = n - 1;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (arr[mid] == x) {
                return mid;
            } else if (arr[mid] < x) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return -1;
    }

    // Recursive Approach
    public static int sortedRecursive(int arr[], int low, int high, int x) {
        if (low > high) {
            return -1;
        }
        int mid = (low + high) / 2;
        if (arr[mid] == x) {
            return mid;
        } else if (arr[mid] < x) {
            return sortedRecursive(arr, mid + 1, high, x);
        } else {
            return sortedRecursive(arr, low, mid - 1, x);
        }
    }

    public static void main(String[] args) {
        int arr[] = { 1, 2, 4, 6, 7, 8, 9, 10, 14, 20 };
        int n = arr.length;
        int low = 0, high = n - 1;
        int x = 10;
        System.out.println(sortedRecursive(arr, low, high, x));
    }
}