import java.util.*;
import java.io.*;
class bitMagicPowerOfTwo{
  public static void main(String args[])
  {
    // The program checks if a number is a power of 2 Ex- 1,2,4,8,etc
    Scanner s1=new Scanner(System.in);
    int n=s1.nextInt();
    if((n&(n-1))==0)
    {
      System.out.println("Power of Two");
    }
    else
    {
      System.out.println("Not a power of two");
    }
  }
}
