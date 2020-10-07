a = [-2, 3, -16, 100, -4, 51]
n = len(a)
m = [0]*(n+1)
if a[0]>0:
    m[0] = a[0]              # makes negative values eq to 0   
max_val = -1
for i in range(1,n):
    if m[i-1] + a[i] > m[i]:
        m[i] = m[i-1] + a[i]     #uses prefix sum 
        max_val = max(max_val,m[i])
print(max_val)

# Kadane algo (greedy)                                                                     
l=-10000000  #finds local max
g=-10000000  #finds global max
for x in a:
    l = max(l+x,x)          
    g = max(l,g)
print(g)
    
