import sys
input = sys.stdin.readline

[N, M] = list(map(int, input().split()))
info = [input().strip() for _ in range(N + M)]
A = set(info[:N])
B = set(info[-M:])

intersection = sorted(A & B) 
print(len(intersection))
for element in intersection:
    print(element)