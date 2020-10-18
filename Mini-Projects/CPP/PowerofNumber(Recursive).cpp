/*
A very simple problem using recursion to find Power of a given number.Its time complexity is quite less too.
*/


#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
#include <map>
#include <set>
#include <forward_list>
using namespace std;

long long int power(long long int x,long long int n){
    if(n==0){
        return 1;
    }
    long long int temp=power(x,n/2);
    if(n%2==0){
        return temp*temp;
    }
    else{
        return x*temp*temp;
    }
}


//calculate power of x raise to power n
int main(){
    int x;
    int n;
    cin>>x>>n;
    cout<<power(x,n);
    
}