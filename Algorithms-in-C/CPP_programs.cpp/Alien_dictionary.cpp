/*......a sorted dictionary of an alien language having N words and k starting alphabets of standard dictionary. 
We have to find the order of characters in the alien language...*/


#include <bits/stdc++.h>

using namespace std;

string findOrder(string[], int, int);
string order;
bool f(string a, string b) {
    int p1 = 0;
    int p2 = 0;
    for (int i = 0; i < min(a.size(), b.size()) and p1 == p2; i++) {
        p1 = order.find(a[i]);
        p2 = order.find(b[i]);
        
    }

    if (p1 == p2 and a.size() != b.size()) return a.size() < b.size();

    return p1 < p2;
}

//  program to test above functions
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, k;
        cin >> n >> k;
        string s[n];
        for (int i = 0; i < n; i++) cin >> s[i];

        string ss = findOrder(s, n, k);
        order = "";
        for (int i = 0; i < ss.size(); i++) order += ss[i];

        string temp[n];
        std::copy(s, s + n, temp);
        sort(temp, temp + n, f);

        bool f = true;
        for (int i = 0; i < n; i++)
            if (s[i] != temp[i]) f = false;

        cout << f;
        cout << endl;
    }
    return 0;
}



/*
dict : array of strings denoting the words in alien langauge
N : Size of the dictionary
K : Number of characters
*/
stack<int> st;

void tops(vector<int> g[],int vertex,int visited[])
{
    if(visited[vertex])
        return;
    visited[vertex]=1;
    vector<int>::iterator it;
    for(it=g[vertex].begin();it!=g[vertex].end();it++)
    {
        tops(g,*it,visited);
    }
    
    st.push(vertex);
}

string findOrder(string dict[], int N, int K) {
    // Your code here
    vector<int> *g;
    g=new vector<int>[K];
    for(int i=0;i<N-1;i++)
    {
        string word1=dict[i];
        string word2=dict[i+1];
        int j=0;
        while(j<word1.size()&&j<word2.size())
        {
            if(word1[j]!=word2[j])
            {
                int s=word1[j]-'a';
                int d=word2[j]-'a';
                g[s].push_back(d);
                break;
            }
            j++;
        }
    }
    int visited[26]={0};
    for(int i=0;i<K;i++)
        if(!visited[i])
            tops(g,i,visited);
    string ans;
    while(!st.empty())
    {
        ans.push_back(st.top()+'a');
        st.pop();
    }
    //cout<<ans<<endl;
    return ans;
}