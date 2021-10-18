c = input('Enter the ciphered text: ')
c = c.upper()
print('Enter the key alphabet wise without repetition :')
p = ''
k = ''
j = ''
dict = {}

for i in range (65,91):
    p = chr(i)
    k = input(p+': ')
    k = k.upper()
    dict.update({k:p})

for char in c:
    j = j+dict[char]

print (j)
