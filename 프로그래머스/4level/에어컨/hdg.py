INF = 10 ** 9
[MIN, MAX] = [-15, 45]

def solution(temperature, t1, t2, a, b, onboard):
    dp = [{key : INF for key in range(MIN, MAX + 1)} for _ in range(len(onboard))]
    dp[0][temperature] = 0
    
    flag = 1 # 에어컨을 가동했을때 온도가 변하는 방향
    if temperature > t2 :
        flag = -1
    
    for curr in range(1, len(onboard)):
        for inner in range(MIN, MAX + 1) if onboard[curr] == 0 else range(t1, t2 + 1):
            # 에어컨 Off
            if inner == temperature:
                dp[curr][inner] = min(dp[curr][inner], dp[curr - 1][inner])
            if MIN <= inner + flag <= MAX:
                dp[curr][inner] = min(dp[curr][inner], dp[curr - 1][inner + flag])
            # 에어컨 On
            dp[curr][inner] = min(dp[curr][inner], dp[curr - 1][inner] + b)
            if MIN <= inner - 1 <= MAX:
                dp[curr][inner] = min(dp[curr][inner], dp[curr - 1][inner - 1] + a)
            if MIN <= inner + 1 <= MAX:
                dp[curr][inner] = min(dp[curr][inner], dp[curr - 1][inner + 1] + a)
    
    return min(dp[len(onboard) - 1].values())