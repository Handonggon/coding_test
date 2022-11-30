import sys
input = sys.stdin.readline

M = str(input()).strip()[::-1]

answer = 0
for i in range(len(M)):
    answer += (int(M[i]) - (int(M[i]) > 4)) * pow(9, i)
print(answer)