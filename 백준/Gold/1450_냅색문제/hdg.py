[N, C] = list(map(int, input().split()))
info = list(map(int, input().split()))

#[N, C] = [2, 1] #3
#info = [1, 1]

#[N, C] = [2, 2] #4
#info = [1, 1]

#[N, C] = [30, 30] #1073741824
#info = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# 다이나믹 프로그래밍 - 메모리 초과(C = 10^9)

dp = [[0 for _ in range(C+1)] for _ in range(N+1)]
dp[0][0] = 1

for seq in range(1, len(info)):
    for weight in range(len(dp[seq-1])):
        count = dp[seq-1][weight]
        if count > 0:
            dp[seq][weight] += count
            if weight + info[seq] <= C:
                dp[seq][weight + info[seq]] += count

print(sum(dp[N]))


# 이분탐색

def combination(element):
    stack = [[0, 0]]

    result = []
    while stack:
        [weight, index] = stack.pop()
        if index == len(element):
            result.append(weight)
            continue

        stack.append([weight + element[index], index+1])
        stack.append([weight, index+1])

    return result

left = combination(info[ :int(len(info)/2)])
right = sorted(combination(info[int(len(info)/2): ]))

answer = 0
for weight in left:
    [start, end] = [0, len(right)-1]
    while start <= end:
        mid = int((start + end) / 2)

        if right[mid] + weight > C:
            end = mid -1
        else:
            start = mid + 1
    answer += start
print(answer)