#include<iostream>
#include<vector>
using namespace std;

void GenerateSieveOfEratosthenes( int n ){
    vector<bool> is_prime(n+1, true);

    // Optimisation technique from Number theory
    // Just have to check till the square root of the number 
    for(int i = 2; i*i <= n; i++){
        if(is_prime[i]){
            for(int j = i*2; j <= n; j +=i ){
                is_prime[j] = false;
            }
        }
    }

    // For printing the Sieve
    for(int i = 2; i <= n; i++){
        if(is_prime[i]){
            cout << i << endl;
        }
    }
}

int main(){

    int n;
    cout << "Enter the number: ";
    cin >> n;

    GenerateSieveOfEratosthenes(n);
    return 0;
}