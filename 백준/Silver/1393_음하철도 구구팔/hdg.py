import sys
import math
input = sys.stdin.readline

[xs, ys] = list(map(int, input().split()))
[xe, ye, dx, dy] = list(map(int, input().split()))

def getGcd(a, b):
    while b:
        a, b = b, a%b
    return a
 
def getDistance(x1, y1, x2, y2):
    return math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

gcd = getGcd(dx, dy)
dx = dx // gcd
dy = dy // gcd

while getDistance(xs, ys, xe, ye) > getDistance(xs, ys, xe + dx, ye + dy):
    xe += dx
    ye += dy

print(xe, ye)