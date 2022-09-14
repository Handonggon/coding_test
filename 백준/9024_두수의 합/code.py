#이분 탐색 + 투포인터 풀이
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    S = sorted(list(map(int, input().split())))

    term = 2 * pow(10, 8)
    for i in range(len(S)-2):
        left, right = i+1, len(S)-1

        while left <= right:
            mid = (left + right) // 2
            if S[i] + S[mid] > K:
                right = mid - 1
            else:
                left = mid + 1

            if abs(S[i] + S[mid] - K) == term:
                answer += 1
            elif abs(S[i] + S[mid] - K) < term:
                answer = 1
                term = abs(S[i] + S[mid] - K)
    print(answer)

#투포인터 풀이
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    S = sorted(list(map(int, input().split())))
    term = 2 * pow(10, 8)
    
    left, right = 0, len(S)-1
    while left < right:
        sum = S[left] + S[right]

        if abs(sum - K) == term:
            answer += 1
        elif abs(sum - K) < term:
            answer = 1
            term = abs(sum - K)
        
        if sum == K:
            left += 1
            right -= 1
        elif sum < K:
            left += 1
        elif sum > K:
            right -= 1

    print(answer)