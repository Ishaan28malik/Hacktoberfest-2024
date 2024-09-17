package strings_and_2DArrays;

import java.util.Scanner;

public class PrintAllSubstrings {

	public static void printSubstrings(String str)
	{
		int i = 0;
		while(i < str.length())
		{
			int j = i;
			while(j < str.length())
			{
				System.out.println(str.substring(i , j + 1));
				j++;
			}
			i++;
		}
	}
	
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		String str = s.nextLine();
		PrintAllSubstrings.printSubstrings(str);
		
		s.close();
	}

}
