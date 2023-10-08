import sys
input = sys.stdin.readline

S = list(input().strip())

stack = []
for i in range(len(S)):
    if S[i] == "(":
        stack.append("(")
    elif S[i] == ")":
        count = 0
        while True:
            c = stack.pop()
            if c == "(":
                break
            count += c
        stack.append(stack.pop() * count)
    elif i < len(S) - 1 and S[i + 1] == "(":
        stack.append(int(S[i]))
    else:
        stack.append(1)
print(sum(stack))