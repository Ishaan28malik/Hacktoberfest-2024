// Strongly connected components of graph
#include<bits/stdc++.h>
using namespace std;
void addEdge(vector<pair<int, int>> adj[], int u, int v, int w){
	adj[u].push_back({v, w});
}
void dfsrec(vector<pair<int, int>> adj[], int V, int u, vector<bool> &visited){
	visited[u] = true;
	for(auto x : adj[u]){
		if(!visited[x.first])
			dfsrec(adj, V, x.first, visited);
	}
	cout << u << " ";
}
void dfs(vector<pair<int, int>> adj[], int V){
	vector<bool> visited(V, false);
	if(V <= 0)
		return;
	cout << endl;
	for(int i = 0; i < V; i++){
		if(!visited[i]){
			dfsrec(adj, V, i, visited);
		}
	} 
	cout << endl;
}
void indegree(vector<pair<int, int>> adj[], int V, vector<int> &indeg){
	for(int i = 0; i < V; i++){
		for(auto x : adj[i]){
			indeg[x.first]++;
		}
	}
}
void dfsrec(vector<pair<int, int>> adj[], int u, stack<int> &s, vector<bool> &visited){
	for(auto x : adj[u]){
		if(!visited[x.first])
		{
			visited[x.first] = true;
			dfsrec(adj, x.first, s, visited);
		}
	}
	s.push(u);
}
void rev(vector<pair<int, int>> adj[], vector<pair<int, int>> adjrev[], int V){
	for(int i = 0; i < V; i++){
		for(auto x : adj[i]){
			adjrev[x.first].push_back({i, 0});
		}
	}
}
int scc(vector<pair<int, int>> adj[], int V){
	stack<int> s;
	vector<bool> visited(V, false);
	for(int i = 0; i < V; i++){
		if(!visited[i]){
			visited[i] = true;
			dfsrec(adj, i, s, visited);
		}
	}
	//show(s);
	int c = 0;
	vector<pair<int, int>> adjrev[V]; 
	rev(adj, adjrev, V);
	vector<bool> visitedd(V, false);
	cout << "Strongly connected components are\n";
	while(!s.empty()){
		int u = s.top();
		s.pop();
		if(!visitedd[u]){
			dfsrec(adjrev, V, u, visitedd);
			cout << endl;
			c++;
		}
	}
	return c;
}
int main(){
	int V = 6;
	vector<pair<int, int>> adj[V];
	addEdge(adj, 0, 1, 10);
	addEdge(adj, 4, 2, 10);
	addEdge(adj, 4, 5, 30);
	addEdge(adj, 3, 4, 90);
	addEdge(adj, 2, 1, 10);
	addEdge(adj, 3, 5, 30);
	addEdge(adj, 1, 4, 90);
	addEdge(adj, 4, 0, 100);
	scc(adj, V);
	return 0;
}
