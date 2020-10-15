#include<iostream>
using namespace std;

int findMissingNo(int arr[],int N){
    int x1=0,x2=1;
    for(int i=0;i<N-1;i++){
        x1^=arr[i];
    }
    for(int i=2;i<=N;i++){
        x2^=i;
    }
    return x1^x2;
}

int main(){
    int N;
    cin>>N;
    int arr[N];
    cout<<"Enter a consecutive numbers array (starting from 1) of size = "<<N<<" : "<<endl;
    for(int i=0;i<N-1;i++){
        cin>>arr[i];
    }
    cout<<"Missing number is : "<<findMissingNo(arr,N)<<endl;
}
