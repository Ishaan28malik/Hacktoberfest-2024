for _ in range(int(input())):
    a,b,k = map(int,input().split())
    count = 0
    for i in range(a,b+1):
        li = []
        while i%2 == 0:
            i /= 2
            li.append(2)
        j = 3
        while i != 1:
            if i%j == 0:
                i /= j
                li.append(j)
            else:
                j += 2
        if len(set(li)) == k:
            count += 1
    print(count)
