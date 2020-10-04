package strings_and_2DArrays;

import java.util.Scanner;

public class RemoveCharacter {

	public static String removeAllOccurrencesOfChar(String input, char c)
	{
		String s = "";
		int i = 0;
		
		while(i < input.length())
		{
			if(input.charAt(i) == c)
			{
				i++;
				continue;
			}
			else if(input.charAt(i) != c)
			{
				s = s + input.charAt(i);
				i++;
			}
		}
		
		return s;
	}
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		String input = s.nextLine();
		char c = s.next().charAt(0);
		System.out.println(RemoveCharacter.removeAllOccurrencesOfChar(input, c));
		s.close();
	}

}
