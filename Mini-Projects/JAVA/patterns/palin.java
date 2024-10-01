import java.util.*;

/*
input : 
10 

output: 
                  1 
                2 1 2 
              3 2 1 2 3 
            4 3 2 1 2 3 4 
          5 4 3 2 1 2 3 4 5 
        6 5 4 3 2 1 2 3 4 5 6 
      7 6 5 4 3 2 1 2 3 4 5 6 7 
    8 7 6 5 4 3 2 1 2 3 4 5 6 7 8 
  9 8 7 6 5 4 3 2 1 2 3 4 5 6 7 8 9 
10 9 8 7 6 5 4 3 2 1 2 3 4 5 6 7 8 9 10 
*/

public class palin{
  public static void main(String args[]){
    int n;
    Scanner se = new Scanner(System.in);
    n = se.nextInt();

    for(int i=1; i<=n; i++){
      //spaces
      for(int j=1; j<=n-i; j++)
        System.out.print("  ");

      for(int j=i ; j>=1; j--)
        System.out.print(j+" ");

      for(int j=2; j<= i ; j++)
        System.out.print(j+" ");

      System.out.println();
    }
  }
}
