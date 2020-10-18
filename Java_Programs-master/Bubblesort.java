import java.util.*;
import java.lang.*;
import java.io.*;

/*Math.pow() is import using java.lang package*/
class Main
{ 
  
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
    System.out.print("Enter the number :");
    int n = sc.nextInt();
    int []a = new int[n];
    int i=0,temp=0,j=0;
    System.out.print("Enter the array Element :");
    for(i=0;i<n;i++)
  {
    a[i] = sc.nextInt();
  }
  for(i=0;i<n;i++)
  {
    for(j=0;j<n-i-1;j++)
    {
      if(a[j]>a[j+1])
      {
        temp=a[j];
        a[j]=a[j+1];
        a[j+1]=temp;
      }
    }
  }
		for(i=0;i<n;i++)
    {System.out.print(a[i]+" ");}
	
}}
© 2020 GitHub, 
