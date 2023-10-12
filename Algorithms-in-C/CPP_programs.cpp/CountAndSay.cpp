// output count and say sequence with each number in the sequence
#include<iostream>
#include<string>
using namespace std;

/**
 * Returns the nth term of the count-and-say sequence.
 * 
 * The count-and-say sequence is a sequence of integers where each term is the description of the previous term.
 * The description of term n is formed by reading the description of term n-1, and counting the number of digits in groups of the same digit.
 * 
 * @param n The index of the term to return.
 * @return The nth term of the count-and-say sequence.
 */

string countAndSay(int n) {
    if (n == 1) return "1";
    string s = countAndSay(n-1);
    string res = "";
    int count = 1;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == s[i+1]) {
            count++;
        } else {
            res += to_string(count) + s[i];
            count = 1;
        }
    }
    return res;
}

int main(void) {
    int n = 4;
    cout << countAndSay(n) << endl;
    return 0;
}

// Time Complexity: O(n^2)
// Space Complexity: O(n)
// n is the number of elements in the sequence
// this is a recursive solution
// we can also use a iterative solution
