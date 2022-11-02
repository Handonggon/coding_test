N = int(input())
expression = input()
number = [int(input()) for n in range(N)]

OPERATOR = {'+': lambda a, b: a + b
          , '-': lambda a, b: a - b
          , '*': lambda a, b: a * b
          , '/': lambda a, b: a / b}

stack = []
for oper in expression:
    if oper.isalpha():
        stack.append(number[ord(oper) - 65])
    else:
        a = stack.pop();
        b = stack.pop();
        stack.append(OPERATOR[oper](b, a))

print("{:.2f}".format(stack[-1]))