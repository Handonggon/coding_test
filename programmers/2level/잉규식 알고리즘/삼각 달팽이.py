def solution(n):
    result = [[[] for j in range(i)] for i in range(1,n+1)]
    
    k = 1
    s = 0
    t = 0
    while n > 0 :
        for i in range(s,n+s) :
            result[i][t].append(k)
            k += 1
        n -= 1
        for i in range(n) :
            t += 1
            result[n+s][t].append(k)
            k += 1
        n -= 1
        for i in range(n+s,s,-1) :
            t -= 1
            result[i][t].append(k)
            k += 1
        n -= 1
        s += 2
    
    answer = []
    for i in result :
        temp = []
        for j in i :
            temp += j
        answer += temp
    
    return answer
