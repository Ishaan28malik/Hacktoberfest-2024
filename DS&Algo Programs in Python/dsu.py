from math import *

edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
n = 5
m = len(edges)

for i in range(len(edges)):
	edges[i].append(i)
edges.sort(key = lambda edges: edges[2])


parent=[-1]*n
def findp(u):
	if(parent[u]<0):
		return u
	return findp(parent[u])
def find_parent(u):
	p = findp(u)
	if(u!=p):
		parent[u]=p
	return p

def union(u,v):
	p1=find_parent(u)
	p2=find_parent(v)
	if(p1==p2):
		return False
	if(abs(parent[p1])>=abs(parent[p2])):
		parent[p1]+=parent[p2]
		parent[p2]=p1
	else:
		parent[p2]+=parent[p1]
		parent[p1]=p2
	return True

ans=0
for i in range(len(edges)):
	if(union(edges[i][0],edges[i][1])):
		ans+=edges[i][2]
print(ans)