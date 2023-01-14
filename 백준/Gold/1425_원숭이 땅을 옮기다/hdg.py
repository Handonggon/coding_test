import sys
input = sys.stdin.readline

[X, Y] = [0, 1]
INF = 10000000000

N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]

# N = 3
# info = [[1, 4], [4, 1], [1, 1]]

#length = 최대의 최소값
def isPossible(length):
    [start, end] = [-INF, INF]
    for i in range(N):
        for j in range(i + 1, N):
            a = length - abs(info[i][X] - info[j][X]) - abs(info[i][Y] - info[j][Y])
            if a < 0:
                return False
            s = min(info[i][Y], info[j][Y]) - (a // 2)
            e = max(info[i][Y], info[j][Y]) + (a // 2)
            if e < start or end < s:
                return False

            if start <= s <= end:
                start = s
            elif start <= e <= end:
                end = e
    return True

[left, right] = [0, INF]

answer = INF
while left <= right:
    mid = (left + right) // 2

    if isPossible(mid):
        right = mid - 1
        answer = min(answer, mid)
    else:
        left = mid + 1
print(answer)