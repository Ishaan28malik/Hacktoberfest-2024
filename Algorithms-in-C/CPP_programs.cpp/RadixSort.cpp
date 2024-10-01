// This file contains the code for Radix Sort algorithm in CPP.

//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

void helper(int arr[], int n, int exp)
{
    vector<int> count(10, 0);
    for (int i = 0; i < n; i++)
        count[(arr[i] / exp) % 10]++;
    for (int i = 1; i < 10; i++)
        count[i] += count[i - 1];
    int output[n] = {0};
    for (int i = n - 1; i >= 0; i--)
    {
        output[count[(arr[i] / exp) % 10] - 1] = arr[i];
        count[(arr[i] / exp) % 10]--;
    }
    for (int i = 0; i < n; i++)
        arr[i] = output[i];
}

void radixSort(int arr[], int n)
{
    // code here
    int maxEl = INT_MIN;
    for (int i = 0; i < n; i++)
        maxEl = max(arr[i], maxEl);
    for (int exp = 1; maxEl / exp > 0; exp *= 10)
        helper(arr, n, exp);
}

//{ Driver Code Starts.

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        int arr[n];

        for (int i = 0; i < n; i++)
            cin >> arr[i];

        radixSort(arr, n);

        for (int i = 0; i < n; i++)
            cout << arr[i] << " ";

        cout << endl;
    }
    return 0;
}
// } Driver Code Ends

// This file is contributed by Siddhartha Chakrabarty