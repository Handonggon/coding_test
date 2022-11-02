[a, b] = list(map(int, input().split()))

def gcd(a, b):
    while b != 0:
        [a, b] = [b, a % b]
    return a

def lcm(a, b):
    return int((a * b) / gcd(a, b))

print(gcd(max(a, b), min(a, b)))
print(lcm(max(a, b), min(a, b)))