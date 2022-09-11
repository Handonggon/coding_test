from collections import deque

def solution(people, limit):
    a = deque(sorted(people))
    res = 0
    
    while True:
        if a:
            b = [a[0]]
            b.append(a.pop())
            if sum(b) > limit:
                res += 1
            else:
                res += 1
                if a:
                    a.popleft()
                else: break
        else: break
            
    return res    