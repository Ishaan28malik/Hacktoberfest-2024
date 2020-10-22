#include<stdio.h>
#include<conio.h>
int main()
{
	int num, sum = 0, temp, count;  //Data type deceleration.
	printf("Enter any number to check ether it is Palindrome number or not");
	scanf("%d",&num); //User input 
	temp = num;  
	while(temp > 0)  // Loop for finding Palindrome number
	{
		count = temp %10;
		sum = (sum * 10) + count;
		temp = temp / 10;
	}
	if(sum == num)  //Checking whether number is palindrome or not
	{
		printf("%d is a Palindrome number",num);
	}
	else
	{
		printf("%d is not a Palindrome number",num);
	}
	getch();
	return 0;
}
