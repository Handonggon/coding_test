import sys
input = sys.stdin.readline

minute = 90
interval = 5
prime = [2, 3, 5, 7, 11, 13, 17]

rateA = int(input()) / 100
rateB = int(input())  / 100
N = (minute // interval)
C = [1 for _ in range(N + 1)]
for i in range(N + 1):
    for j in range(i - 1, 0, -1):
        C[j] += C[j - 1]

totalA = 0
totalB = 0
for count in range(N + 1):
    if count in prime:
        continue
    totalA += C[count] * pow(rateA, count) * pow(1 - rateA, N - count)
    totalB += C[count] * pow(rateB, count) * pow(1 - rateB, N - count)

print(1 - (totalA * totalB))