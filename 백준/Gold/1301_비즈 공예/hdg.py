import sys
input = sys.stdin.readline

def getKey(array):
    return ''.join(map(lambda item: format(item, '02'), array))

N = int(input())
info = [0] + [int(input()) for _ in range(N)]
dp = [[{} for _ in range(N + 1)] for _ in range(N + 1)]

def dfs(prev, curr):
    if sum(info) == 0:
        return 1
    
    key = getKey(info)
    if key in dp[prev][curr]:
        return dp[prev][curr][key]
    
    dp[prev][curr][key] = 0
    for next in range(len(info)):
        if prev == next or curr == next or info[next] == 0:
            continue
        info[next] -= 1
        dp[prev][curr][key] += dfs(curr, next)
        info[next] += 1
    return dp[prev][curr][key]

print(dfs(0, 0))