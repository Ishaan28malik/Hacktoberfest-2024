#include <stdio.h>
int sum=0,rem;
int reverse_function(int num){
   if(num){
      rem=num%10;
      sum=sum*10+rem;
      reverse_function(num/10);
   }
   else
      return sum;
   return sum;
}
int main() {
    int num, reverse = 0, remainder;
    printf("Enter an integer: ");
    scanf("%d", &num);
    reverse=reverse_function(num);
    printf("Reversed number : %d", reverse);
    return 0;
}
