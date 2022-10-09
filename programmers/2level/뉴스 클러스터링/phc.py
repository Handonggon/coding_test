import math

def solution(str1, str2):
    a, b, c = [], [], 0,
    
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            a.append(str1[i:i+2].lower())
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            b.append(str2[i:i+2].lower())
            
    done_box = []
    for i in a:
        if i not in done_box:
            cnt_box = []
            cnt_box.append(a.count(i))
            cnt_box.append(b.count(i))
            c += min(cnt_box)
            done_box.append(i)
                
    d = len(a) + len(b) - c
    
    if c == 0 and d == 0: return 65536
    else: return math.trunc(c/d*65536)