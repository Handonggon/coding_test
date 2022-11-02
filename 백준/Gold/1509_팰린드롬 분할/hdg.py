import sys
input = sys.stdin.readline

str = '#' + input().strip()
#str = 'QWERTYTREWQWERT' #   QWERTYTREWQ W E R T

N = len(str)
dp = [[-1 for x in range(N)] for y in range(N)]

def isPalindrome(left, right):
    if dp[left][right] != -1:
        return dp[left][right]
    if left >= right:
        return 1
    dp[left][right] = (0 if str[left] != str[right] else isPalindrome(left+1, right-1))
    return dp[left][right]

answer = [0 for _ in range(N)]
for i in range(1, N):
    answer[i] = answer[i-1] + 1
    for j in range(1, i):
        if isPalindrome(j, i) == 0:
            continue
        answer[i] = min(answer[i], answer[j-1] + 1)
print(answer[N-1])