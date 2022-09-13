T = 4
for _ in range(T):
    N, K = 10, 4
    S = sorted([-7, 9, 2, -4, 12, 1, 5, -3, -2, 0])
    term = 2 * pow(10, 8)
    answer = 0
    for i in range(len(S)-1):
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
