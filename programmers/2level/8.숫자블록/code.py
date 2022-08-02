def block(n):
    if n == 1:
        return 0
    for i in range(2,10000000):
        if n < i:
            break
        mo,na = divmod(n,i)
        if n != i and na ==0:
            return mo
    return 1
def solution(begin,end):
    answer = []
    for i in range(begin,end+1):
        answer.append(block(i))
        
    return answer
#효율성 테스트 실패
------------------------------------------------------