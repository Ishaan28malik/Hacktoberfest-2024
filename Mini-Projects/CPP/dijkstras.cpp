#include<bits/stdc++.h>
using namespace std;
std::vector<std::vector<pair<int,int>>> Graph;
priority_queue<pair<int,int>> pq;
vector<int>visited;
vector<int>distances;
vector<int>parent;
void dijktras()
{
  while(!pq.empty())
  {
    pair<int,int>curr=pq.top();
    pq.pop();
    visited[curr.second]=1;
    curr.first=(-1)*curr.first;
    for(auto x = Graph[curr.second].begin(); x!= Graph[curr.second].end(); x++ )
    {
      if(distances[(*x).first] > (*x).second + distances[curr.second])
        {
          distances[(*x).first] = (*x).second + distances[curr.second];
          parent[(*x).first] = curr.second;
        }
        if(!visited[(*x).first])
        pq.push(make_pair((-1)*distances[(*x).first],(*x).first));
    }
  }
}

int main()
{
  int v,e;
  cin>>v>>e;
  Graph.resize(v+1);
  visited.resize(v+1,0);
  parent.resize(v+1,0);
  distances.resize(v+1,INT_MAX);
  for(int i=0;i<e;i++)
  {
    int v1,v2,wt;
    cin>>v1>>v2>>wt;
    Graph[v1].push_back(make_pair(v2,wt));
    Graph[v2].push_back(make_pair(v1,wt));
  }
  int source=1;
  distances[source]=0;
  pq.push(make_pair(0,source));
  dijktras();
  if(distances[v]==INT_MAX)
    cout<<-1<<endl;
  else
    {
      int temparray[v+1];
      temparray[0]=v;
      int k=0;
      int w = parent[v];
      while(w != 0)
      {
        temparray[++k]=w;
        w=parent[w];
      }
      for(int z=k;z>=0;z--)
        cout<<temparray[z]<<" ";
      cout<<endl;
    }
  return 0;
}
