// objective of the puzzle is to move the stack of disks from rod A to rod C using auxiallary rod B

#include<stdio.h>

void towerOfHanoi(int n, char from_rod, char to_rod, char aux_rod)
{
    if(n==1)
    {
        printf("\n Move 1 disk from rod %c to rod %c", from_rod, to_rod);
        return;
    }
    
    towerOfHanoi(n-1, from_rod, aux_rod, to_rod);
    printf("\n Move disk %d from rod %c to rod %c ", n, from_rod, to_rod); 
    towerOfHanoi(n-1, aux_rod, to_rod, from_rod); 
}

int main() 
{ 
    int n = 1; // Number of disks 
    towerOfHanoi(n, 'A', 'C', 'B');  // A, B and C are names of rods 
    return 0; 
} 

// For n disks , total 2^n-1 moves are required and 2^(n-1) function calls are made
