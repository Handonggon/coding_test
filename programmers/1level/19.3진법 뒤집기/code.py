def solution(n):
    n3 = 0
    while n != 0:
        for i in range(10):
            if n != 0:
                a = 0
                for i in range(1000):
                    if 3**i > n:
                        break
                    else:
                        a += 1
                if 0 < n:
                    n = n - 3**(a-1)
                    n3 += 10**(a-1)
    # n3_re = list(list(str(n3)).reverse())
    n3_re = list(str(n3))
    n3_re.reverse()
    answer = 0
    p = len(n3_re)
    for i in range(p):
        answer += int(n3_re[-1]) * 3**i 
        n3_re.pop(-1)
    return answer