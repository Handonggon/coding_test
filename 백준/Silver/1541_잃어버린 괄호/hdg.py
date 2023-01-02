import sys
from functools import reduce
input = sys.stdin.readline

s = input().rstrip()

stack = []

number = ''
isPlus = False
for c in s:
    if c.isdecimal():
        number += c
    else:
        stack.append(int(number))
        number = ''
        if isPlus:
            stack.append(stack.pop() + stack.pop())
        isPlus = (c == '+')

print(reduce(lambda acc, cur: acc - cur, stack))

# print(reduce(lambda acc, cur: acc - cur, (map(lambda exp: reduce(lambda acc, cur: acc + cur,list(map(int, exp.split("+")))), input().rstrip().split('-')))))

