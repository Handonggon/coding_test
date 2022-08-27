from collections import deque
def solution(bridge_length, weight, tw):
    answer = 0
    count = -1
    bri = deque([])
    brw = 0
    des = []
    
    finish = tw
    tw.reverse()
    while des!= finish:
        count += 1
        if len(bri) > 0:
            if count - bri[0][1] == bridge_length:
                a = bri.popleft()
                brw -= a[1]
                des.append(a)                
        b = tw.pop()
        if brw + b <= weight:
            bri.append([b,count])
            brw += b
        else:
            tw.append(b)
        
        
    
    return count