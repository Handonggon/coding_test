import sys
input = sys.stdin.readline

line = input().rstrip()
# line = '00000000000000000000000000000000000000000000000000000000000000000000000' # 400

start = 0
for number in range(1, 30001):
    for s in str(number):
        if start < len(line) and line[start] == s:
            start += 1
    if start == len(line):
        break
print(number)