package Algorithms;

import java.util.Scanner;

public class KadanesAlgo {

	public static void main(String[] args) {
		// Given an array finding sum of maximum sub array.
		// example {1, -3, 2, 2, -1}, result is 4
		Scanner sc = new Scanner(System.in);

		System.out.println("enter the number of elements in array");

		int n = sc.nextInt();

		int[] input = new int[n];
		int index = 0;

		while (n > 0) {
			input[index++] = sc.nextInt();
			n--;
		}

		int current_max = input[0];
		int global_max = input[0];

		for (int i = 1; i < input.length; i++) {
			current_max = Math.max(input[i], current_max + input[i]);
			global_max = Math.max(global_max, current_max);
		}

		System.out.println(global_max);

	}

}
