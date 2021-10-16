"""
MATRIX ROTATION IN PLACE IN 
CLOCKWISE DIRECTION
"""

a=[[1,2,3],[4,5,6],[7,8,9]]
print('',a[0],'\n',a[1],'\n',a[2],'\n')

# SWAPPING 1st AND 3rd ROWS
for i in range(3):
  for j in range(1):
    a[j][i],a[2-j][i]=a[2-j][i],a[j][i]
# print('',a[0],'\n',a[1],'\n',a[2],'\n')

# TRANSPOSE OF MATRIX
for i in range(3):
  for j in range(3):
    if i<j:
      a[i][j],a[j][i]=a[j][i],a[i][j]
print('',a[0],'\n',a[1],'\n',a[2])

"""
★MATRIX:-
 [1, 2, 3]
 [4, 5, 6]
 [7, 8, 9]
★After rotation:-
 [7, 4, 1] 
 [8, 5, 2] 
 [9, 6, 3]
"""
