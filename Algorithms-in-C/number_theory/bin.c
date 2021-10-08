#include<stdio.h>
int main()
{
	int i=0,num,bin[30];
	printf("ENTER THE NUMBER: ");
	scanf("%d",&num);
	while(num>1)
	{
		bin[i]=num%2;
		num/=2;
		i++;
	}
	bin[i]=num;
	printf("\nBINARY FORM: ");
	for(num=i;num>=0;num--)
		printf("%d",bin[num]);
	return 0;
}
