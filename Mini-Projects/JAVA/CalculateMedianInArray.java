// Java implementation of Calculate Median in Array

import java.util.Scanner;
class Median 
{
   public static void main(String args[]) 
    { 
	
	Scanner sc=new Scanner(System.in);
	System.out.println("enter a number"); 
	int a=sc.nextInt();
	double[] input=new double[a];
	System.out.println("enter "+a+" elements");
	for(int i=0;i<a;i++) 
	{
		input[i]=sc.nextDouble();
		
	}
	double res=medianCal(a,input);
	 System.out.println("Median :"+res);  
   
    }
static double medianCal(int  n,double in[])
{
	double m=0;	
	
	if(n%2==1)
	{
		m=in[((n+1)/2)-1];
		
	}
	else
	{
		m=(in[n/2-1]+in[n/2])/2;
		
	}
return m;
	
 }
}
