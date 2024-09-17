package strings_and_2DArrays;

import java.util.Scanner;

public class Remove_ConsecutiveDuplicates {
		
		public static String removeConsecutiveDuplicates(String input)
		{
			String x = "";
			int j = 0;
			
			x = x + input.charAt(0);
			
			for(int i = 0; i < input.length() - 1; i++)
			{
				j = i+1;
				if(input.charAt(j) != input.charAt(i))
				{
					x = x + input.charAt(j);
				}
			}
			return x;
			
		}
		
		public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		String input = s.next();
		System.out.println(Remove_ConsecutiveDuplicates.removeConsecutiveDuplicates(input));
		s.close();
	}

}
