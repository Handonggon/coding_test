def solution(n,a,b):
    cnt, target = 1, 2
    while target != n:
        target = target*2
        cnt += 1
    
    if a <= n // 2 and b > n // 2:
        return cnt
    elif b <= n // 2 and a > n // 2:
        return cnt
    else:
        if abs(a-b) == 1: return 1
    
        cnt_2 = 0
        while True:
            n //= 2
            if a - n >= 0 and b - n >= 0:
                a, b = a - n, b - n
            cnt_2 += 1
            if a == 0 or b == 0: return cnt - cnt_2 + 1
            if a > n and b < n:
                return cnt - cnt_2 + 1
            elif b > n and a < n:
                return cnt - cnt_2 + 1