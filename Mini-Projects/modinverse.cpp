// C++ program to find multiplicative modulo inverse using
// Extended Euclid algorithm.
#include<iostream>
#define ll long long int
using namespace std;

// C function for extended Euclidean Algorithm
int gcdExtended(ll a, ll b, int *x, int *y);

// Function to find modulo inverse of a
void modInverse(ll a, ll m)
{
	int x, y;
	int g = gcdExtended(a, m, &x, &y);
	if (g != 1)
		return ;
	else
	{
		// m is added to handle negative x
		int res = (x%m + m) % m;
		cout  << res;
	}
}

// C function for extended Euclidean Algorithm
int gcdExtended(ll a, ll b, int *x, int *y)
{
	// Base Case
	if (a == 0)
	{
		*x = 0, *y = 1;
		return b;
	}

	int x1, y1; // To store results of recursive call
	int gcd = gcdExtended(b%a, a, &x1, &y1);

	// Update x and y using results of recursive
	// call
	*x = y1 - (b/a) * x1;
	*y = x1;

	return gcd;
}

// Driver Program
int main()
{
	ll n,m=1000000007;
	cin>>n;

	modInverse(n, m);
	return 0;
}
