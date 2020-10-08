for _ in range(int(input())):
    n = int(input())
    s = input()
    stack = []
    operand = []
    operator = {'+':1, '-':1, '*':2, '/':2, '^':3}
    for i in range(len(s)):
        if s[i].isalpha():
            operand.append(s[i])
        elif s[i] == '(':
            stack.append(s[i])
        elif s[i] == ')':
            while stack[-1] != '(':
                p = stack.pop()
                operand.append(p)
            stack.pop()
        else:
            # since stack.pop() in line 16 ain't executing 
            '''if operator[s[i]] > operator[stack[-1]]:
                stack.append(s[i])
            elif operator[s[i]] <= operator[stack[-1]]:
                while len(stack) != 0:
                    operand += stack.pop()'''
            while len(stack) != 0 and stack[-1] in operator and s[i] in operator and operator[stack[-1]] >= operator[s[i]]:
                operand += stack.pop()
            stack.append(s[i])      
    while len(stack) != 0:
        operand += stack.pop()
        #operand.append(s[i])
    print(operand)
                
