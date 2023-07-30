import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    input()
    N = int(input())
    T = list(map(int, input().split()))
    prefix = [0]
    for t in T:
        prefix.append(prefix[-1] + t)
    M1 = int(input())
    P1 = list(map(int, input().split()))
    M2 = int(input())
    P2 = list(map(int, input().split()))

    def getMatches(P):
        match = []
        for index in range(N):
            start = index
            end = index + 1
            isSuccess = True
            for p in P:
                while end <= N and prefix[end] - prefix[start] < p:
                    end += 1
                if end > N or prefix[end] - prefix[start] != p:
                    isSuccess = False
                    break
                start = end
                end = end + 1
            if isSuccess:
                match.append([index + 1, end - 1])
        return match
    
    match1 = getMatches(P1)
    match2 = getMatches(P2)
    count = [0 for _ in range(11001)]
    for [s1, e1] in match1:
        for [s2, e2] in match2:
            if s2 > e1 + 1:
                count[sum(T[e1:s2 - 1])] += 1
    
    print(len(match1), len(match2), count.index(max(count)), max(count))