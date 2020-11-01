// C++ program to Convert given Matrix 
// into sorted Spiral Matrix 
#include <bits/stdc++.h> 
using namespace std; 

const int MAX = 1000; 

// Function to convert the array to Spiral 
void ToSpiral(int m, int n, 
			int Sorted[], int a[MAX][MAX]) 
{ 
	// For Array pointer 
	int index = 0; 

	// k - starting row index 
	// m - ending row index 
	// l - starting column index 
	// n - ending column index 
	int k = 0, l = 0; 

	while (k < m && l < n) 
	{ 

		// Print the first row 
		// from the remaining rows 
		for (int i = l; i < n; ++i) 
		{ 
			a[k][i] = Sorted[index]; 
			index++; 
		} 

		k++; 

		// Print the last column 
		// from the remaining columns 
		for (int i = k; i < m; ++i) 
		{ 
			a[i][n - 1] = Sorted[index]; 
			index++; 
		} 
		n--; 

		// Print the last row 
		// from the remaining rows 
		if (k < m) 
		{ 
			for (int i = n - 1; i >= l; --i) 
			{ 
				a[m - 1][i] = Sorted[index]; 
				index++; 
			} 
			m--; 
		} 

		// Print the first column 
		// from the remaining columns 
		if (l < n) 
		{ 
			for (int i = m - 1; i >= k; --i) 
			{ 
				a[i][l] = Sorted[index]; 
				index++; 
			} 
			l++; 
		} 
	} 
} 

// Function to convert 2D array to 1D array 
void convert2Dto1D(int y[MAX][MAX], 
				int m, int n,int x[]) 
{ 

	int index = 0; 

	// Store value 2D Matrix To 1D array 
	for (int i = 0; i < m; i++) 
	{ 
		for (int j = 0; j < n; j++) 
		{ 
			x[index] = y[i][j]; 
			index++; 
		} 
	} 
} 

// Function to print the Matrix 
void PrintMatrix(int a[MAX][MAX], 
				int m, int n) 
{ 

	// Print Spiral Matrix 
	for (int i = 0; i < m; i++) 
	{ 
		for (int j = 0; j < n; j++) 
		{ 
			cout << a[i][j] << " "; 
		} 
		cout << endl; 
	} 
} 


// Function to Convert given Matrix 
// into sorted Spiral Matrix 
void convertMatrixToSortedSpiral( 
	int y[MAX][MAX], int m, int n) 
{ 
	int a[MAX][MAX] = {0}; 
	int x[m * n]; 

	convert2Dto1D(y, m, n,x); 
	sort(x, x + n * m); 
	ToSpiral(m, n, x, a); 
	PrintMatrix(a, m, n); 
} 

// Driver code 
int main() 
{ 
	int m = 4, n = 3; 
	int y[MAX][MAX] = { 
		{ 2, 5, 12 }, 
		{ 22, 45, 55 }, 
		{ 1, 6, 8 }, 
		{ 13, 56, 10 }}; 

	convertMatrixToSortedSpiral(y, m, n); 

	return 0; 
} 

