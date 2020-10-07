import sys

n = 10
data = []
for i in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length of Array: ', a, ' Size of Array(bytes): ',  b)
    data.append(n)
