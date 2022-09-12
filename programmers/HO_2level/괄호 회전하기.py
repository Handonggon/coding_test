from collections import deque

def solution(s):
    s = deque(s)
    res = 0
    
    for _ in range(len(s)):
        s.append(s.popleft())
        ss  = s.copy()
        
        a = []
        n = 0
        while n < len(s):
            a.append(ss.pop())
            while len(a) >= 2:
                if a[-1] == "{" and a[-2] == "}":
                    a.pop()
                    a.pop()
                elif a[-1] == "(" and a[-2] == ")":
                    a.pop()
                    a.pop()
                elif a[-1] == '[' and a[-2] == ']':
                    a.pop()
                    a.pop()
                else: break
            n += 1
            
        if a == []: res += 1
    
    return res            