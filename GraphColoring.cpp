#include<iostream>
#include "bits/stdc++.h"
// #include<vector>

using namespace std;

queue <int> q;
int flag=0;
long long n=100000;
int v, e, v1,v2, visited[10000],level[100000], pop=1, colour[100000],c=1;
vector<int> g[100000];

void bfs(int i)
{
  level[1]=1;
  //cout<<i<<" at level = "<<level[i]<<endl;
  visited[i]=1;
  colour[i]=c;
  c=0;
  q.push(i);


  while(!q.empty())
  {
    for(int j=0; j<g[q.front()].size(); j++)
    {

      if(visited[g[q.front()][j]]!=1)
      {
        //cout<<g[q.front()][j]<<" at level =  "<<level[q.front()]+1<<endl;
        level[g[q.front()][j]]=level[q.front()]+1;
        q.push(g[q.front()][j]);
        visited[g[q.front()][j]]=1;
        colour[g[q.front()][j]]=1 - colour[q.front()];


      }
      else
      {
        if(colour[g[q.front()][j]]==c)
        {
          cout<<"-1";
	  flag=-1;
          return;
        }
      }

    }


    q.pop();
  }


}

int main(){

  int v, e, v1,v2;
  cin>>v>>e;
  g[v+1].resize(v+1);

  for(int i=0;i<e;i++)
  {
    cin>>v1>>v2;
    g[v1].push_back(v2);
    g[v2].push_back(v1);
  }


  for(int i=1;i<v+1;i++)
  {
    cout<<i<<":  ";
    for( vector<int>::iterator it=g[i].begin(); it!=g[i].end(); it++)
      cout<<(*it)<<" ";
    cout<<endl;
  }

  // cout<<g[1].size();
  cout<<"BFS"<<endl;
  bfs(1);

  if(flag==-1)
	cout <<"\nNot possible\n";

  else{
  cout<<"COLOURING\n";

  for(int i=1; i<=v;i++)
  {
    cout<<i<<":"<<colour[i]<<endl;
  }
}

}
