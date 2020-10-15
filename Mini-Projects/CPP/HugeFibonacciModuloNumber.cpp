/* When we need to perform Huge Fibonacci Number % Another Number,
we will use the concept of Pisano Period. */

#include<iostream>

using namespace std;

long long get_pisano_period(long long M) {
    long long a = 0, b = 1, c, p_period;
    c = a + b; //1

    for(long long i = 0; i < M * M; i++) { //4
        c = (a + b) % M;
        a = b;
        b = c;

        if(a == 0 && b == 1) {
            p_period = i + 1;
            return p_period;
        }
    }
    return 0;
}

long long get_fibonacci_huge(long long N, long long M) {
    
    long long a,b,p_period;
    
    p_period = get_pisano_period(M);
    long long index  = N % p_period;

    long long result = index;
    a = 0;
    b = 1;
    for(long long i = 2; i <= index; i++) {
        result = (a + b) % M;
        a = b;
        b = result;
    }
    return result % M;
}

int main() {
    long long n, m;
    cin >> n >> m;
    cout << get_fibonacci_huge(n, m) << endl;
}
