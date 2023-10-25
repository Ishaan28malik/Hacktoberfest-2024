// Problem: there are two strings check if all the chars of string2 are in string 1
// Protonshub placement drive #string #set

#include <iostream>
#include <set>
#include <algorithm>
using namespace std;

bool isContained(string s1, string s2)
{
    set<int> s1char;
    set<int> s2char;

    for (auto &i : s1)
        s1char.insert(i);
    for (auto &i : s2)
        s2char.insert(i);
    return includes(s1char.begin(), s1char.end(), s2char.begin(), s2char.end());
}

int main()
{
    string s1 = "united";
    string s2 = "tie";
    cout << isContained(s1, s2) << endl;

    return 0;
}
