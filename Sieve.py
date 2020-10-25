p = [0]*1000001
    
def sieve():
    for i in range(3, 1000001, 2):
        p[i] = 1
    for i in range(3, 1000001, 2):
        if p[i] == 1:
            for j in range(i*i, 1000001, i):
                p[j] = 0

    p[2] = 1

sieve()
