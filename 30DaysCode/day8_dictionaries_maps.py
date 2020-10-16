def phonebook(n):
    data = []
    while 1 <= n <= 1e5:
        data.append(input().split(' '))
        n -= 1
    return data


def queries(n):
    phone = dict(phonebook(n))
    while True:
        try:
            query = input()
            if phone.get(query):
                print('{}={}'.format(query, phone[query]))
            else:
                print('Not found')
        except:
            break


if __name__ == "__main__":
    n = int(input())
    queries(n)
