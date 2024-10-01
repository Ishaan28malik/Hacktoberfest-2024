#include<stdio.h>
int main()
{
	int a,b,ans=1;
	scanf("%d %d",&a,&b);                  // Taking input for calculating 'a^b'.  
	while(b>0)
	{
		if(b&1!=0)               // Checking if 'b' is odd.
			ans=ans*a;         // Multiplying 'ans' by 'a' if 'b' is odd.
		a=a*a;                  // Squaring 'a' every time.
		b=b>>2;                    //Dividing 'b' by 2.
	}
	printf("%d\n",ans);               //Printing 'ans'.
	return 0;
}
