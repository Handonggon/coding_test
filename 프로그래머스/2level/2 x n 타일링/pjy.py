def solution(n):
    answer = 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    a = 1
    b = 2
    while n != 2:
        answer = a+b
        a = b
        b = answer
        n -= 1

    return answer%1000000007