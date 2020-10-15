/*
2 x 1 and 2 x 2 tiles are to be fit inside a 2 x N box. The no of ways
to do so is calculated using Recursion.
*/

#include<iostream>
using namespace std;

int tilingFunction(int x){
    if(x==1 ||x==0){
        return 1;
    }
    return (tilingFunction(x-1)+2*tilingFunction(x-2));
}
int main(){
    int N;
    cin>>N;
    cout<<tilingFunction(N)<<endl;
}
