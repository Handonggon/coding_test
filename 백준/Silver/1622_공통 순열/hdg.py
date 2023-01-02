import sys
input = sys.stdin.readline
from collections import defaultdict

while True:
    try:
        a = input().rstrip()
        b = input().rstrip()
        alpha1 = defaultdict(int)
        alpha2 = defaultdict(int)

        for s in a:
            alpha1[s] += 1
        for s in b:
            alpha2[s] += 1
        
        answer = ''
        for c in sorted(set(a + b)):
            answer += (c * min(alpha1[c], alpha2[c]))
        print(answer)
    except:
        break