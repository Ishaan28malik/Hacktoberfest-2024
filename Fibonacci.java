import java.util.Scanner;

public class Fibonacci {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.print("Type a number to Fibonacci sequence: ");
		int n = input.nextInt(); // 0 < n < 46
		
		int[] fibo = new int[n];
		fibo[0] = 0; // fixed value
		if (n > 1) {
			fibo[1] = 1;  // fixed value			
		}
		
		for(int i = 2; i < fibo.length; i++)
			fibo[i] = fibo[i - 1] + fibo[i - 2];
		
		String output = "";
		for(int i = 0; i < fibo.length; i++) {
			output += fibo[i] + " ";
		}
		
		System.out.println(output);
		input.close();
	}
}
