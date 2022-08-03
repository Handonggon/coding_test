def solution(p, s):
    answer = []
    
    for i in range(100):
        count=0
        if len(p) != 0 :
            for j in range(len(p)):
                p[j] += s[j]
            while  p[0] >=100:
                p.pop(0)
                s.pop(0)
                count +=1
                if len(p) ==0:
                    break
            if count != 0:
                answer.append(count)
        else:
            break
    return answer