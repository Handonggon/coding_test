def solution(n):
    if n == 1 or n == 2:
        return 1
    box = [0 for _ in range(n+1)]
    box[1], box[2] = 1, 1

    for i in range(3, n+1):
        box[i] = box[i-1] + box[i-2]
        
    return box[n] % 1234567

def solution(n):
    memo = [-1 for _ in range(n+1)]
    
    if memo[n] != -1:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = solution(n-1) + solution(n-2)
    memo[n] = result
    return result % 1234567

def solution(n):
    if n == 1 or n == 2:
        return 1
    else:
        return (solution(n-1) + solution(n-2)) % 1234567