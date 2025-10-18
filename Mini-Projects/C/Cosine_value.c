#include <stdio.h>
#include <math.h>
#include <stdlib.h>
 
void main()
{
    int n, x1;
    float x, cosx, cosval;
 
    printf("Enter the value of x (in degrees) \n");
    scanf("%f", &x);
    x1 = x;
    x = x * (3.142 / 180.0);
    cosval = cos(x);
    printf("cos(%d) = %f\n", x1, cosval);
}
