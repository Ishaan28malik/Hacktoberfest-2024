//input n->number of vertices
//input m->number of edges
//input a,b,c->edge from a to b with capacity c
//Output max_flow->max_flow between 1 and n vertex

#include<bits/stdc++.h>
#define lld long long
#define pb push_back
#define mk make_pair
#define MAX (lld)1e18+7
#define lim (lld)1e18+7
#define MAX2 (lld)1e18+9
#define ff first
#define ss second
#define fastio ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);
using namespace std;
 
const lld mod=lim;
 
lld power(lld x, lld y, lld p)  
{   lld res = 1;     x = x % p; if (x == 0) return 0;  
  
    while (y > 0)  
    { if (y & 1) res = (res*x) % p;  y = y>>1; x = (x*x) % p;   }  
    return res;  } 
 
 
lld extend_gcd(lld a, lld b, lld& x, lld& y) {
    if (b == 0) { x = 1;y = 0;return a;}
    lld x1, y1;
    lld d = extend_gcd(b, a % b, x1, y1);
    x = y1; y = x1 - y1 * (a / b);return d;	}
 
lld rowNum[]={-1,0,0,1};
lld colNum[]={0,-1,1,0};
lld n,m;
vector<vector<lld>> capacity,flow;
std::vector<lld> height,excess,seen;
queue<lld>excess_vertices;
 
void push(lld u,lld v)
{
	lld d = min(capacity[u][v]-flow[u][v],excess[u]);
	flow[u][v]+=d;
	flow[v][u]-=d;
	excess[u]-=d;
	excess[v]+=d;
 
	if(d>0 && excess[v]==d)
		excess_vertices.push(v);
}
 
void relabel(lld u)
{
	lld d=MAX2;
 
	for(lld i=0;i<n;i++)
	{
		if(capacity[u][i]-flow[u][i]>0)
			d = min(d,height[i]);
	}
 
	if(d<MAX2)
	height[u] = 1+d;
}
 
void discharge(lld u)
{
	while(excess[u]>0)
	{
		if(seen[u]<n)
		{
			lld v=seen[u];
			if(capacity[u][v]-flow[u][v]>0 && height[u]>height[v])
				push(u,v);
			else
				seen[u]++;
		}
 
		else
		{
			relabel(u);
			seen[u]=0;
		}
	}
}
 
int main()
{
	fastio
	cin>>n>>m;
	capacity.resize(n,vector<lld>(n,0));
	flow.resize(n,vector<lld>(n,0));
	for(lld i=0;i<m;i++)
	{
		lld a,b,c;
		cin>>a>>b>>c;
		a--;
		b--;
		capacity[a][b]+=c;
	}
 
	height.resize(n,0);
	height[0]=n;
	excess.resize(n,0);
	excess[0]=MAX2;
	for(lld i=1;i<n;i++)
		push(0,i);
	seen.assign(n,0);
 
	while(!excess_vertices.empty())
	{
		lld u=excess_vertices.front();
		excess_vertices.pop();
		if(u!=0 && u!=n-1)
			discharge(u);
	}
 
	lld max_flow = 0;
 
	for(lld i=0;i<n;i++)
		max_flow += flow[0][i];
 
	cout<< max_flow<<endl;
	
}