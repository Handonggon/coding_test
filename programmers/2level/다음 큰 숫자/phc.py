def solution(n):
    a=bin(n)
    
    for i in range(n+1, 1000000):
        b=bin(i)
        if a.count('1') == b.count('1'):
            break
    return i