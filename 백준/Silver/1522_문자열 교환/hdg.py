import sys
input = sys.stdin.readline

info = input().strip()

window = info.count('a')
answer = window
for i in range(len(info)):
    answer = min(answer, (info + info)[i:i + window].count('b'))
print(answer)