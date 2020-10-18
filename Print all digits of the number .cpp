// Print all digits from left to right order of the number. 

#include <iostream>

using namespace std;
void digit(long n)
{
    int r;
    if(n==0)
        return ;
    r=n%10;
    digit(n/10);
    cout<<r<<endl;

}


int main()
{
    long n;
    cin>>n;
    digit(n);
    return 0;
}
