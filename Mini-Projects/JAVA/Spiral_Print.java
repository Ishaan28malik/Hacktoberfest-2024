package strings_and_2DArrays;

import java.util.Scanner;

public class Spiral_Print {

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
	
	public static void spiralPrint(int matrix[][])
	{
		int rs = 0, re = matrix.length - 1;
		int cs = 0, ce = matrix[0].length - 1;
		
		while(rs <= re && cs <= ce)
		{
			
			for(int i = cs; i <= ce; ++i)
			{
				System.out.print(matrix[rs][i] + " ");
			}
			rs++;
			for(int i = rs; i <= re ; ++i)
			{
				System.out.print(matrix[i][ce] + " ");
			}
			ce--;
            if(re >= rs)
            {
                for(int i = ce; i >=cs; --i)
				{
					System.out.print(matrix[re][i] + " ");
				}
                re--;
            }
            for(int i = re ; i >= rs; --i)
            {
				System.out.print(matrix[i][cs] + " ");
			}
            cs++;
		}
	}
	public static void main(String[] args) {
		int a[][] = takeInput2D();
		Spiral_Print.spiralPrint(a);
	}
}
