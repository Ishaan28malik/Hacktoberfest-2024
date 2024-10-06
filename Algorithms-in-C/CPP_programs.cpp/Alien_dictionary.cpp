/*......a sorted dictionary of an alien language having N words and k starting alphabets of standard dictionary. 
We have to find the order of characters in the alien language...*/


#include <bits/stdc++.h>
using namespace std;

// Helper function to compare two words based on the alien dictionary order
bool compare(const string &a, const string &b, const unordered_map<char, int> &order_map) {
    int len = min(a.size(), b.size());
    for (int i = 0; i < len; i++) {
        if (a[i] != b[i]) {
            return order_map.at(a[i]) < order_map.at(b[i]);
        }
    }
    return a.size() < b.size(); // If the words are the same up to the minimum length
}

// Topological sort using DFS
void topoSort(int v, vector<int> adj[], vector<bool> &visited, stack<int> &st) {
    visited[v] = true;
    for (int u : adj[v]) {
        if (!visited[u]) {
            topoSort(u, adj, visited, st);
        }
    }
    st.push(v);
}

// Function to find the order of characters in the alien dictionary
string findOrder(string dict[], int N, int K) {
    // Create a graph to store relations between characters
    vector<int> adj[K];

    // Build the graph by comparing adjacent words
    for (int i = 0; i < N - 1; i++) {
        string word1 = dict[i], word2 = dict[i + 1];
        int len = min(word1.size(), word2.size());
        for (int j = 0; j < len; j++) {
            if (word1[j] != word2[j]) {
                adj[word1[j] - 'a'].push_back(word2[j] - 'a');
                break;
            }
        }
    }

    // Perform topological sort to find the order of characters
    stack<int> st;
    vector<bool> visited(K, false);
    for (int i = 0; i < K; i++) {
        if (!visited[i]) {
            topoSort(i, adj, visited, st);
        }
    }

    // Build the result string based on the topological order
    string order;
    while (!st.empty()) {
        order += (char)(st.top() + 'a');
        st.pop();
    }

    return order;
}

// Main function to test the above logic
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, k;
        cin >> n >> k;
        string s[n];
        for (int i = 0; i < n; i++) cin >> s[i];

        // Get the alien dictionary order
        string order = findOrder(s, n, k);

        // Create a map for character positions for efficient sorting
        unordered_map<char, int> order_map;
        for (int i = 0; i < order.size(); i++) {
            order_map[order[i]] = i;
        }

        // Sort the words based on the alien dictionary order
        vector<string> temp(s, s + n);
        sort(temp.begin(), temp.end(), [&](const string &a, const string &b) {
            return compare(a, b, order_map);
        });

        // Check if the sorted array matches the original array
        bool isSortedCorrectly = true;
        for (int i = 0; i < n; i++) {
            if (s[i] != temp[i]) {
                isSortedCorrectly = false;
                break;
            }
        }

        cout << isSortedCorrectly << endl;
    }
    return 0;
}
