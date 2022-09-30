N = int(input())
server = [list(map(int, input().split())) for _ in range(N)]

left, right = 0, max(max(computer) for computer in server)
half = sum(sum(computer) for computer in server) / 2

def onCount(minute):
    result = 0
    for computer in server:
        for count in computer:
            result += (count if count < minute else minute)
    return result

while left <= right:
    mid = (left + right) // 2

    if onCount(mid) < half:
        left = mid + 1
    else:
        answer = mid
        right = mid - 1

print(answer)