import java.util.Arrays;

public class QuickSort {
    public static void main(String[] args) {
        int[] nums = { 7,2,5,24,345,42,32,1,3,432,6,89};
        sort(nums,0,nums.length-1);
        System.out.println(Arrays.toString(nums));
    }
    public static void sort(int[] nums, int low, int hi){
        if( low >= hi ){
            return;
        }
        int start = low;
        int end = hi;
        int mid = start + (end - start )/2;
        int pivot = nums[mid];
        while(start <= end){
            while(pivot > nums[start]){
                start++;
            }
            while(pivot < nums[end]){
                end--;
            }
            if(start <= end){
                int temp = nums[end];
                nums[end] = nums[start];
                nums[start] = temp;
                start++;
                end--;
            }
        }
        sort(nums,low,end);
        sort(nums, start, hi);
    }
}
