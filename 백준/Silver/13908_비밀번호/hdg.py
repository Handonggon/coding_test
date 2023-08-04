import sys
input = sys.stdin.readline

def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    return 1

def nCr(n, r):
    return int(factorial(n) / (factorial(n - r) * factorial(r)))


[n, m] = map(int, input().split())
answer = pow(10, n)
if m > 0:
    info = list(map(int, input().split()))
    for i in range(1, m + 1):
        answer += pow(-1, i) * pow(10 - i, n) * nCr(m, i)
print(answer)