/* Enter the complete sentence and remove the duplicity from it. */

#include <bits/stdc++.h>

using namespace std;

int main()
{
    string sent,word;
    vector <string> hsh;
    getline(cin,sent);
    stringstream sh(sent);
    do
    {
        sh>>word;
        auto ser=find(hsh.begin(),hsh.end(),word);
        if(ser==hsh.end())
        {
            cout<<word<<" ";
            hsh.push_back(word);
        }

    }while(sh);
    return 0;
}
