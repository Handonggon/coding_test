import sys
input = sys.stdin.readline

[INDEX, LENGHT] = [0, 1]

while True:
    t = int(input())
    if t == 0:
        break
    info = [int(input()) for _ in range(t)]

    def isPossible(length):
        points = list(filter(lambda item: item[1]>=length, enumerate(info)))
        if len(points) >= 3:
            stand = points.pop();
            for i in range(len(points) - 1):
                point1 = points[i]
                point2 = points[i + 1]

                arc1 = (abs(stand[INDEX] - point1[INDEX]) / t)
                arc2 = (abs(stand[INDEX] - point2[INDEX]) / t)
                if 0.5 <= arc1 < 0.75 and 0.25 <= arc2 < 0.5:
                    return not (arc1 == 0.5 and arc2 == 0.25)
        return False

    [left, right] = [min(info), max(info)]

    answer = left
    while left <= right:
        mid = (left + right) // 2
        if isPossible(mid):
            left = mid + 1
            answer = max(answer, mid)
        else:
            right = mid - 1
    print(sum(map(lambda item: 0 if answer >= item else item - answer, info)), end="\n\n")