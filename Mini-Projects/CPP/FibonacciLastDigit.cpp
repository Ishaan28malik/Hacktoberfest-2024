// Here the last digit of a large fibonacci number is required.
// There's an observation that the number in the fibonacci series repeat their last digit after 60 numbers.

#include<iostream>
#include<vector>

using namespace std;

long long fibonacciNoLastDigit(long long N) {
    long long i;
    if(N == 0) {
        return 0;
    }
    if(N <= 60) {
        long long arr[N];
        arr[0] = 0;
        arr[1] = 1;
        for (i = 2; i <= N; i++) {
            arr[i] = arr[i - 1] + arr[i - 2];
        }
        return arr[N] % 10;
    }
    else {
        long long arr[60];
        arr[0] = 0;
        arr[1] = 1;
        for (i = 2; i <= 60; i++) {
            arr[i] = arr[i - 1] + arr[i - 2];
        }
        long long dif = N % 60;
        return arr[dif] % 10; 
    }    
}

int main() {
    long long N;
    cin >> N;
    cout<<fibonacciNoLastDigit(N)<<endl;
    return 0;
}
