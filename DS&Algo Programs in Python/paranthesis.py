class Stack():
    def __init__(self):
        self.a = []
        self.top = -1

    def push(self, ele):
        self.a.append(ele)
        self.top += 1

    def pop(self):
        self.a.pop()
        self.top -= 1

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
        
s = Stack()

userIn1 = input('Please provide paranthesis:')
counter = 0

for i in userIn1:
    if i == '(':
        s.push(1)
        counter += 1
    elif i == ')':
        if s.isEmpty():
            counter -= 1
        else:
            s.pop()
            counter -= 1
    else:
        continue

if counter == 0:
    print('There are equal number of paranthesis')
else:
    print('There are unequal number of paranthesis')
        
ns = Stack()
userIn2 = input('Please provide html tags:')
counter = 0

for i in userIn2:
    if i == '<':
        ns.push(1)
        counter += 1
    elif i == '>':
        if ns.isEmpty():
            counter -= 1
        else:
            ns.pop()
            counter -= 1
    else:
        continue

if counter == 0:
    print('There are equal number of html tags')
else:
    print('There are unequal number of html tags')
