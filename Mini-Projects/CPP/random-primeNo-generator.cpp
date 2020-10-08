#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <bits/stdc++.h>
using namespace std;

long long int primegenerator(long long int low,long long int high);
long long int prime(  long long int pr,  long long int &j);
long long int cd(  long long int x,  long long int t);

int main()
{
    cout<<"\nEnter the lower and upper bounds for the generator:"<<endl;
    long long int a,b;
    cin>>a>>b;
    cout<<primegenerator(a,b);
}
long long int primegenerator(long long int low,long long int high)
{
    long long int primearr[1000],i,j=0,flag=0,sizert,secret;
    srand(time(0));
    while (low < high)
    {
        flag = 0;
        for(i = 2; i <= low/2; ++i)
        {
            if(low % i == 0)
            {
                flag = 1;
                break;
            }
        }
        if (flag == 0)
        {
            primearr[j]=low;
            ++j;
        }
        ++low;
    }

    secret = rand() % (j);

    return(primearr[secret]);
}
long long int prime(  long long int pr,  long long int &j)
{
    long long int i;
    j = sqrt(pr);
    for (i = 2; i <= j; i++)
    {
        if (pr % i == 0)
            return 0;
    }
    return 1;
}
long long int cd(  long long int x,  long long int t)
{
      long long int k = 1;
    while (1)
    {
        k = k + t;
        if (k % x == 0)
            return (k / x);
    }
}
