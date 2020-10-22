num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter the operator: ")
if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    result = num1 / num2

print('The result is: '+str(result))


