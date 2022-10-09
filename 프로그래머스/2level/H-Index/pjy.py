def solution(c):
    
    answer = 0
    c.sort(reverse=True)
    for i in c:
        if i > answer:
            answer += 1
        else:
            return answer    
    return answer