class Solution
{
	public:
	stack <int> st;
	vector<int> rev[5001];
	int scc;
	//Function to find number of strongly connected components in the graph.
    int kosaraju(int V, vector<int> adj[])
    {
       vector<bool> visited(V,false);
       scc = 0;
       for(int i=0;i<V;i++)// Step 1: Perform normal DFS and push the nodes to the stack
       {
           if(!visited[i])
           dfs1(i,adj,visited);
       }
       
      reverse(adj,V); // Step 2: Reverse the edges (Finding Graph Transpose)
       
      for(int i=0;i<V;i++)
      visited[i] = false;
       
       while(!st.empty()) // Step 3: Perform DFS again on the transposed graph
       {
          
           int u = st.top();
           st.pop();
           
           if(!visited[u])
           {
               dfs2(u,rev,visited);
               scc++;
           }
           
           
           
       }
       return scc;
       
    }
    void dfs2(int u,vector<int> rev[],vector<bool> &visited)
    {
        if(visited[u])
        return;
        
        visited[u] = true;
        
        for(int v:rev[u])
        {
           if(!visited[v])
           dfs2(v,rev,visited);
        }
        
    }
    void dfs1(int u,vector<int> adj[],vector<bool> &visited)
    {
        if(visited[u])
        return;
        
        visited[u] = true;
        
        for(int v:adj[u])
        {
           if(!visited[v])
           dfs1(v,adj,visited);
        }
        
        st.push(u);
    }
    
    void reverse(vector<int> adj[],int V)
    {
        for(int i=0;i<V;i++)
        {
            for(int j:adj[i])
            {
                rev[j].push_back(i);
            }
        }
        
       
    }
};