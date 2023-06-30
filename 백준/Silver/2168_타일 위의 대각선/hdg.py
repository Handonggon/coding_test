import sys
import math
input = sys.stdin.readline

[x, y] = map(int, input().split())
gcd = math.gcd(x, y)
print(int((((x / gcd) + (y / gcd)) - 1) * gcd))