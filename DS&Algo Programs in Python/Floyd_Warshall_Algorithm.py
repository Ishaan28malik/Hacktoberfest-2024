''' Floyd Warshal Algorithm'''

cost = [
      [0,1,8],
      [9,0,5],
      [1,7,0]
      ]

n = 3 # Number of Vertices
D = cost 

for k in range(n):
  for i in range(n):
    for j in range(n):
      D[i][j] = min(D[i][j],D[i][k] + D[k][j])

print("Final Shortest Path Matrix")
for i in range(n):
  print(*D[i])
