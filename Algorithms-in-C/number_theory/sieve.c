#include<stdio.h>
int main()
{
	int n,i,j,c=0;
	scanf("%d",&n);  //Finding number of prime numbers upto 'n'.
	int a[n+1];
	for(i=0;i<n+1;i++)
		a[i]=0;      
	for(i=2;i<=n/2;i++)
	{
		if(a[i]==0)
		{
			for(j=2*i;j<=n;j=j+i)
				a[j]=1;
		}
	}
	for(i=2;i<n+1;i++)
	{
		if(a[i]==0)     //If a[i]==0 then 'i' is prime.
			c++;         
	}
	printf("%d\n",c);
	return 0;
}





