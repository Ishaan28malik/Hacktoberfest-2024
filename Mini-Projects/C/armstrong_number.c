// Armstrong Number in C


/* Example of an Armstrong Number of order 3,


 153 = 1*1*1 + 5*5*5 + 3*3*3 */

// Program

#include <stdio.h>
int main() {
    int num, temp, rem, result = 0;
    printf("Enter a three-digit number: ");
    scanf("%d", &num);
    temp = num;

    while (temp != 0) {
       // remainder contains the last digit
        rem = temp % 10;
        
       result += rem * rem * rem;
        
       // removing last digit from the temporary number
       temp /= 10;
    }

    if (result == num)
        printf("%d is an Armstrong number.", num);
    else
        printf("%d is not an Armstrong number.", num);

    return 0;
}