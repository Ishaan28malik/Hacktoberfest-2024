// Program to print the given pattern 
import java.util.*; 
class GFG 
{ 
static void print_asterisk(int asterisk) 
{ 
	if (asterisk == 0) 
		return; 
	System.out.print("* "); 
	print_asterisk(asterisk - 1); 
} 
static void print_space(int space) 
{ 
	if (space == 0) 
		return; 
	System.out.print(" "); 
	System.out.print(" "); 
	print_space(space - 1); 
} 

// function to print the pattern 
static void pattern(int n, int num) 
{ 
	// base case 
	if (n == 0) 
		return; 
	print_asterisk(n); 
	print_space(2 * (num - n) + 1); 
	print_asterisk(n); 
	System.out.print("\n"); 

	// recursively calling pattern() 
	pattern(n - 1, num); 
} 

// Driver Code 
public static void main(String[] args) 
{ 
	int n = 5; 
	pattern(n, n); 
} 
} 

// This code is contributed by PrinciRaj1992 
