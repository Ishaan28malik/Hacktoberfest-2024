#include <bits/stdc++.h>
using namespace std;
#define ll long long int

/*

Given a Number N , find the no. of set BIts ( bits = 1) in its binary form .

Logic - To make the num in binary form , keep on dividing the no. by 2 and store int part (it becomes 0) and then store the remainder
in each stepv , then reverse all of them . 

e.g. - N =6  , 6/2 (r=0) , 3/2(r=1) , 1/2 (r=1) , 0 (stop , no storing) reverse all em - 011 -> 110 , hence 6 = '110' (binary form) setbits =2

*/

 int setBits(int N) {
        int set_bits = 0 ;

        while(N>0){
            if(N%2)set_bits++ ;
            N/=2 ;
        }

        return set_bits ;
    }

// TC - O (log n) sinfe n /=2 


/*

ANOTHER ALGORITHM - Brian Kernighan Algo.

-> if you sbtract 1 from a number N , then ALL the bits after the rightmost SET BIT (including it) gets flipped in N-1 .
  e.g. - N = 6(1 10) , N-1 = 5(1 01)

-> COROLary - doing bitwise & will UNSET the rightmost set bit of N (that is rightmost set bit(1) of N will become 0) .

-> so to count no of set bits in N , do the bitwise '&' operation with N & N-1 that will make the rightmost set bit =0 
and now assign thi new value to N and again repeta the operation to make the next rightmost set bit = 0 and do so till
whole num. becomes = hence TC reduces since we only travelled through set bits .

*/

int Brian_Ker_Algo(int N){
    int set_bits =0 ;

    while(N>0){
        
        int bit = N & (N-1) ; // unset th rightmost bit 

        set_bits++; // at each step of succesful itr(N!=0) means 1 bit has been encountered

        N = bit ; // assigh this new unset bit value to N till it becomes 0

    }

    return set_bits ;
}

int main()
{

int N  = 6 ;

cout << setBits(N) << endl ; //2(110 = 6)

N = 7 ;

cout << Brian_Ker_Algo(N) << endl ; // 3 (111 = 7 )
  return 0;
}
