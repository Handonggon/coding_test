def solution(n, left, right):
    answer = []
    for i in range(left//n+1,right//n+2) :
        answer += [i] * i + ([k for k in range(i+1,n+1)])
    l = left%n
    return answer[l:l+right-left+1]