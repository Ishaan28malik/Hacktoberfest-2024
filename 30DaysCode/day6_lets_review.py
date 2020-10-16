def lets_review(t):
    #Constraints t and s
    if 1 <= t <= 10:
        s = input()
        if 2 <= len(s) <= 10000:
            even_s, odd_s = '', ''
            for j, letter in enumerate(s):
                if j % 2 == 0:
                    even_s += letter
                else:
                    odd_s += letter
            return print('{} {}'.format(even_s, odd_s)), lets_review(t-1)


if __name__ == '__main__':
    t = int(input())
    lets_review(t)
