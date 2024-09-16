public class Program
{
    public static void main(String[] args) {

        for (int i=1;i<=5;i++){
        for(int j=1;j<=i-1;j++){
           System.out.print(" ");
           }
           for(int j=1;j<=-2*i+11;j++){
               System.out.print("*") ;
           }
           System.out.println();
        }

    }
}



/* Output:

*********
 *******
  *****
   ***
    *
  You can try more such examples
  */



