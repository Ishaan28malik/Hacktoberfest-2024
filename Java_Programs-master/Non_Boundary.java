import java.util.*;
class Non_Boundary
{
    public static void main(String[]args)
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Input the number of rows or columns in the matrix");
        int m=sc.nextInt();
        System.out.println("Input elements in the matrix");
        if(m>=2&&m<=20)
        {
            int a[][]=new int[m][m];

            for(int x=0;x<m;x++)
            {
                for(int y=0;y<m;y++)
                {
                    a[x][y]=sc.nextInt();
                }
            }
            System.out.println("The original matrix is-");
            for(int x=0;x<m;x++)
            {
                for(int y=0;y<m;y++)
                {
                    System.out.print(a[x][y]+"\t");
                }
                System.out.println();
            }
            System.out.println("The non-boundary elements are");
            for(int x=0;x<m;x++)
            {
                for(int y=0;y<m;y++)
                {
                    if(x==0||y==0||y==(m-1)||x==(m-1))
                    {
                        System.out.print("\t");
                        continue;}
                    System.out.print(a[x][y]+"\t");
                }
                System.out.println();
            }
        }
    }
}

