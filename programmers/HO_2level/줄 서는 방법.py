def fun(p):
    cnt = 1
    for i in range(1, p):
        cnt *= i
    return cnt
    
def solution(n,k):
    res = []
    tt = [i for i in range(1, n+1)]
    while n != 0:
        a = 1
        cnt = fun(n)
        while a <= n:
            if cnt * a >= k:
                total = cnt * (a-1)
                res.append(tt[a-1])
                tt.remove(tt[a-1])
                k -= total
                break
            a += 1
        n -= 1
    return res