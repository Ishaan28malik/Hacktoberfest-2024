/*  Stirling Alogrithm
    x^k = sum (i = 1 to k) {k, i} * i! * ncr(x, i)
    sum (x = 0 to n) x^k
            = sum (i = 0 to k) {k, i} * i! * sum (x = 0 to n) nCr(x, i)
            = sum (i = 0 to k) {k, i} * i! * nCr(n + 1, i + 1)
            = sum (i = 0 to k) {k, i} * i! * (n + 1)! / ((i + 1)! * (n - i)!)
            = sum (i = 0 to k) {k, i} * ((n + 1) * n * (n - 1) * ..... * (n - i + 1)) / (i + 1)
    
    {k, i} = Stirling Number of Second Kind = {k - 1, i - 1} + i * {k - 1, i}
    Assuming x <= 1e18 and k <= 1e3
    
    Time Complexity: O(k * k)
*/

#include <stdio.h>
const long long mod = 1000000007;

long long add(long long x, long long y) { x += y; if(x >= mod) x -= mod; return x; }
long long mul(long long x, long long y) { return ((x % mod) * (y % mod)) % mod; }

int main()
{
    long long x, k;
    printf("Enter a number that represent X:\n");
    scanf("%lld", &x);
    printf("Enter a number that represent K:\n");
    scanf("%lld", &k);

    // Assumption 1 <= k <= 1e3
    long long S[1001][1001];
    // Initialize Stirling variable
    for(int i = 0; i <= k; i ++) {
      S[1][i] = 0;
    }
    S[1][1] = 1;

    // Calculate Stirling number of second kind
    for(int i = 2; i <= k; i ++) {
        for(int j = 1; j <= k; j ++) {
            S[i][j] = add(S[i - 1][j - 1], mul(j, S[i - 1][j]));
        }
    }
    long long ans = 0;
    for(long long i = 1; i <= k; i ++) {
        long long d = i + 1;
        long long res = 1;
        for(long long j = x + 1; j >= x - i + 1; j --) {
            long long u = j;
            if(u % d == 0) {
                u /= d;
                d /= d;
            }
            res = mul(u, res);
        }
        ans = add(ans, mul(res, S[k][i]));
    }

    printf("The sum of power of all number from 1 to %lld is %lld\n", x, ans);
    return 0;
}