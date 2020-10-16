n = int(input())
data = []
while 1 <= n <= 1e5:
    data.append(input().split(' '))
    n -= 1
phonebook = dict(data)

while True:
    try:
        query = input()
        if phonebook.get(query):
            print('{}={}'.format(query, phonebook[query]))
        else:
            print('Not found')
    except:
        break
