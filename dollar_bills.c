//shows how to pay the amount using smallest number of $20 $10 $5 and $1 bills
#include <stdio.h>
int main(){
    int d, tw ,t ,f ,o;              
    printf("Enter dollar amount: ");
    scanf("%d",&d);
    tw = d/20;
    t= (d-(tw*20))/10;
    f= (d-(tw*20)-(t*10))/5;
    o= d-(tw*20)-(t*10)-(f*5);
    printf("$20 bills: %d\n$10 bills: %d\n$5 bills: %d\n$1 bills: %d\n",tw,t,f,o);
    return 0;
}