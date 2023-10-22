import sys
input = sys.stdin.readline

[N, M] = list(map(int, input().split()))
info = list(map(int, input().split()))

[left, right] = [0, max(info)]

def isPossible(mid):
    count = 1
    minimum = info[0]
    maximum = info[0]
    for n in info[1:]:
        minimum = min(minimum, n)
        maximum = max(maximum, n)
        if (maximum - minimum) > mid:
            count += 1
            minimum = n
            maximum = n
    return count <= M

while left <= right:
    mid = (right + left) // 2

    if isPossible(mid):
        right = mid - 1
    else:
        left = mid + 1
print(left)