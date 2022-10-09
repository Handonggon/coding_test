from collections import deque
def solution(q1, q2):
    answer = 0
    
    limit = 3*(len(q1)+len(q2))-2
    
    if (sum(q1)+sum(q2))%2 != 0:
        return -1
    
    
    
    half = int((sum(q1)+sum(q2))/2)
    
    if max(q1)>half or max(q2)> half:
        return -1
    
    q1 = deque(q1)
    q2 = deque(q2)

    hh1 = sum(q1)
    hh2 = sum(q2)
    
    count = 0
    
    while hh1 != half and count != limit :
        count += 1
        if hh1 > hh2 :
            a = q1.popleft()
            hh1 -= a
            hh2 += a
            q2.append(a)
            answer +=1
        else:
            a = q2.popleft()
            hh2 -= a
            hh1 += a
            q1.append(a)
            answer +=1
    if count == limit:
        return -1
    return answer