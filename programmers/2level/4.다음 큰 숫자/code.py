def tot(n):
    to2 =""
    while n !=0:
        to2 += str(n%2)
        n = n//2
    return to2[::-1]

def solution(n):
    answer = 0
    num1 = tot(n)
    count1=0
    for i in num1:
        if i =="1":
            count1 += 1
        else:
            pass
    for i in range(n+1,1000001):
        x = tot(i)
        count2=0
        for j in x:
            if j == '1':
                count2 += 1
        if count2 == count1:
            return int(x,2)
시간초과
------------------------------------------------------------------------
def solution(n):
    answer = 0
    num1 = format(n,'b')
    count1=0
    for i in num1:
        if i =="1":
            count1 += 1
        else:
            pass
    for i in range(n+1,1000001):
        x = format(i,'b')
        count2=0
        for j in x:
            if j == '1':
                count2 += 1
        if count2 == count1:
            return int(x,2)