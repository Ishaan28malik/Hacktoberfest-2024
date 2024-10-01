import java.util.*;
/*
input : 
7 

output : 
      1 
     2 2 
    3 3 3 
   4 4 4 4 
  5 5 5 5 5 
 6 6 6 6 6 6 
7 7 7 7 7 7 7 
*/

public class pyranum{
  public static void main(String [] args){
    int n;
    Scanner se;
    se = new Scanner(System.in);
    n = se.nextInt();

    for(int i=1; i<=n; i++){
      for(int j=1; j<=n-i; j++)
        System.out.print(" ");

      for(int j=1; j<=i;j++)
        System.out.print(i+" ");

      System.out.println();
    }
  }
}
