import sys
input = sys.stdin.readline
from math import gcd 

N = int(input())
lcm = 1
for num in set(map(int, list(str(N)))):
    if num == 0:
        continue
    lcm = lcm * num // gcd(lcm, num)

def get(N, lcm):
    size = 1
    while True:
        for suffix in range(size):
            if (N * size + suffix) % lcm == 0:
                return N * size + suffix
        size *= 10

print(get(N, lcm))