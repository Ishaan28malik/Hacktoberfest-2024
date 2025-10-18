class Et:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def isOperator(c):
    if (c == '+' or c == '-' or c == '*' or c == '/' or c == '^'):
        return True
    else:
        return False

def inorder(t):
    ar = []
    if t is not None:
        inorder(t.left)
        print(t.value)
        inorder(t.right)

def constructTree(postfix):
    stack = []

    for char in postfix:

        if not isOperator(char):
            t = Et(char)
            stack.append(t)

        else:
            t = Et(char)
            t1 = stack.pop()
            t2 = stack.pop()

            t.right = t1
            t.left = t2

            stack.append(t)

    t = stack.pop()

    return t

postfix = "ab+c-"
r = constructTree(postfix)
print("Infix expression is")
inorder(r)
