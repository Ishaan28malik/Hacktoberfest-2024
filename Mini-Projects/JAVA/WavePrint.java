package strings_and_2DArrays;

import java.util.Scanner;

public class WavePrint {

static Scanner s = new Scanner(System.in);
	
	
	public static int[][] takeInput2D(){
		
		int numRows = s.nextInt();
		int numCols = s.nextInt();
		int[][] input = new int[numRows][numCols];
		for(int i = 0; i < numRows; i++){
			for(int j = 0; j < numCols; j++){
				input[i][j] = s.nextInt();
			}
		}
		return input;
	}
	
	public static void wavePrint(int input[][])
	{
		int rows = input.length;
		
		if(rows == 0)
			return;
		
		int cols = input[0].length;
		
		for(int j = 0; j < cols; j++)
		{
			if(j % 2 == 0)
			{
				for(int i = 0; i < rows; i++)
				{
					System.out.print(input[i][j] + " ");
			    }
			}
			else
			{
				for(int i = rows-1; i >= 0; i--)
					{
						System.out.print(input[i][j] + " ");
					}
			}
			
		}
	}
	
	public static void main(String[] args) {
	
		int input[][] = takeInput2D();
		WavePrint.wavePrint(input);
		
	}

}
