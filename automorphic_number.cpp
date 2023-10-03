#include<iostream>
using namespace std;

int main()
{
    int n=76,flag=1;
    int square=n*n;
    while(n>0){
        if(n%10!=square%10){
            flag=0;
            break;
        }
        else{
            n=n/10;
            square=square/10;
        }
        
    }
    if(flag==0){
        cout<<"not automorphic number";
    }
    else{
        cout<<"automorphic number";
    }
    
    
    return 0;
}
