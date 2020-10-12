#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

vector<int>dist;
void bfs(int s,vector<vector<int>>a,vector<bool>visited)
{
    visited[s]=true;
    queue<int>q;
    q.push(s);
    dist[s]=0;
    while(!q.empty())
    {
        s=q.front();
        //cout<<s<<" ";
        q.pop();
        for(int i:a[s])
        {
            if(!visited[i]&&dist[i]==-1)
            {
                dist[i]=dist[s]+1;
                visited[i]=true;
                q.push(i);
            }
        }
    }
}

int main() {
  int q;
  cin>>q;
  for(int t=0;t<q;t++)
  {
      int n,m;
      cin>>n>>m;
      vector<vector<int>>a(n);
      for(int i=0;i<m;i++)
      {
          int x,y;
          cin>>x>>y;
          a[x-1].push_back(y-1);
          a[y-1].push_back(x-1);
      }
      int s;
      cin>>s;
      vector<bool>visited(n+1,false);
      dist.resize(n,-1);
      bfs(s-1,a,visited);

      for(int i=0;i<dist.size();i++)
          if(dist[i]==-1)
              cout<<dist[i]<<" ";
          else if(dist[i]!=0)
              cout<<dist[i]*6<<" ";
      cout<<endl;
      dist.clear();

  }
    return 0;
}
