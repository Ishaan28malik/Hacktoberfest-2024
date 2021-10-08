// To compile this, use gcc bhaskara.c -lm

#include <stdio.h>
#include <math.h>

int main()
{
	double a, b, c;
	printf("Enter a number that represents A:\n");
	scanf("%lf", &a);
	printf("Enter a number that represents B:\n");
	scanf("%lf", &b);
	printf("Enter a number that represents C:\n");
	scanf("%lf", &c);

	if(a == 0)
	{
		printf("It's impossible to calculate bhaskara!\n");
		printf("Division by zero!\n");
	}
	else
	{
		double delta;
		delta = pow(b, 2) - 4 * a * c;

		if(delta < 0)
		{
			printf("It's impossible to calculate bhaskara!\n");
			printf("There is no Real solution!\n");
		}
		else
		{
			double x1, x2;
			x1 = (-b + sqrt(delta))/(2 * a);
			x2 = (-b - sqrt(delta))/(2 * a);

			printf("X1 = %lf\n", x1);
			printf("X2 = %lf\n", x2);
		}
	}

	return 0;
}
