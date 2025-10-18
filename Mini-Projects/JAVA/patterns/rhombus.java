import java.util.*;
/*
input : 
8 

output : 
       ********
      ********
     ********
    ********
   ********
  ********
 ********
********
*/

public class rhombus{
  public static void main(String[] args){
     int n;
     Scanner se = new Scanner(System.in);
     n = se.nextInt();

     for(int i=1; i<=n; i++){
       for(int j=1; j<=n-i;j++)
        System.out.print(" ");

       for(int j=1; j<=n; j++)
        System.out.print("*");

       System.out.println();
     }
  }
}
