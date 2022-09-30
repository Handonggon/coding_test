N, M = map(int, input().split())
trees = list(map(int, input().split()))

def sum(height):
    result = 0
    for tree in trees:
        if tree > height:
            result += (tree - height)
    return result

left, right = 1, max(trees)-1

while left <= right:
    mid = (left + right) // 2

    if sum(mid) < M:
        right = mid - 1
    else:
        left = mid + 1

print(right)