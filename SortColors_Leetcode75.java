/* Solving without using the inbuilt "sorting" function which is given in many programming languages because here we have to sort 'in-place' and in linear time */
/* The time complexity-O(n) Space complexity-O(1) */

class Solution{
	public static void main(int[] nums) {
		int p1=0,index=0,p2=nums.length-1;
		int temp;
		
		while(index <= p2){
			if (nums[index] == 0){
				temp=nums[index];
				nums[index]=nums[p1];
				nums[p1]=temp;
				p1++;
			}
			if (nums[index]==2){
				temp=nums[index];
				nums[index]=nums[p2];
				nums[p2]=temp;
				p2--;
				index--;
			}
			index++;
		}
	}
}			
