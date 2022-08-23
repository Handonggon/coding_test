from collections import deque
def solution(a,b):
    sum_a, sum_b = sum(a), sum(b)
    to = (sum_a + sum_b) // 2
    a, b = deque(a), deque(b)
    res = 0
    while True:
        if sum_a == 0 or sum_b == 0: break
        
        elif sum_a > to:
            a_p = a.popleft()
            sum_a -= a_p
            sum_b += a_p
            b.append(a_p)
            res += 1
            
        elif sum_b > to:
            b_p = b.popleft()
            sum_b -= b_p
            sum_a += b_p
            a.append(b_p)
            res += 1
            
        else: break

    if sum_a != to: return -1
    else: return res