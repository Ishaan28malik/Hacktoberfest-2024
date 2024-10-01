# Write a python program that takes two arrays a, b of length n storing integers
# Return an array c that holds the dot product of a,b

def dotprod(a,b):
    if len(a) != len(b):
        print('Unequal arrays!')
    else:
        c = [i*j for i,j in zip(a,b)]
        print(c)

l1 = [2,3,4,5]
l2 = [5,6,7]
dotprod(l1, l2)

















