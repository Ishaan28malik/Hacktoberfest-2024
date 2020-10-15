/*  Dynamic Programming Technique used to reduce the total time complexity of the fibonacci function.
        Time taken = (number of calls) * (t) 
        Number of Calls <= 2*n + 1
        => Time Taken= (2*n + 1) * O(1) = O(2*n+1)
        => O(N) <<< O(2^N) which is the time taken using the recursion approach.
*/

#include<iostream>
using namespace std;

int arr[100];

int fibonacciUsingDP(int n){
    if(arr[n]!=-1){
        return arr[n];
    }
    if(n==1 ||n==2){
        return arr[n];
    }
    else{
        return arr[n] = fibonacciUsingDP(n-1) + fibonacciUsingDP(n-2);
    }
}

int main(){
    int N;
    cin>>N;
    for(int i=2;i<50;i++){
        arr[i]=-1;
    }
    arr[1]=1;
    arr[2]=1;
    cout<<"Result of Fibonnaci Series at this position : "<<fibonacciUsingDP(N)<<endl;
}
