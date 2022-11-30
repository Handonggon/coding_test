import sys
input = sys.stdin.readline

[X, Y] = list(map(int, input().split()))

# [X, Y] = [45, 49]
# [X, Y] = [45, 50]

def gaussSum(num):
    return (num * (num + 1)) / 2

left, right = [0, Y - X]
# left, right = [0, pow(2, 31)]

while left <= right:
    mid = (left + right) // 2

    if mid % 2:
        if gaussSum(mid // 2 + 1) + gaussSum(mid // 2) >= Y - X:
            right = mid - 1
        else:
            left = mid + 1
    else:
        if 2 * gaussSum(mid // 2) >= Y - X:
            right = mid - 1
        else:
            left = mid + 1

print(left)