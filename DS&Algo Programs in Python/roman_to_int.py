'''
Input:
The first line of each test case contains the no of test cases T
Then T test cases follow. Each test case contains a string s denoting the roman no

Output:
For each test case in a new line print the integer representation of roman number s
'''

def roman_to_int(roman):
    value = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    prev = 0
    ans = 0
    n = len(roman)
    for i in range(n-1, -1, -1):
        if value[roman[i]] >= prev:
            ans += value[roman[i]]
        else:
            ans -= value[roman[i]]

        prev = value[roman[i]]

    print(ans)
'''for _ in range(int(input())):
    s = input()
    roman_to_int(s)
'''
# s = 'V'
# s = 'III'
s = 'XIV'

roman_to_int(s)
