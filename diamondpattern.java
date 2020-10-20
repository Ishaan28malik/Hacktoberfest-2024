import java.util.*;
      
      public class Main{
      
      public static void main(String[] args) {
          Scanner scn = new Scanner(System.in);
          int n = scn.nextInt();
          int nsp = n/2;          // number of spaces
          int nno = 1;            //number of numbers
          int ov = 1;             //outer variable
          for(int i=1; i<=n; i++){
              for(int j=1; j<=nsp; j++){
                  System.out.print("	");
              }
              int iv = ov;        //inner variable
              for(int j=1; j<=nno; j++){
                    System.out.print(iv + "	");
                    if(j<=(nno/2))
                        iv++;
                    else
                        iv--;
              }
              System.out.println();
              if(i<=n/2){
                  nsp--;
                  nno+=2;
                  ov++;
              } else {
                  nsp++;
                  nno-=2;
                  ov--;
              }
          }
      
       }
      }
