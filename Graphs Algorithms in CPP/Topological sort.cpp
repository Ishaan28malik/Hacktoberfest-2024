class Solution
{
	public:
	stack<int> st;
	//Function to return list containing vertices in Topological order. 
	vector<int> topoSort(int V, vector<int> adj[]) 
	{
	   vector<bool> visited(V,false);
	   
	   for(int i=0;i<V;i++)
	   {
	       if(!visited[i])
	       dfs(i,adj,visited);
	   }
	   vector<int> res;
	   
	   while(!st.empty())
	   {
	       res.push_back(st.top());
	       st.pop();
	   }
	   
	   return res;
	}
	
	void dfs(int u,vector<int> adj[],vector<bool>& visited)
	{
	    if(visited[u])
	    return;
	    
	    visited[u] = true;
	    
	    for(int v:adj[u])
	    {
	        if(!visited[v])
	        dfs(v,adj,visited);
	    }
	    st.push(u);
	}
};