# BFS Traversal Function		
def bfs(l, start_node, goal_node):
	visited = [0]*10
	visited[start_node] = 1
	print('BFS : ', end = " ")
	print(start_node, end = " ")
	s = [start_node]
	k = start_node
	while k != goal_node:
		k = s.pop()
		p = -1
		for i in l[k]:
			p += 1
			if i == 1 and visited[p] != 1:
				if p == goal_node:
					print('-->', end = " ")
					print(p, end = " ")
					k = p
					break
				print('-->', end = " ")
				print(p, end = " ")
				visited[p] = 1
				s.insert(0, p)
				

## main program

# Graph Declaration
l = [[0,0,0,1,0,1,1,0,1,1],
     [0,0,1,1,1,1,1,1,0,1], 
     [0,1,0,0,1,1,0,1,1,1], 
     [1,1,0,0,0,0,1,0,0,0], 
     [0,1,1,0,0,0,1,0,1,1], 
     [1,1,1,0,0,0,1,0,0,1], 
     [1,1,0,1,1,1,0,1,0,1], 
     [0,1,1,0,0,0,1,0,1,1], 
     [1,0,1,0,1,0,0,1,0,0], 
     [1,1,1,0,1,1,1,1,0,0]]

# DFS Traversal
start_node = 0
goal_node = 4
dfs(l, start_node, goal_node)
print()


