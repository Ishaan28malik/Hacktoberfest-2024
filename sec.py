
# Python program to print all EVEN numbers within an interval
l = 10
u = 20
if l%2==0:
    for num in range(l, u + 1, 2):
        print(num)
else:
    for num in range(l+1, u + 1, 2):
        print(num)
