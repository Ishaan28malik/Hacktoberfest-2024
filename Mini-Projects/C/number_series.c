#include<stdio.h>
int main()
{
	int j,i,n,f;
	double  sum=0.0;
	printf("Enter last element:\n");
	scanf("%d",&n);
	for(i=1;i<=n;i++)//loop for adding elements of series
	{
		if(i!=n)
			printf("1/%d!+",i);
		else
			printf("1/%d!=",i);
		f=1;
		for(j=1;j<=i;j++)//loop for finding factorial
		{
			f=f*j;
		}
		sum=sum+(1.0)/f;
	}
	printf("%lg\n",sum);
	return 0;
}
