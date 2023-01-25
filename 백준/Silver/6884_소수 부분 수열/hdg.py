import math
import sys
input = sys.stdin.readline

def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

T = int(input())
for t in range(T):
    [n, *info] = list(map(int, input().split()))

    subtotal = [0]
    for number in info:
        subtotal.append(number + subtotal[-1])

    answer = False
    for x in range(2, n + 1):
        for index in range(n - x + 1):
            if isPrime(subtotal[index + x] - subtotal[index]):
                print('Shortest primed subsequence is length {0}:'.format(x), end=' ')
                print(*info[index:index + x])
                answer = True
                break
        if answer:
            break
    if not answer:
        print('This sequence is anti-primed.')