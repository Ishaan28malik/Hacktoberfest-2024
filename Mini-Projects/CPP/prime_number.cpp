#include <iostream>
using namespace std;

int main() {
    int divisor, number_entered;
    bool isPrime = true;

    cout << "Enter a positive integer: ";
    cin >> number_entered;

    // 0 and 1 are not prime numbers
    if (number_entered == 0 || number_entered == 1) {
        isPrime = false;
    }
    else {
        for (divisor = 2; divisor <= number_entered / 2; ++divisor) {
            if (number_entered % i == 0) {
                isPrime = false;
                break;
            }
        }
    }
    if (isPrime)
        cout << number_entered << " is a prime number";
    else
        cout << number_entered << " is not a prime number";

    return 0;
}