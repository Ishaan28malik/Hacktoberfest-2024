# Program to add two matrices using nested loops

# 3x3 matrix
X = [
    [12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# 3x4 matrix
Y = [
    [5, 8, 1, 5],
    [6, 7, 3, 4],
    [4, 5, 9, 7]
]
# result is 3x4
result = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# iterate through rows of X
for i in range(len(X)):
    # iterate through columns of Y
    for j in range(len(X[0])):
            result[i][j] += X[i][j] + Y[i][j]

for r in result:
    print(r)