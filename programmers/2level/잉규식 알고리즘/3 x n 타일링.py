def solution(n):
    if n%2 == 1 :
        return 0
    else :
        arr = [3,11]
        for i in range(1, n) :
            arr.append((arr[i]*4 - arr[i-1])%1000000007)
        return arr[n//2 -1]