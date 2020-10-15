#include<iostream>
using namespace std;

int main(){
    int a,b;
    cin>>a>>b;
    a=a^b;
    b=a^b;
    a=a^b;
    cout<<"Swapped Values of a: "<<a<<" and b: "<<b<<endl;
}
