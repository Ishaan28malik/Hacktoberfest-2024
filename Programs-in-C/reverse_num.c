#include <stdio.h>

int getReversedNumber(int num) {
    int orignalNum, reverseNum = 0, remainder;
    orignalNum = num;
    while(num > 0) {
        remainder = num % 10;
        num = num / 10;
        reverseNum = reverseNum * 10 + remainder;
    }
    
    return reverseNum;
}

int main() {
    int num;
    printf("Enter the number you want to reverse");
    scanf("%d", &num);
    int reverseNum = getReversedNumber(num);
    printf("reversednum is: %d", reverseNum);
    return 0;
}