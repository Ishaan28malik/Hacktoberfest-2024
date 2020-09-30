#include<stdio.h>
char *ntw(int n)//convert number to words
{
    char *str;
    if(n==1)
    str = "one";
    if(n==2)
    str ="two";
    if(n==3)
    str="three";
    if(n==4)
    str="four";
    if(n==5)
    str="five";
    if(n==6)
    str="six";
    if(n==7)
    str="seven";
    if(n==8)
    str="eight";
    if(n==9)
    str="nine";
    if(n==10)
    str="ten";
    if(n==11)
    str="eleven";
    if(n==12)
    str="twelve";
    if(n==13)
    str="thirteen";
    if(n==14)
    str="fourteen";
    if(n==16)
    str="sixteen";
    if(n==18)
    str="eighteen";
    if(n==17)
    str="seventeen";
    if(n==19)
    str="nineteen";
    if(n==20)
    str="twenty";
    return str;
}
int main()
{
    int a,b,i,j;
    scanf("%d %d",&a,&b);
    if(b>30)
    {
       if(b==45)
       printf("quarter to %s",ntw(a+1));
       else if(b<40)
       printf("twenty %s minutes to %s",ntw(40-b),ntw(a+1));
       else
       printf("%s minutes to %s",ntw(60-b),ntw(a+1));
    }
    else
    {
       if(b==15)
       printf("quarter past %s",ntw(a));
       else if(b==30)
       printf("half past %s",ntw(a));
       else if(b==0)
       printf("%s o' clock",ntw(a));
       else if(b>20)
       printf("twenty %s minutes past %s",ntw(b-20),ntw(a));
       else
       printf("%s minute past %s",ntw(b),ntw(a));
    }
    return 0;
}
