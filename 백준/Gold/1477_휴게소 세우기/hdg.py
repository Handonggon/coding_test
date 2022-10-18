[N, M, L] = list(map(int, input().split()))
info = [0] + sorted(list(map(int, input().split()))) + [L]

#[N, M, L] = [3, 1, 1000]
#info = [0] + [200, 701, 800] + [L]

#[N, M, L] = [6, 7, 800]
#info = [0] + sorted([622, 411, 201, 555, 755, 82]) + [L]

def neededMinCount(line):
    count = 0
    for index in range(1, len(info)):
        section = info[index] - info[index-1]
        count += int(section / line)
        if section % line == 0:
            count -= 1
    return count


[left, right] = [1, L-1]


while left <= right:
    mid = int((left + right) / 2)

    if neededMinCount(mid) > M:
        left = mid + 1
    else:
        right = mid - 1

print(left)