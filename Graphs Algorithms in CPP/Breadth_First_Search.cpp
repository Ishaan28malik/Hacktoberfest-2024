#include<bits/stdc++.h>
using namespace std;

class Solution
{
    public:

    // function to return breadth-first traversal of a given graph
    // res returns the vector containing BFS of the graph


	vector<int>BFS(int V, vector<int> adj[])
	{
	    vector<int> res;
	    queue<int> q;
	    vector<bool> visited(V, false);
	    
	    q.push(0);
	    
	    while(!q.empty())
	    {
	        int top = q.front();
	        q.pop();
	        
	        if(visited[top] == true)
	        continue;
	        
	        visited[top] = true;
	        res.push_back(top);
	        
	        for(int i = 0; i < adj[top].size(); i++)
	        {
	            if(!visited[adj[top][i]])
	            q.push(adj[top][i]);
	        }
	    }
	    
	    return res;
	}
};

// driver code 

int main()
{

	// V -> vertices, E -> edges
	int V, E;
	cin >> V >> E;

	vector<int> adj[V];

	for(int i = 0; i < E; i++)
	{
		int u, v;
		cin >> u >> v;
		adj[u].push_back(v);
	}

	/* custom input example
		               0
		            /     \
		           1       2
		          / \     / \
		         3  NULL NULL NULL
		        / \
		     NULL NULL

		V = 4, E = 3, 
		4 3
		0 1
		0 2
		1 3
    */
    
    Solution obj;

    vector<int>ans = obj.BFS(V, adj);

    for(int i=0;i<ans.size();i++){

    	cout << ans[i] << " ";
    }
    
    cout<<endl;

	return 0;
} 